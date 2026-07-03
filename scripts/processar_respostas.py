#!/usr/bin/env python3
"""Tabula as respostas do questionário (curto/base) e gera o resumo agregado.

Entrada: consultas/respostas/respostas.csv no esquema documentado em
consultas/respostas/README.md (uma linha por respondente; campos múltiplos
separados por ";"). Saída: consultas/respostas/resumo-respostas.md, com
ranking de pontos, perfis, períodos, problemas e medidas apoiadas.

O gate de volume mínimo do questionário (LIBERACAO.md / guia §4) pode ser
verificado com --gate/--gate-entorno: o script sai com código 1 se o volume
ainda não foi atingido, imprimindo o progresso.

Uso:
  python3 scripts/processar_respostas.py [CSV] [-o SAIDA.md]
  python3 scripts/processar_respostas.py --gate 50 --gate-entorno 10
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

import pontos  # mesmo diretório scripts/

ROOT = Path(__file__).resolve().parents[1]
CSV_DEFAULT = ROOT / "consultas/respostas/respostas.csv"
OUT_DEFAULT = ROOT / "consultas/respostas/resumo-respostas.md"

COLUNAS = [
    "respondente_id", "data", "origem", "perfil", "ponto_mais_critico",
    "ponto_outro_texto", "periodo_critico", "problemas", "medidas_apoiadas",
    "observacao",
]

# Vocabulários controlados (ver consultas/respostas/README.md para o mapa
# rótulo do formulário → código). Valores fora disso são contados, mas avisados.
PERFIS = {"alphaville", "entorno", "trabalha", "usuario", "outro"}
PERIODOS = {"pico_manha", "meio_dia", "pico_tarde", "fim_de_semana", "varia"}
PROBLEMAS = {"congestionamento", "semaforo", "conversao", "velocidade",
             "pedestre_ciclista", "pavimento", "drenagem", "acidente"}
MEDIDAS = {"reducao_velocidade", "restricao_conversao", "ajuste_semaforo",
           "pavimentar_rota", "rotula_redesenho"}

# Perfis que contam como "de fora do condomínio" para o gate do entorno.
PERFIS_ENTORNO = {"entorno", "trabalha", "usuario", "outro"}


def carregar(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        faltantes = [c for c in COLUNAS if c not in (leitor.fieldnames or [])]
        if faltantes:
            raise SystemExit(f"CSV sem as colunas obrigatórias: {faltantes} "
                             f"(esperado: {COLUNAS})")
        return [r for r in leitor if any((v or "").strip() for v in r.values())]


def _multi(valor: str) -> list[str]:
    return [v.strip() for v in (valor or "").split(";") if v.strip()]


def tabular(rows: list[dict[str, str]], ids_validos: set[str]) -> dict:
    tab: dict = {
        "total": len(rows),
        "perfil": Counter(),
        "origem": Counter(),
        "ponto": Counter(),
        "periodo": Counter(),
        "problemas": Counter(),
        "medidas": Counter(),
        "com_observacao": 0,
        "entorno": 0,
        "avisos": [],
        "datas": sorted({(r.get("data") or "").strip() for r in rows
                         if (r.get("data") or "").strip()}),
    }
    for r in rows:
        rid = (r.get("respondente_id") or "?").strip()
        perfil = (r.get("perfil") or "").strip()
        tab["perfil"][perfil or "(vazio)"] += 1
        if perfil and perfil not in PERFIS:
            tab["avisos"].append(f"{rid}: perfil desconhecido '{perfil}'")
        if perfil in PERFIS_ENTORNO:
            tab["entorno"] += 1

        tab["origem"][(r.get("origem") or "(vazio)").strip() or "(vazio)"] += 1

        ponto = (r.get("ponto_mais_critico") or "").strip()
        if ponto in ids_validos or ponto == "outro":
            tab["ponto"][ponto] += 1
        else:
            tab["ponto"]["(inválido)"] += 1
            tab["avisos"].append(f"{rid}: ponto_mais_critico inválido '{ponto}'")

        periodo = (r.get("periodo_critico") or "").strip()
        tab["periodo"][periodo or "(vazio)"] += 1
        if periodo and periodo not in PERIODOS:
            tab["avisos"].append(f"{rid}: periodo_critico desconhecido '{periodo}'")

        for p in _multi(r.get("problemas", "")):
            tab["problemas"][p] += 1
            if p not in PROBLEMAS:
                tab["avisos"].append(f"{rid}: problema desconhecido '{p}'")
        for m in _multi(r.get("medidas_apoiadas", "")):
            tab["medidas"][m] += 1
            if m not in MEDIDAS:
                tab["avisos"].append(f"{rid}: medida desconhecida '{m}'")

        if (r.get("observacao") or "").strip():
            tab["com_observacao"] += 1
    return tab


def _secao(titulo: str, contador: Counter, total: int) -> list[str]:
    linhas = [f"## {titulo}", "", "| Valor | Respostas | % |", "|---|---:|---:|"]
    for valor, n in sorted(contador.items(), key=lambda kv: (-kv[1], kv[0])):
        pct = 100.0 * n / total if total else 0.0
        linhas += [f"| {valor} | {n} | {pct:.0f}% |"]
    linhas += [""]
    return linhas


def render_md(tab: dict, rows_pontos: list[dict[str, str]]) -> str:
    nomes = {r["id"]: r["nome_curto"] for r in rows_pontos}
    total = tab["total"]
    periodo_dados = (f"{tab['datas'][0]} a {tab['datas'][-1]}"
                     if tab["datas"] else "sem datas informadas")
    linhas = [
        "# Resumo das respostas do questionário (gerado)",
        "",
        "<!-- GERADO por scripts/processar_respostas.py — NÃO editar à mão. -->",
        "",
        f"> **{total} respostas** ({periodo_dados}) · {tab['entorno']} de fora do "
        f"condomínio · {tab['com_observacao']} com observação aberta.",
        "> Uso **agregado e anônimo** — ver [aviso de privacidade](../moradores/aviso-privacidade.md).",
        "",
        "## Ranking — ponto mais crítico",
        "",
        "| Ponto | Respostas | % |",
        "|---|---:|---:|",
    ]
    for ponto, n in sorted(tab["ponto"].items(), key=lambda kv: (-kv[1], kv[0])):
        rotulo = f"**{ponto}** — {nomes[ponto]}" if ponto in nomes else ponto
        pct = 100.0 * n / total if total else 0.0
        linhas += [f"| {rotulo} | {n} | {pct:.0f}% |"]
    linhas += [""]
    linhas += _secao("Perfil dos respondentes", tab["perfil"], total)
    linhas += _secao("Período mais crítico", tab["periodo"], total)
    linhas += _secao("Problemas relatados (múltipla escolha)", tab["problemas"], total)
    linhas += _secao("Medidas que os respondentes apoiariam (múltipla escolha)",
                     tab["medidas"], total)
    if tab["avisos"]:
        linhas += ["## Avisos de consistência", ""]
        linhas += [f"- {a}" for a in tab["avisos"]]
        linhas += [""]
    return "\n".join(linhas) + "\n"


def gate(tab: dict, minimo: int, minimo_entorno: int) -> list[str]:
    """Retorna a lista de critérios ainda não atendidos (vazia = gate ok)."""
    pendencias = []
    if tab["total"] < minimo:
        pendencias.append(f"total: {tab['total']}/{minimo}")
    if tab["entorno"] < minimo_entorno:
        pendencias.append(f"fora do condomínio: {tab['entorno']}/{minimo_entorno}")
    return pendencias


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="?", type=Path, default=CSV_DEFAULT)
    parser.add_argument("-o", "--out", type=Path, default=OUT_DEFAULT)
    parser.add_argument("--gate", type=int, default=None,
                        help="volume mínimo total de respostas (sai com 1 se não atingido)")
    parser.add_argument("--gate-entorno", type=int, default=10,
                        help="mínimo de respostas de fora do condomínio (com --gate)")
    args = parser.parse_args(argv)

    if not args.csv.exists():
        print(f"Ausente: {args.csv} — exporte as respostas do formulário "
              "(ver consultas/respostas/README.md).", file=sys.stderr)
        return 1

    rows_pontos = pontos.load()
    rows = carregar(args.csv)
    tab = tabular(rows, pontos.public_ids(rows_pontos))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render_md(tab, rows_pontos), encoding="utf-8")
    print(f"Resumo gravado em {args.out.relative_to(ROOT)} "
          f"({tab['total']} respostas, {tab['entorno']} de fora do condomínio).")
    for a in tab["avisos"]:
        print(f"  AVISO: {a}", file=sys.stderr)

    if args.gate is not None:
        pendencias = gate(tab, args.gate, args.gate_entorno)
        if pendencias:
            print("Gate do questionário AINDA NÃO atingido — " + "; ".join(pendencias),
                  file=sys.stderr)
            return 1
        print(f"Gate do questionário atingido (≥{args.gate} total, "
              f"≥{args.gate_entorno} de fora do condomínio).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
