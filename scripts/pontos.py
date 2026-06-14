#!/usr/bin/env python3
"""Cadastro canônico dos pontos de estrangulamento (fonte única de verdade).

`dados/pontos.csv` concentra ID, nome, status, coordenadas, confiança e aliases.
Este módulo lê o cadastro e gera artefatos derivados, de modo que README, matrizes,
questionários e mapa nunca divirjam manualmente:

  pontos.py validate            valida a consistência interna do cadastro
  pontos.py geojson [-o ARQ]    gera o GeoJSON (mapa) a partir do cadastro
  pontos.py lista --style EST   imprime a lista de pontos no estilo do documento

Estilos de lista disponíveis: questionario-curto, questionario-base, readme, matriz.

Uso como biblioteca: `from pontos import load, validate`.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "dados/pontos.csv"
GEOJSON_OUT = ROOT / "dados/tratados/pontos.geojson"
OSM_PATH = ROOT / "dados/brutos/osm_vias_alpha_viario.json"

# Vias OSM que compõem cada ponto do tipo corredor — usadas para a geometria de
# linha no mapa. Pontos do tipo 'point' viram Point; corredores viram MultiLineString
# se a malha OSM estiver disponível (senão caem para o ponto representativo).
CORRIDOR_WAYS = {
    "P4": ["Avenida Vicente Monteggia"],
    "P6": ["Rua Florestan Fernandes", "Estrada Kanazawa"],
}

COLUMNS = [
    "id",
    "nome",
    "nome_curto",
    "tipo",
    "geometria",
    "status",
    "lat",
    "lon",
    "confianca_coord",
    "plano_funcional",
    "demanda_origem",
    "aliases",
]

REQUIRED = [c for c in COLUMNS if c not in ("demanda_origem", "aliases")]

VALID = {
    "geometria": {"point", "polyline"},
    "status": {"consolidado", "preliminar"},
    "plano_funcional": {"direta", "parcial", "fora"},
    "confianca_coord": {"alta", "media", "baixa", "referencia_corredor"},
}

# Caixa delimitadora aproximada de Porto Alegre, para validar coordenadas.
POA_BBOX = (-30.6, -29.8, -51.6, -50.8)  # lat_min, lat_max, lon_min, lon_max


def load(path: Path = REGISTRY) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return rows


def aliases_of(row: dict[str, str]) -> list[str]:
    raw = (row.get("aliases") or "").strip()
    return [a.strip() for a in raw.split("|") if a.strip()] if raw else []


def validate(rows: list[dict[str, str]]) -> list[str]:
    """Retorna lista de erros (vazia = cadastro válido)."""
    errors: list[str] = []
    if not rows:
        return ["cadastro vazio"]

    header = list(rows[0].keys())
    if header != COLUMNS:
        errors.append(f"cabeçalho inesperado: {header} != {COLUMNS}")

    ids = [r.get("id", "") for r in rows]
    for dup in sorted({i for i in ids if ids.count(i) > 1}):
        errors.append(f"ID duplicado: {dup}")

    lat_min, lat_max, lon_min, lon_max = POA_BBOX
    for r in rows:
        pid = r.get("id", "?")
        if not re.fullmatch(r"P\d+", pid or ""):
            errors.append(f"{pid}: ID fora do padrão Pn")
        for col in REQUIRED:
            if not (r.get(col) or "").strip():
                errors.append(f"{pid}: campo obrigatório '{col}' vazio")
        for col, allowed in VALID.items():
            val = (r.get(col) or "").strip()
            if val and val not in allowed:
                errors.append(f"{pid}: '{col}'='{val}' fora de {sorted(allowed)}")
        try:
            lat = float(r["lat"])
            lon = float(r["lon"])
            if not (lat_min <= lat <= lat_max and lon_min <= lon <= lon_max):
                errors.append(f"{pid}: coordenada ({lat},{lon}) fora da caixa de POA")
        except (ValueError, KeyError):
            errors.append(f"{pid}: lat/lon não numéricos")

    # IDs devem ser sequenciais P1..Pn (sem buracos), facilitando a verificação P1-P8 vs P1-P9.
    nums = sorted(int(i[1:]) for i in ids if re.fullmatch(r"P\d+", i))
    if nums and nums != list(range(1, max(nums) + 1)):
        errors.append(f"sequência de IDs com buracos: {nums}")

    return errors


def public_ids(rows: list[dict[str, str]]) -> set[str]:
    """IDs que devem aparecer nas listas públicas (todos, hoje)."""
    return {r["id"] for r in rows}


def _corridor_lines(names: list[str]) -> list[list[list[float]]]:
    """LineStrings (em [lon, lat]) das vias OSM com os nomes dados."""
    if not OSM_PATH.exists():
        return []
    data = json.loads(OSM_PATH.read_text(encoding="utf-8"))
    wanted = set(names)
    lines: list[list[list[float]]] = []
    for el in data.get("elements", []):
        if el.get("type") == "way" and el.get("tags", {}).get("name") in wanted:
            geom = el.get("geometry") or []
            if len(geom) >= 2:
                lines.append([[p["lon"], p["lat"]] for p in geom])
    return lines


def to_geojson(rows: list[dict[str, str]]) -> dict:
    features = []
    for r in rows:
        props = {k: r[k] for k in COLUMNS if k not in ("lat", "lon")}
        props["aliases"] = aliases_of(r)
        lines = _corridor_lines(CORRIDOR_WAYS[r["id"]]) if r["id"] in CORRIDOR_WAYS else []
        if lines:
            geometry = {"type": "MultiLineString", "coordinates": lines}
            props["coord_representativa"] = [float(r["lon"]), float(r["lat"])]
        else:
            geometry = {"type": "Point", "coordinates": [float(r["lon"]), float(r["lat"])]}
        features.append({"type": "Feature", "geometry": geometry, "properties": props})
    return {
        "type": "FeatureCollection",
        "metadata": {
            "fonte": "dados/pontos.csv (cadastro canônico)",
            "nota": "Pontos do tipo 'point' são Point; corredores (P4/P6) são MultiLineString da "
            "malha OSM, com 'coord_representativa' nas propriedades para rotulagem.",
        },
        "features": features,
    }


def _label(row: dict[str, str], curto: bool) -> str:
    base = row["nome_curto"] if curto else row["nome"]
    if row.get("status") == "preliminar":
        base += " (preliminar)"
    return base


# Marcadores de região auto-gerada nos documentos.
BEGIN = "<!-- BEGIN pontos:{style} (gerado por scripts/pontos.py — não editar à mão) -->"
END = "<!-- END pontos:{style} -->"

# Documentos com regiões marcadas que `sync` mantém em dia a partir do cadastro.
# Um arquivo pode ter mais de uma região (estilos diferentes).
SYNC_TARGETS = [
    ("consultas/moradores/questionario-curto.md", "questionario-curto"),
    ("consultas/moradores/questionario-base.md", "questionario-base"),
    ("consultas/moradores/questionario-base.md", "bare-mais-critico"),
    ("consultas/moradores/questionario-base.md", "bare-segundo"),
]


def render_list(rows: list[dict[str, str]], style: str) -> str:
    if style == "questionario-curto":
        lines = [f"- [ ] {r['id']} — {_label(r, curto=True)}" for r in rows]
        lines.append("- [ ] Outro: __________________________")
    elif style == "questionario-base":
        lines = [f"- [ ] {r['id']} - {_label(r, curto=False)}" for r in rows]
        lines.append("- [ ] Outro ponto: ______________________________")
    elif style == "readme":
        lines = [f"{i}. **{r['id']}** — {_label(r, curto=True)}" for i, r in enumerate(rows, 1)]
    elif style == "matriz":
        lines = [f"| **{r['id']}** | {r['nome']} | {r['status']} |" for r in rows]
    elif style in ("bare-mais-critico", "bare-segundo"):
        lines = [f"   - [ ] {r['id']}" for r in rows]
        lines.append("   - [ ] Outro: ______________________________")
    else:
        raise SystemExit(f"estilo desconhecido: {style}")
    return "\n".join(lines)


def render_block(rows: list[dict[str, str]], style: str) -> str:
    return f"{BEGIN.format(style=style)}\n{render_list(rows, style)}\n{END.format(style=style)}"


def inject(text: str, rows: list[dict[str, str]], style: str) -> tuple[str, bool]:
    """Substitui a região marcada de `style` em `text`. Retorna (novo_texto, encontrou)."""
    start_tag = BEGIN.format(style=style)
    end_tag = END.format(style=style)
    i = text.find(start_tag)
    j = text.find(end_tag)
    if i == -1 or j == -1 or j < i:
        return text, False
    new = text[:i] + render_block(rows, style) + text[j + len(end_tag):]
    return new, True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("validate", help="valida a consistência do cadastro")

    pg = sub.add_parser("geojson", help="gera o GeoJSON do mapa")
    pg.add_argument("-o", "--out", type=Path, default=GEOJSON_OUT)

    pl = sub.add_parser("lista", help="imprime a lista de pontos em um estilo")
    pl.add_argument("--style", required=True)

    ps = sub.add_parser("sync", help="atualiza as regiões marcadas dos documentos")
    ps.add_argument("--check", action="store_true", help="só verifica se há divergência (não grava)")

    args = parser.parse_args(argv)
    rows = load()

    if args.cmd == "validate":
        errors = validate(rows)
        if errors:
            print("Cadastro inválido:", file=sys.stderr)
            for e in errors:
                print(f"  - {e}", file=sys.stderr)
            return 1
        ordered = sorted(public_ids(rows), key=lambda i: int(i[1:]))
        print(f"Cadastro OK: {len(rows)} pontos ({', '.join(ordered)}).")
        return 0

    if args.cmd == "geojson":
        errors = validate(rows)
        if errors:
            print("Recusando gerar GeoJSON: cadastro inválido (rode 'validate').", file=sys.stderr)
            return 1
        gj = to_geojson(rows)
        args.out.write_text(json.dumps(gj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"GeoJSON gravado em {args.out.relative_to(ROOT)} ({len(rows)} pontos).")
        return 0

    if args.cmd == "lista":
        print(render_list(rows, args.style))
        return 0

    if args.cmd == "sync":
        if validate(rows):
            print("Recusando sincronizar: cadastro inválido (rode 'validate').", file=sys.stderr)
            return 1
        stale: list[str] = []
        for relp, style in SYNC_TARGETS:
            path = ROOT / relp
            text = path.read_text(encoding="utf-8")
            new, found = inject(text, rows, style)
            if not found:
                print(f"AVISO: região '{style}' não encontrada em {relp}", file=sys.stderr)
                continue
            if new != text:
                stale.append(f"{relp} [{style}]")
                if not args.check:
                    path.write_text(new, encoding="utf-8")
        if args.check:
            if stale:
                print("Regiões desatualizadas:\n  - " + "\n  - ".join(stale), file=sys.stderr)
                return 1
            print("Documentos em dia com o cadastro.")
            return 0
        print(f"Sincronizado ({len(stale)} região(ões) atualizada(s)).")
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
