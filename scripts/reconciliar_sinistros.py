#!/usr/bin/env python3
"""Reconcilia IDs e associação principal em janela comum, sem publicar brutos.

Exige os dois insumos locais. Não altera os processamentos oficiais nem elimina
duplicatas silenciosamente. Emite apenas resumo e divergências dos recortes P1-P9.
"""
from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

import processar_sinistros_distancia as aux
import processar_sinistros_eptc_distancia as eptc

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dados/tratados"
START, END = "20200101", "20250831"
METRICS = ("feridos", "feridos_gr", "fatais", "moto")


def number(row, field):
    return int(float(str(row.get(field) or 0).replace(",", ".")))


def date(row):
    return row["data"].replace("-", "")[:8]


def in_window(row):
    return START <= date(row) <= END


def classify(counterparts, point, osm):
    """Razão observável de ausência no recorte oposto; não causa administrativa."""
    if not counterparts:
        return "id_ausente_no_bruto"
    rows = [r for r in counterparts if in_window(r)]
    if not rows:
        return "data_fora_da_janela"
    coords = [aux.valid_coord(r) for r in rows]
    coords = [c for c in coords if c is not None]
    if not coords:
        return "coordenada_invalida"
    distances = [aux.distance_to_reference(point, *c, osm) for c in coords]
    if min(distances) <= aux.POINTS[point]["primary_m"]:
        raise ValueError(f"Contraparte dentro do recorte mas não associada: {point}")
    return "coordenada_fora_do_limiar"


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main():
    if aux.POINTS != eptc.POINTS:
        raise ValueError("Bases usam referências ou limiares diferentes")
    raw_path = ROOT / "dados/brutos/cat_acidentes.csv"
    with raw_path.open(encoding="utf-8") as f:
        raw_aux = list(csv.DictReader(f, delimiter=";"))
    sources = {"auxiliar": defaultdict(list), "eptc": defaultdict(list)}
    for r in raw_aux:
        sources["auxiliar"][r["idacidente"]].append(r)
    selected = {}
    input_paths = [raw_path, eptc.DBF_PATH, aux.OSM_PATH, Path(__file__).resolve(),
                   Path(aux.__file__).resolve(), Path(eptc.__file__).resolve()]
    for name, prefix in (("auxiliar", ""), ("eptc", "eptc_")):
        path = OUT / f"{prefix}acidentes_associados_distancia.csv"
        input_paths.append(path)
        with path.open(encoding="utf-8") as f:
            rows = [r for r in csv.DictReader(f) if r["associacao_principal"] == "sim" and in_window(r)]
        selected[name] = {(r["ponto"], r["idacidente"]): r for r in rows}
        if len(selected[name]) != len(rows):
            raise ValueError(f"Duplicatas ID/ponto no recorte principal: {name}")
    needed = {i for _, i in selected["auxiliar"].keys() | selected["eptc"].keys()}
    dbf_count = 0
    for rec, get, get_int in eptc.read_dbf_records(eptc.DBF_PATH):
        dbf_count += 1
        if get(rec, "Id") in needed:
            row = eptc.base_row(rec, get, get_int)
            sources["eptc"][row["idacidente"]].append(row)
    osm = aux.load_osm_segments()
    # Detecta derivados obsoletos antes de atribuir divergências à base oposta.
    for source, chosen in selected.items():
        for (point, ident), derived in chosen.items():
            originals = sources[source].get(ident, [])
            if len(originals) != 1:
                raise ValueError(f"ID ausente/ambíguo no próprio bruto: {source}/{ident}")
            original = originals[0]
            coord = aux.valid_coord(original)
            if (not in_window(original) or coord is None or
                    aux.distance_to_reference(point, *coord, osm) > aux.POINTS[point]["primary_m"] or
                    date(original) != date(derived) or any(
                        number(original, k) != number(derived, k) for k in METRICS)):
                raise ValueError(f"Derivado não confere com bruto: {source}/{point}/{ident}")
    details, counts, summary = [], Counter(), []
    common_mismatches = Counter()
    for point in aux.POINTS:
        aa = {i for p, i in selected["auxiliar"] if p == point}
        ee = {i for p, i in selected["eptc"] if p == point}
        summary.append({"ponto": point, "auxiliar": len(aa), "eptc": len(ee),
                        "comuns": len(aa & ee), "so_auxiliar": len(aa-ee), "so_eptc": len(ee-aa)})
        for i in sorted(aa & ee):
            a, e = selected["auxiliar"][(point, i)], selected["eptc"][(point, i)]
            for field in METRICS:
                if number(a, field) != number(e, field):
                    common_mismatches[field] += 1
            if date(a) != date(e):
                common_mismatches["data"] += 1
        for i in sorted(aa ^ ee):
            present = "auxiliar" if i in aa else "eptc"
            absent = "eptc" if i in aa else "auxiliar"
            counterparts = sources[absent].get(i, [])
            category = classify(counterparts, point, osm)
            counts[(point, present, category)] += 1
            item = {"ponto": point, "idacidente": i, "presente_no_recorte": present,
                    "motivo_ausencia_no_outro_recorte": category}
            for source in ("auxiliar", "eptc"):
                rows = sources[source].get(i, [])
                if len(rows) > 1:
                    raise ValueError(f"ID ambíguo no bruto {source}: {i}")
                r = rows[0] if rows else None
                coord = aux.valid_coord(r) if r else None
                item[f"data_{source}"] = date(r) if r else ""
                item[f"distancia_m_{source}"] = round(aux.distance_to_reference(point, *coord, osm), 3) if coord else ""
            details.append(item)
    OUT.mkdir(parents=True, exist_ok=True)
    for name, rows in (("sinistros_reconciliacao_resumo.csv", summary),
                       ("sinistros_reconciliacao_divergencias.csv", details)):
        with (OUT/name).open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
    totals = Counter()
    for (point, source, category), count in counts.items():
        totals[(source, category)] += count
    metadata = {"janela": [START, END], "criterio": "associacao_principal; mesmo ID; sem filtro de vitimas",
                "registros_brutos": {"auxiliar": len(raw_aux), "eptc": dbf_count},
                "auxiliar_cont_vit_zero": sum(aux.int_field(r, "cont_vit") == 0 for r in raw_aux),
                "divergencias_metricas_ids_comuns_por_associacao": dict(common_mismatches),
                "classificacao_por_ponto": [dict(ponto=p, presente_no_recorte=s, motivo=c, n=n)
                    for (p,s,c),n in sorted(counts.items())],
                "insumos_sha256": {str(p.relative_to(ROOT)): sha(p) for p in input_paths}}
    (OUT/"sinistros_reconciliacao_metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2)+"\n")
    lines = ["# Reconciliação das bases de sinistros", "",
        "> Gerado por `scripts/reconciliar_sinistros.py`. Janela comum: **01/01/2020–31/08/2025**. "
        "Associação principal com os mesmos pontos, geometrias e limiares. Os totais oficiais de 2010–2026 não foram alterados.", "",
        "O cruzamento é por ID, procurando a contraparte nos **brutos completos**, inclusive quando ela não tem coordenada válida. "
        "As categorias explicam a inclusão no recorte, não por que a administração alterou ou omitiu o registro. "
        "Ausência de um ID não prova ausência do evento, pois não foi feito pareamento probabilístico entre IDs diferentes.", "",
        "| Ponto | Auxiliar | EPTC | IDs comuns | Só auxiliar | Só EPTC |", "|---|---:|---:|---:|---:|---:|"]
    lines += ["| {ponto} | {auxiliar} | {eptc} | {comuns} | {so_auxiliar} | {so_eptc} |".format(**r) for r in summary]
    lines += ["", "## Decomposição das diferenças", "",
        "| Presente apenas no recorte | Razão observada na outra base | Associações ID/ponto |", "|---|---|---:|"]
    lines += [f"| {s} | `{c}` | {n} |" for (s,c),n in sorted(totals.items())]
    lines += ["", f"São **{len(details)} associações divergentes**, correspondentes a **{len({r['idacidente'] for r in details})} IDs**. "
        "As linhas por ponto não são somáveis como número de eventos únicos. "
        "Não houve divergência de data, feridos, graves, fatais ou motos nas associações comuns." if not common_mismatches else
        f"Divergências nos campos dos IDs comuns: {dict(common_mismatches)}.", "",
        "No P7, os 18 IDs auxiliares também estão no recorte EPTC. Dos 18 adicionais da EPTC, "
        "6 têm coordenada inválida no auxiliar, 11 têm coordenada fora dos 100 m e 1 não consta no bruto auxiliar. "
        "Isso não pode ser explicado simplesmente por inclusão de danos materiais.", "",
        "**Ambas as bases contêm registros sem vítimas registradas.** O auxiliar tem 75.176 linhas; "
        f"{metadata['auxiliar_cont_vit_zero']} têm `cont_vit = 0`. Nenhum dos dois processadores aplica filtro de vítimas.", "",
        "## Rastreabilidade e limites", "",
        "- [Resumo CSV](sinistros_reconciliacao_resumo.csv), [divergências por ID/ponto](sinistros_reconciliacao_divergencias.csv) "
        "e [metadados com hashes](sinistros_reconciliacao_metadata.json). O detalhe contém apenas IDs, datas e distâncias; os brutos permanecem privados.",
        "- Reprodução: `make reconcile-data`, com os dois brutos locais. Não baixa dados nem chama serviços externos.",
        "- Coordenadas diferentes não permitem escolher qual é correta sem boletins/base oficial e validação espacial. "
        "Não foram fundidas as bases nem imputadas localizações.",
        "- O ID 804757 aparece duas vezes no contexto ampliado de P1 e de P2 na EPTC, fora desta janela (02/09/2026). "
        "Não altera os recortes principais. Mantido como recebido, sem deduplicação silenciosa; totais globais devem distinguir linhas, IDs e pares ID/ponto.", ""]
    (OUT/"sinistros_reconciliacao.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Reconciliação: {len(details)} associações divergentes; métricas comuns: {dict(common_mismatches)}")


if __name__ == "__main__":
    main()
