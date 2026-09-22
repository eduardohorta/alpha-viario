#!/usr/bin/env python3
"""Refina a triagem de sinistros por distancia geometrica aos pontos P1-P9,
usando a base oficial da EPTC (shapefile ACIDENTES_TRANSITO_2010_202609,
264.567 registros, todo o municipio, 2010 a setembro/2026) em vez da base
"Dados Abertos POA" (cat_acidentes.csv, 2020-2025) usada na Rodada 02.

Mesma formula de distancia, mesmos pontos de referencia e mesmos limiares
(100 m/200 m para intersecoes; 50 m/100 m para corredores/rotas) da Rodada 02
(scripts/processar_sinistros_distancia.py), para permitir comparacao direta.

Fonte: anexo do Pedido 17 (protocolo 017904-26-00, resposta de 22/09/2026),
DBF bruto (~560 MB) em retornos-protocolos/017904-26-00/ (gitignored, fora do
repositorio publico) -- este script nao e reexecutavel sem esse arquivo local;
serve como registro auditavel do metodo, nao como pipeline via `make data`.

O script nao produz inferencia causal; apenas associa registros por
proximidade geometrica.
"""

from __future__ import annotations

import csv
import json
import math
import struct
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DBF_PATH = ROOT / "retornos-protocolos/017904-26-00/ACIDENTES_TRANSITO_2010_202609/ACIDENTES_TRANSITO_2010_202609.dbf"
OSM_PATH = ROOT / "dados/brutos/osm_vias_alpha_viario.json"
OUT_DIR = ROOT / "dados/tratados"

EARTH_R = 6_371_000.0
LAT0 = math.radians(-30.12)

# Mesmos pontos, limiares e rotulos do processar_sinistros_distancia.py (Rodada 02).
POINTS = {
    "P1": {"label": "Rotula Estr. 3 Meninas x Estr. Cristiano Kraemer", "type": "point",
           "lat": -30.11831, "lon": -51.20319, "primary_m": 100.0, "context_m": 200.0},
    "P2": {"label": "Confluencia Cristiano Kraemer x Belem Velho x Monte Cristo", "type": "point",
           "lat": -30.11756, "lon": -51.20636, "primary_m": 100.0, "context_m": 200.0},
    "P3": {"label": "Acesso Av. Vicente Monteggia via Joao Salomoni/Rodrigues", "type": "point",
           "lat": -30.11550, "lon": -51.21248, "primary_m": 100.0, "context_m": 200.0},
    "P4": {"label": "Corredor Av. Vicente Monteggia", "type": "polyline",
           "road_names": ["Avenida Vicente Monteggia"], "primary_m": 50.0, "context_m": 100.0},
    "P5": {"label": "Joao Salomoni x Av. da Cavalhada", "type": "point",
           "lat": -30.11310, "lon": -51.22650, "primary_m": 100.0, "context_m": 200.0},
    "P6": {"label": "Rota Florestan Fernandes / Estrada Kanazawa", "type": "polyline",
           "road_names": ["Rua Florestan Fernandes", "Estrada Kanazawa"], "primary_m": 50.0, "context_m": 100.0},
    "P7": {"label": "Estr. 3 Meninas x Estr. Costa Gama", "type": "point",
           "lat": -30.13373, "lon": -51.17574, "primary_m": 100.0, "context_m": 200.0},
    "P8": {"label": "Estr. Costa Gama x Estr. Afonso Lourenco Mariante", "type": "point",
           "lat": -30.11518, "lon": -51.17707, "primary_m": 100.0, "context_m": 200.0},
    "P9": {"label": "Entroncamento Rua Santuario x Av. Oscar Pereira", "type": "point",
           "lat": -30.096763, "lon": -51.178065, "primary_m": 100.0, "context_m": 200.0},
}


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


def point_segment_distance_m(px, py, ax, ay, bx, by) -> float:
    vx, vy = bx - ax, by - ay
    wx, wy = px - ax, py - ay
    seg_len2 = vx * vx + vy * vy
    if seg_len2 == 0:
        return math.hypot(px - ax, py - ay)
    t = max(0.0, min(1.0, (wx * vx + wy * vy) / seg_len2))
    proj_x, proj_y = ax + t * vx, ay + t * vy
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


def distance_to_reference(point_id, lat, lon, osm_segments) -> float:
    spec = POINTS[point_id]
    if spec["type"] == "point":
        return point_distance_m(lat, lon, float(spec["lat"]), float(spec["lon"]))
    px, py = to_xy(lat, lon)
    distances = []
    for name in spec["road_names"]:
        for ax, ay, bx, by in osm_segments.get(name, []):
            distances.append(point_segment_distance_m(px, py, ax, ay, bx, by))
    return min(distances) if distances else float("inf")


def read_dbf_records(path: Path):
    with open(path, "rb") as f:
        header = f.read(32)
        num_records = struct.unpack("<I", header[4:8])[0]
        header_size = struct.unpack("<H", header[8:10])[0]
        record_size = struct.unpack("<H", header[10:12])[0]

        fields = []
        f.seek(32)
        while True:
            fh = f.read(32)
            if fh[0:1] == b"\r":
                break
            name = fh[0:11].split(b"\x00")[0].decode("latin1")
            flen = fh[16]
            fields.append((name, flen))

        offsets = {}
        off = 1
        for name, flen in fields:
            offsets[name] = (off, flen)
            off += flen
        assert off == record_size, f"offset mismatch: {off} != {record_size}"

        f.seek(header_size)

        def get(rec, fname):
            o, l = offsets[fname]
            return rec[o:o + l].decode("latin1").strip()

        def get_int(rec, fname):
            v = get(rec, fname)
            try:
                return int(float(v)) if v else 0
            except ValueError:
                return 0

        for _ in range(num_records):
            rec = f.read(record_size)
            if len(rec) < record_size:
                break
            yield rec, get, get_int


def base_row(rec, get, get_int) -> dict:
    return {
        "idacidente": get(rec, "Id"),
        "data": get(rec, "Data"),
        "hora": get(rec, "HoraAproxi"),
        "dia_sem": get(rec, "DiaSemana"),
        "latitude": get(rec, "Latitude"),
        "longitude": get(rec, "Longitude"),
        "log1": get(rec, "LocalLogra"),
        "log2": get(rec, "CruzLograd"),
        "tipo_acid": get(rec, "TipoOcorre"),
        "feridos": get_int(rec, "Ferido"),
        "feridos_gr": get_int(rec, "VitimaGrav"),
        "fatais": get_int(rec, "Fatais"),
        "moto": get_int(rec, "Motociclet"),
        "bicicleta": get_int(rec, "Bicicleta"),
        "onibus": get_int(rec, "Onibus") + get_int(rec, "OnibusMetr") + get_int(rec, "OnibusUrba"),
    }


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> None:
    osm_segments = load_osm_segments()

    associated: list[dict] = []
    totals = {"rows": 0, "valid_coord": 0, "invalid_coord": 0}
    data_min = data_max = None

    for rec, get, get_int in read_dbf_records(DBF_PATH):
        totals["rows"] += 1
        d = get(rec, "Data")[:8]
        if d:
            data_min = d if data_min is None or d < data_min else data_min
            data_max = d if data_max is None or d > data_max else data_max

        try:
            lat = float(get(rec, "Latitude"))
            lon = float(get(rec, "Longitude"))
        except ValueError:
            totals["invalid_coord"] += 1
            continue
        if lat == 0 or lon == 0 or not (-30.5 <= lat <= -29.8 and -51.5 <= lon <= -50.8):
            totals["invalid_coord"] += 1
            continue
        totals["valid_coord"] += 1

        row = base_row(rec, get, get_int)
        for point_id, spec in POINTS.items():
            distance = distance_to_reference(point_id, lat, lon, osm_segments)
            if distance <= float(spec["context_m"]):
                out = dict(row)
                out.update({
                    "ponto": point_id,
                    "rotulo_ponto": spec["label"],
                    "tipo_referencia": spec["type"],
                    "dist_m": round(distance, 1),
                    "limiar_principal_m": spec["primary_m"],
                    "associacao_principal": "sim" if distance <= float(spec["primary_m"]) else "nao_contexto",
                })
                associated.append(out)

    summary_rows = []
    for point_id, spec in POINTS.items():
        rows = [r for r in associated if r["ponto"] == point_id]
        primary = [r for r in rows if r["associacao_principal"] == "sim"]

        def sum_field(items, field):
            return sum(int(r[field]) for r in items)

        def count_le(max_m):
            return sum(1 for r in rows if float(r["dist_m"]) <= max_m)

        summary_rows.append({
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
            "min_dist_m": min((float(r["dist_m"]) for r in rows), default=""),
            "observacao": "Associacao por distancia (base EPTC 2010-202609); nao implica causalidade.",
        })

    summary_fields = [
        "ponto", "rotulo_ponto", "tipo_referencia", "limiar_principal_m", "contexto_m",
        "ocorrencias_principal", "ocorrencias_ate_50m", "ocorrencias_ate_100m", "ocorrencias_ate_200m",
        "feridos_principal", "feridos_graves_principal", "fatais_principal",
        "motos_principal", "bicicletas_principal", "onibus_principal",
        "min_dist_m", "observacao",
    ]
    associated_fields = [
        "ponto", "rotulo_ponto", "tipo_referencia", "dist_m", "limiar_principal_m", "associacao_principal",
        "idacidente", "data", "hora", "dia_sem", "latitude", "longitude", "log1", "log2", "tipo_acid",
        "feridos", "feridos_gr", "fatais", "moto", "bicicleta", "onibus",
    ]

    write_csv(OUT_DIR / "eptc_acidentes_resumo_distancia_pontos.csv", summary_rows, summary_fields)
    write_csv(OUT_DIR / "eptc_acidentes_associados_distancia.csv", associated, associated_fields)

    def overlap_stats(rows):
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
        "fonte": "Shapefile EPTC ACIDENTES_TRANSITO_2010_202609, anexo do Pedido 17 (017904-26-00, 22/09/2026)",
        "totais_dbf": totals,
        "janela_temporal_fonte": {"campo": "Data", "inicio": data_min, "fim": data_max},
        "associacoes": {
            "todas": overlap_stats(associated),
            "principais": overlap_stats(principais),
            "nota": "Totais por ponto NAO sao somaveis: 'sinistros_multi_ponto' contam em mais de "
                    "um ponto. Para um agregado, use 'sinistros_distintos'.",
        },
        "referencias": POINTS,
        "arquivos_saida": [
            "dados/tratados/eptc_acidentes_resumo_distancia_pontos.csv",
            "dados/tratados/eptc_acidentes_associados_distancia.csv",
        ],
    }
    (OUT_DIR / "eptc_acidentes_distancia_metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"registros lidos: {totals['rows']}, com coordenada valida: {totals['valid_coord']}")
    print(f"associacoes (contexto): {len(associated)}, principais: {len(principais)}")
    for row in summary_rows:
        print(row["ponto"], row["ocorrencias_principal"], "principal;", row["ocorrencias_ate_200m"], "ate 200m")


if __name__ == "__main__":
    main()
