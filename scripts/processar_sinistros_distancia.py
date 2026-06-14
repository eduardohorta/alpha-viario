#!/usr/bin/env python3
"""Refina a triagem de sinistros por distancia geometrica aos pontos P1-P8.

O objetivo e substituir a primeira triagem por bounding box/logradouro por uma
base mais auditavel. O script nao produz inferencia causal; apenas associa
registros por proximidade geometrica e separa casos sem coordenada para revisao.
"""

from __future__ import annotations

import csv
import json
import math
import unicodedata
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "dados/brutos/cat_acidentes.csv"
OSM_PATH = ROOT / "dados/brutos/osm_vias_alpha_viario.json"
OUT_DIR = ROOT / "dados/tratados"

EARTH_R = 6_371_000.0
LAT0 = math.radians(-30.12)


POINTS = {
    "P1": {
        "label": "Rotula Estr. 3 Meninas x Estr. Cristiano Kraemer",
        "type": "point",
        "lat": -30.11831,
        "lon": -51.20319,
        "primary_m": 100.0,
        "context_m": 200.0,
    },
    "P2": {
        "label": "Confluencia Cristiano Kraemer x Belem Velho x Monte Cristo",
        "type": "point",
        "lat": -30.11756,
        "lon": -51.20636,
        "primary_m": 100.0,
        "context_m": 200.0,
    },
    "P3": {
        "label": "Acesso Av. Vicente Monteggia via Joao Salomoni/Rodrigues",
        "type": "point",
        "lat": -30.11550,
        "lon": -51.21248,
        "primary_m": 100.0,
        "context_m": 200.0,
    },
    "P4": {
        "label": "Corredor Av. Vicente Monteggia",
        "type": "polyline",
        "road_names": ["Avenida Vicente Monteggia"],
        "primary_m": 50.0,
        "context_m": 100.0,
    },
    "P5": {
        "label": "Joao Salomoni x Av. da Cavalhada",
        "type": "point",
        "lat": -30.11310,
        "lon": -51.22650,
        "primary_m": 100.0,
        "context_m": 200.0,
    },
    "P6": {
        "label": "Rota Florestan Fernandes / Estrada Kanazawa",
        "type": "polyline",
        "road_names": ["Rua Florestan Fernandes", "Estrada Kanazawa"],
        "primary_m": 50.0,
        "context_m": 100.0,
    },
    "P7": {
        "label": "Estr. 3 Meninas x Estr. Costa Gama",
        "type": "point",
        "lat": -30.13373,
        "lon": -51.17574,
        "primary_m": 100.0,
        "context_m": 200.0,
    },
    "P8": {
        "label": "Estr. Costa Gama x Estr. Afonso Lourenco Mariante",
        "type": "point",
        "lat": -30.11518,
        "lon": -51.17707,
        "primary_m": 100.0,
        "context_m": 200.0,
    },
}


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


def point_distance_m(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    x1, y1 = to_xy(lat1, lon1)
    x2, y2 = to_xy(lat2, lon2)
    return math.hypot(x1 - x2, y1 - y2)


def point_segment_distance_m(
    px: float, py: float, ax: float, ay: float, bx: float, by: float
) -> float:
    vx = bx - ax
    vy = by - ay
    wx = px - ax
    wy = py - ay
    seg_len2 = vx * vx + vy * vy
    if seg_len2 == 0:
        return math.hypot(px - ax, py - ay)
    t = max(0.0, min(1.0, (wx * vx + wy * vy) / seg_len2))
    proj_x = ax + t * vx
    proj_y = ay + t * vy
    return math.hypot(px - proj_x, py - proj_y)


def load_osm_segments() -> dict[str, list[tuple[float, float, float, float]]]:
    data = json.loads(OSM_PATH.read_text())
    by_name: dict[str, list[tuple[float, float, float, float]]] = defaultdict(list)
    for element in data.get("elements", []):
        if element.get("type") != "way":
            continue
        name = element.get("tags", {}).get("name")
        geom = element.get("geometry") or []
        if not name or len(geom) < 2:
            continue
        for a, b in zip(geom, geom[1:]):
            ax, ay = to_xy(a["lat"], a["lon"])
            bx, by = to_xy(b["lat"], b["lon"])
            by_name[name].append((ax, ay, bx, by))
    return by_name


def valid_coord(row: dict[str, str]) -> tuple[float, float] | None:
    try:
        lat = float((row.get("latitude") or "").replace(",", "."))
        lon = float((row.get("longitude") or "").replace(",", "."))
    except ValueError:
        return None
    if lat == 0 or lon == 0:
        return None
    if not (-30.5 <= lat <= -29.8 and -51.5 <= lon <= -50.8):
        return None
    return lat, lon


def int_field(row: dict[str, str], name: str) -> int:
    value = (row.get(name) or "").strip()
    if not value:
        return 0
    try:
        return int(float(value.replace(",", ".")))
    except ValueError:
        return 0


def vehicle_onibus(row: dict[str, str]) -> int:
    return (
        int_field(row, "onibus_urb")
        + int_field(row, "onibus_met")
        + int_field(row, "onibus_int")
    )


def road_pair_matches(n1: str, n2: str) -> list[tuple[str, str]]:
    combined = f"{n1} | {n2}"
    matches: list[tuple[str, str]] = []

    def has(*terms: str) -> bool:
        return all(term in combined for term in terms)

    if has("3 MENINAS", "CRISTIANO"):
        matches.append(("P1", "par_logradouros_intersecao"))
    if ("CRISTIANO" in combined and ("BELEM VELHO" in combined or "MONTE CRISTO" in combined)) or has(
        "BELEM VELHO", "MONTE CRISTO"
    ):
        matches.append(("P2", "par_logradouros_intersecao"))
    if "VICENTE MONTEGGIA" in combined and (
        "JOAO SALOMONI" in combined or "RODRIGUES DA FONSECA" in combined
    ):
        matches.append(("P3", "par_logradouros_intersecao"))
    if "VICENTE MONTEGGIA" in combined:
        matches.append(("P4", "logradouro_corredor_sem_coord"))
    if has("JOAO SALOMONI", "CAVALHADA"):
        matches.append(("P5", "par_logradouros_intersecao"))
    if "FLORESTAN FERNANDES" in combined or "KANAZAWA" in combined or "KANASAWA" in combined:
        matches.append(("P6", "logradouro_rota_sem_coord"))
    if has("3 MENINAS", "COSTA GAMA"):
        matches.append(("P7", "par_logradouros_intersecao"))
    if has("COSTA GAMA", "AFONSO LOURENCO MARIANTE"):
        matches.append(("P8", "par_logradouros_intersecao"))
    return matches


def distance_to_reference(
    point_id: str,
    lat: float,
    lon: float,
    osm_segments: dict[str, list[tuple[float, float, float, float]]],
) -> float:
    spec = POINTS[point_id]
    if spec["type"] == "point":
        return point_distance_m(lat, lon, float(spec["lat"]), float(spec["lon"]))

    px, py = to_xy(lat, lon)
    distances = []
    for name in spec["road_names"]:
        for ax, ay, bx, by in osm_segments.get(name, []):
            distances.append(point_segment_distance_m(px, py, ax, ay, bx, by))
    if not distances:
        return float("inf")
    return min(distances)


def base_row(row: dict[str, str]) -> dict[str, str | int]:
    return {
        "idacidente": row.get("idacidente", ""),
        "data": row.get("data", ""),
        "hora": row.get("hora", ""),
        "dia_sem": row.get("dia_sem", ""),
        "latitude": row.get("latitude", ""),
        "longitude": row.get("longitude", ""),
        "log1": row.get("log1", ""),
        "log2": row.get("log2", ""),
        "tipo_acid": row.get("tipo_acid", ""),
        "feridos": int_field(row, "feridos"),
        "feridos_gr": int_field(row, "feridos_gr"),
        "fatais": int_field(row, "fatais"),
        "moto": int_field(row, "moto"),
        "bicicleta": int_field(row, "bicicleta"),
        "onibus": vehicle_onibus(row),
    }


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> None:
    osm_segments = load_osm_segments()

    associated: list[dict[str, object]] = []
    no_coord_review: list[dict[str, object]] = []
    totals = {
        "rows": 0,
        "valid_coord": 0,
        "invalid_coord": 0,
        "relevant_no_coord": 0,
    }
    data_min: str | None = None
    data_max: str | None = None

    with CSV_PATH.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            totals["rows"] += 1
            d = (row.get("data") or "")[:10]
            if d:
                data_min = d if data_min is None or d < data_min else data_min
                data_max = d if data_max is None or d > data_max else data_max
            coord = valid_coord(row)
            n1 = norm(row.get("log1"))
            n2 = norm(row.get("log2"))

            if coord is None:
                totals["invalid_coord"] += 1
                matches = road_pair_matches(n1, n2)
                if matches:
                    totals["relevant_no_coord"] += 1
                    for point_id, method in matches:
                        out = base_row(row)
                        out.update(
                            {
                                "ponto": point_id,
                                "rotulo_ponto": POINTS[point_id]["label"],
                                "metodo_revisao": method,
                                "observacao": "Sem coordenada valida no CSV; nao foi atribuido por distancia.",
                            }
                        )
                        no_coord_review.append(out)
                continue

            totals["valid_coord"] += 1
            lat, lon = coord
            for point_id, spec in POINTS.items():
                distance = distance_to_reference(point_id, lat, lon, osm_segments)
                if distance <= float(spec["context_m"]):
                    out = base_row(row)
                    out.update(
                        {
                            "ponto": point_id,
                            "rotulo_ponto": spec["label"],
                            "tipo_referencia": spec["type"],
                            "dist_m": round(distance, 1),
                            "limiar_principal_m": spec["primary_m"],
                            "associacao_principal": "sim"
                            if distance <= float(spec["primary_m"])
                            else "nao_contexto",
                        }
                    )
                    associated.append(out)

    summary_rows: list[dict[str, object]] = []
    for point_id, spec in POINTS.items():
        rows = [r for r in associated if r["ponto"] == point_id]
        primary = [r for r in rows if r["associacao_principal"] == "sim"]
        context = rows

        def sum_field(items: list[dict[str, object]], field: str) -> int:
            return sum(int(r[field]) for r in items)

        def count_le(max_m: float) -> int:
            return sum(1 for r in rows if float(r["dist_m"]) <= max_m)

        summary_rows.append(
            {
                "ponto": point_id,
                "rotulo_ponto": spec["label"],
                "tipo_referencia": spec["type"],
                "limiar_principal_m": spec["primary_m"],
                "contexto_m": spec["context_m"],
                "ocorrencias_principal": len(primary),
                "ocorrencias_ate_50m": count_le(50.0),
                "ocorrencias_ate_100m": count_le(100.0),
                "ocorrencias_ate_200m": count_le(200.0),
                "feridos_principal": sum_field(primary, "feridos"),
                "feridos_graves_principal": sum_field(primary, "feridos_gr"),
                "fatais_principal": sum_field(primary, "fatais"),
                "motos_principal": sum_field(primary, "moto"),
                "bicicletas_principal": sum_field(primary, "bicicleta"),
                "onibus_principal": sum_field(primary, "onibus"),
                "feridos_contexto": sum_field(context, "feridos"),
                "feridos_graves_contexto": sum_field(context, "feridos_gr"),
                "fatais_contexto": sum_field(context, "fatais"),
                "motos_contexto": sum_field(context, "moto"),
                "bicicletas_contexto": sum_field(context, "bicicleta"),
                "onibus_contexto": sum_field(context, "onibus"),
                "min_dist_m": min((float(r["dist_m"]) for r in rows), default=""),
                "observacao": "Associacao por distancia; nao implica causalidade.",
            }
        )

    manual_rows: list[dict[str, object]] = []
    for point_id in POINTS:
        rows = sorted(
            [r for r in associated if r["ponto"] == point_id],
            key=lambda r: (float(r["dist_m"]), str(r["data"])),
        )
        for rank, row in enumerate(rows[:20], start=1):
            out = dict(row)
            out["ranking_distancia_no_ponto"] = rank
            out["check_manual"] = ""
            manual_rows.append(out)

    summary_fields = [
        "ponto",
        "rotulo_ponto",
        "tipo_referencia",
        "limiar_principal_m",
        "contexto_m",
        "ocorrencias_principal",
        "ocorrencias_ate_50m",
        "ocorrencias_ate_100m",
        "ocorrencias_ate_200m",
        "feridos_principal",
        "feridos_graves_principal",
        "fatais_principal",
        "motos_principal",
        "bicicletas_principal",
        "onibus_principal",
        "feridos_contexto",
        "feridos_graves_contexto",
        "fatais_contexto",
        "motos_contexto",
        "bicicletas_contexto",
        "onibus_contexto",
        "min_dist_m",
        "observacao",
    ]
    associated_fields = [
        "ponto",
        "rotulo_ponto",
        "tipo_referencia",
        "dist_m",
        "limiar_principal_m",
        "associacao_principal",
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
    ]
    no_coord_fields = [
        "ponto",
        "rotulo_ponto",
        "metodo_revisao",
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
        "observacao",
    ]
    manual_fields = ["ranking_distancia_no_ponto", *associated_fields, "check_manual"]

    write_csv(OUT_DIR / "acidentes_resumo_distancia_pontos.csv", summary_rows, summary_fields)
    write_csv(OUT_DIR / "acidentes_associados_distancia.csv", associated, associated_fields)
    write_csv(OUT_DIR / "acidentes_revisao_manual_proximos.csv", manual_rows, manual_fields)
    write_csv(OUT_DIR / "acidentes_sem_coordenada_revisao.csv", no_coord_review, no_coord_fields)

    def overlap_stats(rows: list[dict[str, object]]) -> dict[str, int]:
        by_id: dict[str, set[str]] = defaultdict(set)
        for r in rows:
            by_id[str(r["idacidente"])].add(str(r["ponto"]))
        return {
            "linhas": len(rows),
            "sinistros_distintos": len(by_id),
            "sinistros_multi_ponto": sum(1 for pts in by_id.values() if len(pts) > 1),
        }

    principais = [r for r in associated if r["associacao_principal"] == "sim"]

    metadata = {
        "totais_csv": totals,
        "janela_temporal_fonte": {"campo": "data", "inicio": data_min, "fim": data_max},
        "associacoes": {
            "todas": overlap_stats(associated),
            "principais": overlap_stats(principais),
            "nota": "Totais por ponto NÃO são somáveis: 'sinistros_multi_ponto' contam em mais de "
            "um ponto. Para um agregado, use 'sinistros_distintos'.",
        },
        "referencias": POINTS,
        "arquivos_saida": [
            "dados/tratados/acidentes_resumo_distancia_pontos.csv",
            "dados/tratados/acidentes_associados_distancia.csv",
            "dados/tratados/acidentes_revisao_manual_proximos.csv",
            "dados/tratados/acidentes_sem_coordenada_revisao.csv",
        ],
    }
    (OUT_DIR / "acidentes_distancia_metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
