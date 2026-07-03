#!/usr/bin/env python3
"""Gera o mapa dos pontos (mapas/mapa-pontos.png) a partir do cadastro canônico.

Insumos locais, sem rede: a malha vem de dados/brutos/osm_vias_alpha_viario.json
(© OpenStreetMap, ODbL) e os pontos de dados/pontos.csv via `pontos.load()` —
o mapa nunca diverge do cadastro. Corredores (P4/P6) são traçados como linha;
os demais pontos, como marcador com rótulo.

Uso: python3 scripts/gerar_mapa.py [-o ARQ.png]
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.patheffects as pe  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

import pontos  # mesmo diretório scripts/

ROOT = Path(__file__).resolve().parents[1]
OSM_PATH = ROOT / "dados/brutos/osm_vias_alpha_viario.json"
OUT_DEFAULT = ROOT / "mapas/mapa-pontos.png"

COR_MALHA = "#b8b8b8"
COR_PONTO = "#c0392b"
COR_P4 = "#d35400"
COR_P6 = "#7d5a2f"

# Espessura da malha por classe OSM (o recorte só contém as vias do estudo).
LARGURA = {"primary": 2.2, "primary_link": 2.2, "secondary": 1.6}

# Deslocamento (em pontos tipográficos) de cada rótulo Pn, escolhido para não
# cobrir a via nem os rótulos vizinhos (P1/P2 são próximos).
DESLOC_ROTULO = {
    "P1": (10, -12), "P2": (-14, 12), "P3": (8, 10), "P4": (-26, 2),
    "P5": (-6, 12), "P6": (6, -14), "P7": (10, -4), "P8": (10, 6), "P9": (10, -4),
}

# Referência de orientação: Alphaville Clube (confiança alta — ver
# dados/tratados/georreferenciamento_referencias_demandas.csv).
REF_ALPHAVILLE = (-51.1892160, -30.1259442)

# Rótulos de via (nome curto → âncora manual em lon/lat), só os que orientam o leitor.
VIAS_ROTULADAS = {
    "Estr. das Três Meninas": (-51.1826, -30.1312),
    "Estr. Cristiano Kraemer": (-51.2075, -30.1330),
    "Av. Vicente Monteggia": (-51.2245, -30.1085),
    "Estr. Costa Gama": (-51.1720, -30.1255),
    "Av. da Cavalhada": (-51.2300, -30.1035),
    "Av. Belém Velho": (-51.1965, -30.1145),
}


def _halo(lw: float = 2.5) -> list:
    return [pe.withStroke(linewidth=lw, foreground="white")]


def desenhar(out: Path) -> None:
    osm = json.loads(OSM_PATH.read_text(encoding="utf-8"))
    rows = pontos.load()
    erros = pontos.validate(rows)
    if erros:
        raise SystemExit(f"cadastro inválido, não gero mapa: {erros}")

    fig, ax = plt.subplots(figsize=(10.5, 8.5))

    # Malha viária de fundo.
    for el in osm.get("elements", []):
        geom = el.get("geometry") or []
        if len(geom) < 2:
            continue
        lw = LARGURA.get(el.get("tags", {}).get("highway", ""), 1.0)
        ax.plot([p["lon"] for p in geom], [p["lat"] for p in geom],
                color=COR_MALHA, linewidth=lw, zorder=1, solid_capstyle="round")

    # Corredores (P4/P6) por cima da malha.
    estilo_corredor = {
        "P4": dict(color=COR_P4, linewidth=3.2, zorder=2),
        "P6": dict(color=COR_P6, linewidth=2.6, linestyle=(0, (5, 2)), zorder=2),
    }
    for pid, nomes in pontos.CORRIDOR_WAYS.items():
        for linha in pontos._corridor_lines(nomes):
            ax.plot([c[0] for c in linha], [c[1] for c in linha],
                    solid_capstyle="round", **estilo_corredor[pid])

    # Marcadores e rótulos dos pontos.
    for r in rows:
        pid = r["id"]
        lon, lat = float(r["lon"]), float(r["lat"])
        if pid not in pontos.CORRIDOR_WAYS:
            preliminar = r["status"] == "preliminar"
            ax.plot(lon, lat, "o", markersize=9,
                    markerfacecolor="white" if preliminar else COR_PONTO,
                    markeredgecolor=COR_PONTO, markeredgewidth=1.8, zorder=3)
        ax.annotate(pid, (lon, lat), textcoords="offset points",
                    xytext=DESLOC_ROTULO.get(pid, (8, 8)),
                    fontsize=11, fontweight="bold", color=COR_PONTO,
                    path_effects=_halo(), zorder=4)

    # Referência de orientação (Alphaville Clube).
    ax.plot(*REF_ALPHAVILLE, marker="D", markersize=7, color="#5b7d99",
            linestyle="", zorder=3)
    ax.annotate("Alphaville\n(referência: clube)", REF_ALPHAVILLE,
                textcoords="offset points", xytext=(8, 9), fontsize=8,
                color="#41627e", path_effects=_halo(2.0), zorder=4)

    # Rótulos das vias principais.
    for nome, (lon, lat) in VIAS_ROTULADAS.items():
        ax.text(lon, lat, nome, fontsize=7.5, style="italic", color="#666666",
                ha="center", path_effects=_halo(2.0), zorder=2)

    # Enquadramento e proporção (1° de lon encolhe com cos(lat)).
    lats = [p["lat"] for el in osm["elements"] for p in (el.get("geometry") or [])]
    lons = [p["lon"] for el in osm["elements"] for p in (el.get("geometry") or [])]
    m_lat, m_lon = 0.004, 0.004
    ax.set_xlim(min(lons) - m_lon, max(lons) + m_lon)
    ax.set_ylim(min(lats) - m_lat, max(lats) + m_lat)
    lat_media = (min(lats) + max(lats)) / 2
    ax.set_aspect(1.0 / math.cos(math.radians(lat_media)))
    ax.set_axis_off()

    # Barra de escala: 1 km em graus de longitude na latitude média.
    km_lon = 1.0 / (111.32 * math.cos(math.radians(lat_media)))
    x0 = min(lons) - m_lon + 0.15 * km_lon
    y0 = min(lats) - m_lat + 0.4 * km_lon
    ax.plot([x0, x0 + km_lon], [y0, y0], color="#333333", linewidth=2.5, zorder=5)
    ax.annotate("1 km", (x0 + km_lon / 2, y0), textcoords="offset points",
                xytext=(0, 5), ha="center", fontsize=8, color="#333333",
                path_effects=_halo(2.0), zorder=5)

    # Norte.
    ax.annotate("N", xy=(0.97, 0.90), xytext=(0.97, 0.965), xycoords="axes fraction",
                ha="center", fontsize=11, fontweight="bold", color="#333333",
                arrowprops=dict(arrowstyle="<|-", color="#333333", linewidth=1.6))

    # Legenda.
    itens = [
        plt.Line2D([], [], marker="o", linestyle="", markersize=9,
                   markerfacecolor=COR_PONTO, markeredgecolor=COR_PONTO,
                   label="Ponto de estrangulamento"),
        plt.Line2D([], [], marker="o", linestyle="", markersize=9,
                   markerfacecolor="white", markeredgecolor=COR_PONTO,
                   markeredgewidth=1.8, label="Ponto preliminar (P9)"),
        plt.Line2D([], [], color=COR_P4, linewidth=3.2,
                   label="P4 — corredor Av. Vicente Monteggia"),
        plt.Line2D([], [], color=COR_P6, linewidth=2.6, linestyle=(0, (5, 2)),
                   label="P6 — rota Florestan Fernandes / Kanazawa"),
        plt.Line2D([], [], color=COR_MALHA, linewidth=2.0, label="Vias do estudo (OSM)"),
    ]
    ax.legend(handles=itens, loc="lower right", fontsize=8, framealpha=0.9)

    ax.set_title("Pontos de estrangulamento P1–P9 — entorno do Alphaville Porto Alegre\n"
                 "Vila Nova / Zona Sul · vias municipais", fontsize=12)
    fig.text(0.5, 0.015,
             "Pontos: dados/pontos.csv (cadastro canônico) · Malha: © colaboradores do "
             "OpenStreetMap (ODbL) · Localização aproximada, a validar em campo · "
             "Gerado por scripts/gerar_mapa.py",
             ha="center", fontsize=7, color="#888888")

    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-o", "--out", type=Path, default=OUT_DEFAULT)
    args = parser.parse_args(argv)
    desenhar(args.out)
    try:
        rel = args.out.relative_to(ROOT)
    except ValueError:
        rel = args.out
    print(f"Mapa gravado em {rel}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
