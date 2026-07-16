#!/usr/bin/env python3
"""Agrega a série da sonda de tempos de viagem (Google Routes API) para o dossiê.

Lê o bruto `dados/brutos/tempos_google.csv` (coletado no repositório privado
alpha-viario-sonda; **não versionado aqui**) e emite **apenas agregados** — nunca
os registros brutos da Google Routes API:

  dados/tratados/sonda_tempos_agregado.csv   agregados por rota × janela
  dados/tratados/sonda_tempos_resumo.md      resumo textual para o dossiê

Índice de atraso = duracao_s / duracao_livre_s (>1 = mais lento que o fluxo livre).

Uso:
  python3 scripts/agregar_sonda.py [--input CAMINHO]
"""

from __future__ import annotations

import argparse
import csv
import statistics
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "dados/brutos/tempos_viagem/tempos_google.csv"
ROTAS = ROOT / "dados/rotas-sonda-tempos.csv"
OUT_CSV = ROOT / "dados/tratados/sonda_tempos_agregado.csv"
OUT_MD = ROOT / "dados/tratados/sonda_tempos_resumo.md"

# Pares direcionais (para medir assimetria) e rotas isoladas.
PARES = {
    "P4 — corredor Vicente Monteggia": ("R01", "R02"),
    "P4 — trecho S06 (João Vedana↔João Passuelo)": ("R03", "R04"),
    "P7 — acesso à Costa Gama": ("R05", "R06"),
    "P8 — semáforo Costa Gama × Mariante": ("R07", "R08"),
    "P1–P2 — eixo Cristiano Kraemer": ("R09", "R10"),
}

JANELAS = ["pico_manha", "pico_tarde", "fim_de_semana"]
JANELA_ROTULO = {
    "pico_manha": "pico manhã (dia útil 6–9h)",
    "pico_tarde": "pico tarde (dia útil 17–20h)",
    "fim_de_semana": "fim de semana",
    "outro": "outro",
}


def bucket(ts: str) -> str:
    t = datetime.fromisoformat(ts)
    if t.weekday() >= 5:
        return "fim_de_semana"
    if 6 <= t.hour <= 9:
        return "pico_manha"
    if 17 <= t.hour <= 20:
        return "pico_tarde"
    return "outro"


def load_rotas() -> dict[str, dict[str, str]]:
    with ROTAS.open(encoding="utf-8") as f:
        return {r["rota_id"]: r for r in csv.DictReader(f)}


def median(xs: list[float]) -> float:
    return statistics.median(xs)


def pct(xs: list[float], p: float) -> float:
    if not xs:
        return 0.0
    s = sorted(xs)
    k = min(len(s) - 1, int(round((p / 100) * (len(s) - 1))))
    return s[k]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    args = parser.parse_args(argv)

    if not args.input.exists():
        print(f"Bruto ausente: {args.input.relative_to(ROOT) if args.input.is_absolute() else args.input}. "
              "Rode 'make sonda-agg' (baixa do repo privado da sonda).")
        return 1

    rotas = load_rotas()
    with args.input.open(encoding="utf-8") as f:
        raw = [r for r in csv.DictReader(f) if r.get("status") == "OK"]
    if not raw:
        print("Sem registros OK no bruto.")
        return 1

    datas = [r["timestamp"][:10] for r in raw]
    janela = (min(datas), max(datas))

    # agrupa por (rota, janela)
    grp: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for r in raw:
        grp[(r["rota_id"], bucket(r["timestamp"]))].append(r)

    def agg(rows: list[dict[str, str]]) -> dict[str, float]:
        dur = [float(r["duracao_s"]) for r in rows]
        dist = [float(r["distancia_m"]) for r in rows]
        di = [float(r["duracao_s"]) / float(r["duracao_livre_s"])
              for r in rows if float(r["duracao_livre_s"]) > 0]
        return {
            "n": len(rows),
            "dur_med_s": round(median(dur)),
            "dist_med_m": round(median(dist)),
            "idx_atraso_med": round(median(di), 2),
            "idx_atraso_p85": round(pct(di, 85), 2),
        }

    # CSV de agregados
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fields = ["rota_id", "ponto_id", "janela", "n", "dur_med_s", "dist_med_m",
              "idx_atraso_med", "idx_atraso_p85", "descricao"]
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for rid in sorted(rotas):
            for jan in JANELAS + ["outro"]:
                rows = grp.get((rid, jan))
                if not rows:
                    continue
                a = agg(rows)
                w.writerow({"rota_id": rid, "ponto_id": rotas[rid]["ponto_id"],
                            "janela": jan, **a, "descricao": rotas[rid]["descricao"]})

    _write_resumo(raw, grp, rotas, janela, agg)
    print(f"Agregado {len(raw)} medições ({janela[0]}–{janela[1]}) → "
          f"{OUT_CSV.relative_to(ROOT)} + {OUT_MD.relative_to(ROOT)}.")
    return 0


def _write_resumo(raw, grp, rotas, janela, agg) -> None:
    picos = lambda rid: (grp.get((rid, "pico_manha"), []) + grp.get((rid, "pico_tarde"), []))

    # pior atraso no pico, por rota
    rank = []
    for rid in rotas:
        rows = picos(rid)
        if rows:
            a = agg(rows)
            rank.append((rid, rotas[rid]["ponto_id"], a["idx_atraso_med"], a["idx_atraso_p85"],
                         a["dur_med_s"], rotas[rid]["descricao"]))
    rank.sort(key=lambda x: x[2], reverse=True)

    lines = [
        "# Sonda de tempos de viagem — resumo agregado",
        "",
        f"> **Gerado por `scripts/agregar_sonda.py`.** Janela: **{janela[0]} a {janela[1]}**; "
        f"**{len(raw)} medições** válidas em 12 rotas. Fonte: **Google Routes API** "
        "(sonda própria do projeto, coleta nos picos e fins de semana). "
        "**Indicativo, não substitui medição da EPTC** — pede-se vistoria e contagens oficiais.",
        "> Índice de atraso = duração real ÷ duração em fluxo livre (>1 = mais lento). "
        "Apenas **agregados**; os registros brutos da Google não são publicados.",
        "",
        "## Rotas mais lentas no pico (dia útil)",
        "",
        "| Rota | Ponto | Índice de atraso (mediana) | p85 | Duração mediana | Trecho |",
        "|------|-------|---------------------------:|----:|----------------:|--------|",
    ]
    for rid, pid, dimed, dip85, dur, desc in rank:
        lines.append(f"| {rid} | {pid} | {dimed:.2f} | {dip85:.2f} | {dur//60}min{dur%60:02d}s | {desc} |")

    lines += ["", "## Assimetria direcional no pico", "",
              "| Par | Sentido A | Sentido B | Razão A/B (tempo) |",
              "|-----|----------:|----------:|------------------:|"]
    for nome, (a, b) in PARES.items():
        ra, rb = picos(a), picos(b)
        if not ra or not rb:
            continue
        da, db = median([float(r["duracao_s"]) for r in ra]), median([float(r["duracao_s"]) for r in rb])
        razao = da / db if db else 0
        lines.append(f"| {nome} | {da/60:.1f}min ({a}) | {db/60:.1f}min ({b}) | {razao:.2f}× |")

    # destaque P7
    r05, r06 = picos("R05"), picos("R06")
    if r05 and r06:
        d5 = median([float(r["duracao_s"]) for r in r05])
        di5 = median([float(r["distancia_m"]) for r in r05])
        d6 = median([float(r["duracao_s"]) for r in r06])
        di6 = median([float(r["distancia_m"]) for r in r06])
        lines += ["", "## Destaque — P7 (retorno distante)", "",
                  f"A rota **legalmente disponível** de Três Meninas→Costa Gama (R05, incluindo o "
                  f"retorno distante) leva **{d5/60:.1f} min / {di5/1000:.1f} km** no pico, contra "
                  f"**{d6/60:.1f} min / {di6/1000:.1f} km** do movimento direto permitido (R06) — "
                  f"o desvio **{d5/d6:.1f}× o tempo** e **{di5/di6:.1f}× a distância**. "
                  "É a medida empírica do custo imposto aos moradores pela ausência da conversão/alça."]

    lines += ["", "## Limitações",
              "- Janela curta (série em acumulação); reprocessar perto do protocolo.",
              "- Tempos do Google refletem estimativa de tráfego, não contagem volumétrica.",
              "- Índice <1 em rotas curtas ocorre quando a duração em fluxo livre é conservadora; "
              "os agregados (mediana/p85) são robustos a esses casos.", ""]

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
