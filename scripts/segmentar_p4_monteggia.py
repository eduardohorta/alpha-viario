#!/usr/bin/env python3
"""Segmenta os sinistros do P4 ao longo da Av. Vicente Monteggia.

Entrada principal: `dados/tratados/acidentes_associados_distancia.csv`, ja
filtrada na Rodada 02 por proximidade da geometria OSM. Esta rotina apenas
projeta os registros P4 no eixo OSM da Monteggia e resume trechos entre marcos
de intersecao observados nos proprios registros geocodificados.
"""

from __future__ import annotations

import csv
import heapq
import json
import math
import statistics
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OSM_PATH = ROOT / "dados/brutos/osm_vias_alpha_viario.json"
ASSOCIADOS_PATH = ROOT / "dados/tratados/acidentes_associados_distancia.csv"
OUT_DIR = ROOT / "dados/tratados"

EARTH_R = 6_371_000.0
LAT0 = math.radians(-30.12)

VM_NAME = "Avenida Vicente Monteggia"
VM_NORM = "AV VICENTE MONTEGGIA"


def norm(text: str | None) -> str:
    if not text:
        return ""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return " ".join(text.upper().replace(".", " ").replace("-", " ").split())


def to_xy(lat: float, lon: float) -> tuple[float, float]:
    lat_r = math.radians(lat)
    lon_r = math.radians(lon)
    x = EARTH_R * lon_r * math.cos(LAT0)
    y = EARTH_R * lat_r
    return x, y


def coord_dist_m(a: tuple[float, float], b: tuple[float, float]) -> float:
    ax, ay = to_xy(*a)
    bx, by = to_xy(*b)
    return math.hypot(ax - bx, ay - by)


def segment_projection(
    px: float, py: float, ax: float, ay: float, bx: float, by: float
) -> tuple[float, float]:
    vx = bx - ax
    vy = by - ay
    wx = px - ax
    wy = py - ay
    seg_len2 = vx * vx + vy * vy
    if seg_len2 == 0:
        return math.hypot(px - ax, py - ay), 0.0
    t = max(0.0, min(1.0, (wx * vx + wy * vy) / seg_len2))
    proj_x = ax + t * vx
    proj_y = ay + t * vy
    return math.hypot(px - proj_x, py - proj_y), t


def load_vm_graph() -> dict[tuple[float, float], list[tuple[tuple[float, float], float]]]:
    data = json.loads(OSM_PATH.read_text())
    graph: dict[tuple[float, float], list[tuple[tuple[float, float], float]]] = {}

    def key(point: dict[str, float]) -> tuple[float, float]:
        return (round(float(point["lat"]), 7), round(float(point["lon"]), 7))

    for element in data.get("elements", []):
        if element.get("type") != "way":
            continue
        if element.get("tags", {}).get("name") != VM_NAME:
            continue
        geom = element.get("geometry") or []
        for a, b in zip(geom, geom[1:]):
            ka = key(a)
            kb = key(b)
            weight = coord_dist_m(ka, kb)
            graph.setdefault(ka, []).append((kb, weight))
            graph.setdefault(kb, []).append((ka, weight))

    if not graph:
        raise RuntimeError("Geometria da Avenida Vicente Monteggia nao localizada no OSM.")
    return graph


def nearest_node(
    graph: dict[tuple[float, float], list[tuple[tuple[float, float], float]]],
    target: tuple[float, float],
) -> tuple[float, float]:
    return min(graph, key=lambda node: coord_dist_m(node, target))


def shortest_path(
    graph: dict[tuple[float, float], list[tuple[tuple[float, float], float]]],
    start: tuple[float, float],
    end: tuple[float, float],
) -> list[tuple[float, float]]:
    queue: list[tuple[float, tuple[float, float]]] = [(0.0, start)]
    distances = {start: 0.0}
    previous: dict[tuple[float, float], tuple[float, float]] = {}
    visited: set[tuple[float, float]] = set()

    while queue:
        current_dist, current = heapq.heappop(queue)
        if current in visited:
            continue
        visited.add(current)
        if current == end:
            break
        for neighbor, weight in graph[current]:
            next_dist = current_dist + weight
            if next_dist < distances.get(neighbor, float("inf")):
                distances[neighbor] = next_dist
                previous[neighbor] = current
                heapq.heappush(queue, (next_dist, neighbor))

    if end not in distances:
        raise RuntimeError("Nao foi possivel construir caminho continuo para P4.")

    path = [end]
    current = end
    while current != start:
        current = previous[current]
        path.append(current)
    path.reverse()
    return path


def build_axis() -> tuple[list[dict[str, object]], float]:
    graph = load_vm_graph()
    # Extremidades OSM do eixo P4 no recorte local: Cavalhada/Nonoai e Joao Salomoni.
    start = nearest_node(graph, (-30.0951734, -51.2258212))
    end = nearest_node(graph, (-30.1155340, -51.2125347))
    path = shortest_path(graph, start, end)

    segments: list[dict[str, object]] = []
    station = 0.0
    for a, b in zip(path, path[1:]):
        ax, ay = to_xy(*a)
        bx, by = to_xy(*b)
        length = math.hypot(ax - bx, ay - by)
        segments.append(
            {
                "from_m": station,
                "to_m": station + length,
                "a": a,
                "b": b,
                "ax": ax,
                "ay": ay,
                "bx": bx,
                "by": by,
            }
        )
        station += length
    return segments, station


def project_station(
    lat: float, lon: float, axis_segments: list[dict[str, object]]
) -> tuple[float, float]:
    px, py = to_xy(lat, lon)
    best_dist = float("inf")
    best_station = 0.0
    for segment in axis_segments:
        distance, t = segment_projection(
            px,
            py,
            float(segment["ax"]),
            float(segment["ay"]),
            float(segment["bx"]),
            float(segment["by"]),
        )
        station = float(segment["from_m"]) + t * (
            float(segment["to_m"]) - float(segment["from_m"])
        )
        if distance < best_dist:
            best_dist = distance
            best_station = station
    return best_station, best_dist


def int_field(row: dict[str, str], name: str) -> int:
    value = (row.get(name) or "").strip()
    if not value:
        return 0
    return int(float(value.replace(",", ".")))


def load_p4_records(axis_segments: list[dict[str, object]]) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    with ASSOCIADOS_PATH.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("ponto") != "P4" or row.get("associacao_principal") != "sim":
                continue
            lat = float(row["latitude"])
            lon = float(row["longitude"])
            station_m, eixo_dist_m = project_station(lat, lon, axis_segments)
            out = dict(row)
            out["estacao_m"] = round(station_m, 1)
            out["dist_eixo_p4_m"] = round(eixo_dist_m, 1)
            records.append(out)
    return records


def observed_intersection_markers(records: list[dict[str, object]]) -> list[dict[str, object]]:
    stations_by_name: dict[str, list[float]] = defaultdict(list)
    for row in records:
        names = {norm(str(row.get("log1", ""))), norm(str(row.get("log2", "")))}
        for name in names:
            if not name or name == VM_NORM:
                continue
            stations_by_name[name].append(float(row["estacao_m"]))

    markers: list[dict[str, object]] = []
    for name, stations in stations_by_name.items():
        if len(stations) < 2:
            continue
        markers.append(
            {
                "logradouro": name,
                "n_registros": len(stations),
                "estacao_mediana_m": round(statistics.median(stations), 1),
                "estacao_min_m": round(min(stations), 1),
                "estacao_max_m": round(max(stations), 1),
            }
        )
    markers.sort(key=lambda row: (float(row["estacao_mediana_m"]), str(row["logradouro"])))
    return markers


def build_breakpoints(total_length_m: float) -> list[dict[str, object]]:
    # Marcos observados nos registros P4 e compatibilizados com a direcao OSM
    # Cavalhada/Nonoai -> Joao Salomoni. As posicoes sao aproximacoes
    # longitudinais, nao coordenadas cadastrais oficiais.
    return [
        {
            "id": "M0",
            "estacao_m": 0.0,
            "rotulo": "Av. da Cavalhada / Av. Nonoai / R. Dr. Campos Velho",
        },
        {"id": "M1", "estacao_m": 271.0, "rotulo": "Av. Fabio Araujo Santos"},
        {"id": "M2", "estacao_m": 673.0, "rotulo": "Av. Otto Niemeyer"},
        {"id": "M3", "estacao_m": 1197.0, "rotulo": "Estr. Aracaju"},
        {"id": "M4", "estacao_m": 1474.0, "rotulo": "Rua Amapa"},
        {"id": "M5", "estacao_m": 1934.0, "rotulo": "Estr. Joao Vedana"},
        {"id": "M6", "estacao_m": 2644.0, "rotulo": "Estr. Joao Passuelo"},
        {
            "id": "M7",
            "estacao_m": round(total_length_m, 1),
            "rotulo": "Av. Joao Salomoni / Av. Rodrigues da Fonseca",
        },
    ]


def segment_for_station(
    station_m: float, breakpoints: list[dict[str, object]]
) -> dict[str, object]:
    for index, (a, b) in enumerate(zip(breakpoints, breakpoints[1:]), start=1):
        start = float(a["estacao_m"])
        end = float(b["estacao_m"])
        if start <= station_m < end or (
            index == len(breakpoints) - 1 and station_m <= end
        ):
            return {
                "segmento_id": f"P4-S{index:02d}",
                "trecho": f'{a["rotulo"]} -> {b["rotulo"]}',
                "inicio_m": start,
                "fim_m": end,
                "extensao_m": round(end - start, 1),
            }
    raise RuntimeError(f"Estacao fora dos marcos P4: {station_m}")


def summarize_segments(
    records: list[dict[str, object]], breakpoints: list[dict[str, object]]
) -> list[dict[str, object]]:
    by_segment: dict[str, list[dict[str, object]]] = defaultdict(list)
    segment_specs: dict[str, dict[str, object]] = {}
    for row in records:
        spec = segment_for_station(float(row["estacao_m"]), breakpoints)
        row.update(spec)
        by_segment[str(spec["segmento_id"])].append(row)
        segment_specs[str(spec["segmento_id"])] = spec

    summaries: list[dict[str, object]] = []
    for segment_id in sorted(segment_specs):
        spec = segment_specs[segment_id]
        rows = by_segment[segment_id]
        extensao_km = float(spec["extensao_m"]) / 1000.0
        pairs = Counter(
            f'{row.get("log1", "").strip()} | {row.get("log2", "").strip()}'.strip()
            for row in rows
        )
        fatal_ids = [
            str(row["idacidente"]) for row in rows if int_field(row, "fatais") > 0
        ]
        summaries.append(
            {
                "segmento_id": segment_id,
                "trecho": spec["trecho"],
                "inicio_m": spec["inicio_m"],
                "fim_m": spec["fim_m"],
                "extensao_m": spec["extensao_m"],
                "ocorrencias": len(rows),
                "ocorrencias_por_km": round(len(rows) / extensao_km, 1)
                if extensao_km
                else "",
                "feridos": sum(int_field(row, "feridos") for row in rows),
                "feridos_graves": sum(int_field(row, "feridos_gr") for row in rows),
                "fatais": sum(int_field(row, "fatais") for row in rows),
                "motos": sum(int_field(row, "moto") for row in rows),
                "bicicletas": sum(int_field(row, "bicicleta") for row in rows),
                "onibus": sum(int_field(row, "onibus") for row in rows),
                "ids_fatais": ";".join(fatal_ids),
                "pares_logradouro_mais_comuns": " || ".join(
                    f"{pair} ({count})" for pair, count in pairs.most_common(5)
                ),
            }
        )
    return summaries


def summarize_bins(records: list[dict[str, object]], total_length_m: float) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    bin_size = 250.0
    rounded_total = round(total_length_m, 1)
    start = 0.0
    while start < total_length_m:
        end = min(start + bin_size, total_length_m)
        selected = [
            row
            for row in records
            if start <= float(row["estacao_m"]) < end
            or (
                end == total_length_m
                and start <= float(row["estacao_m"]) <= rounded_total
            )
        ]
        if selected:
            rows.append(
                {
                    "janela_id": f"{int(start):04d}_{int(end):04d}m",
                    "inicio_m": round(start, 1),
                    "fim_m": round(end, 1),
                    "ocorrencias": len(selected),
                    "feridos": sum(int_field(row, "feridos") for row in selected),
                    "feridos_graves": sum(
                        int_field(row, "feridos_gr") for row in selected
                    ),
                    "fatais": sum(int_field(row, "fatais") for row in selected),
                    "motos": sum(int_field(row, "moto") for row in selected),
                    "bicicletas": sum(int_field(row, "bicicleta") for row in selected),
                    "onibus": sum(int_field(row, "onibus") for row in selected),
                }
            )
        start += bin_size
    rows.sort(
        key=lambda row: (
            -int(row["fatais"]),
            -int(row["feridos_graves"]),
            -int(row["ocorrencias"]),
        )
    )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    axis_segments, total_length_m = build_axis()
    records = load_p4_records(axis_segments)
    markers = observed_intersection_markers(records)
    breakpoints = build_breakpoints(total_length_m)
    segment_summaries = summarize_segments(records, breakpoints)
    bin_summaries = summarize_bins(records, total_length_m)

    write_csv(
        OUT_DIR / "acidentes_p4_marcos_intersecoes.csv",
        markers,
        [
            "logradouro",
            "n_registros",
            "estacao_mediana_m",
            "estacao_min_m",
            "estacao_max_m",
        ],
    )
    write_csv(
        OUT_DIR / "acidentes_p4_segmentos.csv",
        segment_summaries,
        [
            "segmento_id",
            "trecho",
            "inicio_m",
            "fim_m",
            "extensao_m",
            "ocorrencias",
            "ocorrencias_por_km",
            "feridos",
            "feridos_graves",
            "fatais",
            "motos",
            "bicicletas",
            "onibus",
            "ids_fatais",
            "pares_logradouro_mais_comuns",
        ],
    )
    write_csv(
        OUT_DIR / "acidentes_p4_registros_segmentados.csv",
        records,
        [
            "segmento_id",
            "trecho",
            "estacao_m",
            "dist_eixo_p4_m",
            "idacidente",
            "data",
            "hora",
            "dia_sem",
            "latitude",
            "longitude",
            "log1",
            "log2",
            "tipo_acid",
            "feridos",
            "feridos_gr",
            "fatais",
            "moto",
            "bicicleta",
            "onibus",
        ],
    )
    write_csv(
        OUT_DIR / "acidentes_p4_hotspots_250m.csv",
        bin_summaries,
        [
            "janela_id",
            "inicio_m",
            "fim_m",
            "ocorrencias",
            "feridos",
            "feridos_graves",
            "fatais",
            "motos",
            "bicicletas",
            "onibus",
        ],
    )

    metadata = {
        "eixo_osm": VM_NAME,
        "comprimento_eixo_m": round(total_length_m, 1),
        "registros_p4_principais": len(records),
        "metodo": (
            "projecao dos registros P4 no caminho OSM da Av. Vicente Monteggia; "
            "segmentos por marcos de intersecao observados nos logradouros dos "
            "proprios sinistros"
        ),
        "limite": (
            "segmentacao preliminar; marcos nao substituem base cadastral oficial "
            "nem validacao visual em mapa/aerofoto"
        ),
    }
    (OUT_DIR / "acidentes_p4_segmentacao_metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
