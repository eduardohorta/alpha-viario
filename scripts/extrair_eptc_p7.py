#!/usr/bin/env python3
"""Filtra o DBF de acidentes da EPTC (2010-202609) por proximidade ao P7.

Fonte: anexo do Pedido 17 (protocolo 017904-26-00, resposta de 22/09/2026),
shapefile ACIDENTES_TRANSITO_2010_202609 (264.567 registros, todo o município),
obtido via link do drive.procempa.com.br indicado pela EPTC. O DBF bruto
(~560 MB) fica em retornos-protocolos/017904-26-00/ (gitignored, fora do
repositório) -- este script não é reexecutável sem esse arquivo local; serve
como registro auditável do método usado, não como pipeline reproduzível via
`make data`. Mesma fórmula de distância (equirretangular, referência de
latitude -30.12) e mesmos limiares (100 m principal / 200 m contexto) do
`processar_sinistros_distancia.py` (Rodada 02, base Dados Abertos POA), para
permitir comparação direta entre as duas fontes.
"""
import struct, math, csv, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DBF = ROOT / "retornos-protocolos/017904-26-00/ACIDENTES_TRANSITO_2010_202609/ACIDENTES_TRANSITO_2010_202609.dbf"
OUT_CSV = ROOT / "dados/tratados/eptc_acidentes_p7_2010_202609.csv"

P7_LAT, P7_LON = -30.13373, -51.17574
EARTH_R = 6_371_000.0
LAT0 = math.radians(-30.12)
PRIMARY_M = 100.0
CONTEXT_M = 200.0

def to_xy(lat, lon):
    lat_r = math.radians(lat)
    lon_r = math.radians(lon)
    x = EARTH_R * lon_r * math.cos(LAT0)
    y = EARTH_R * lat_r
    return x, y

def dist_m(lat1, lon1, lat2, lon2):
    x1, y1 = to_xy(lat1, lon1)
    x2, y2 = to_xy(lat2, lon2)
    return math.hypot(x1 - x2, y1 - y2)

with open(DBF, "rb") as f:
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
        ftype = fh[11:12].decode("latin1")
        flen = fh[16]
        fdec = fh[17]
        fields.append((name, ftype, flen, fdec))

    # compute byte offsets (1 byte deletion flag first)
    offsets = {}
    off = 1
    for name, ftype, flen, fdec in fields:
        offsets[name] = (off, flen, ftype)
        off += flen

    print(f"num_records={num_records} header_size={header_size} record_size={record_size} computed_len={off}")

    f.seek(header_size)
    matches = []
    count_read = 0
    while True:
        rec = f.read(record_size)
        if len(rec) < record_size:
            break
        count_read += 1
        try:
            lat_raw = rec[offsets["Latitude"][0]:offsets["Latitude"][0]+offsets["Latitude"][1]].decode("latin1").strip()
            lon_raw = rec[offsets["Longitude"][0]:offsets["Longitude"][0]+offsets["Longitude"][1]].decode("latin1").strip()
            if not lat_raw or not lon_raw:
                continue
            lat = float(lat_raw)
            lon = float(lon_raw)
        except (ValueError, KeyError):
            continue
        if lat == 0 or lon == 0:
            continue
        d = dist_m(lat, lon, P7_LAT, P7_LON)
        if d <= CONTEXT_M:
            def get(fname):
                o, l, t = offsets[fname]
                return rec[o:o+l].decode("latin1").strip()
            matches.append({
                "Id": get("Id"),
                "Data": get("Data"),
                "Ano": get("Ano"),
                "TipoOcorre": get("TipoOcorre"),
                "LocalLogra": get("LocalLogra"),
                "CruzLograd": get("CruzLograd"),
                "Cruzamento": get("Cruzamento"),
                "Bairro": get("Bairro"),
                "Latitude": lat,
                "Longitude": lon,
                "dist_m": round(d, 1),
                "VitimaGrav": get("VitimaGrav"),
                "Ferido": get("Ferido"),
                "Morte": get("Morte"),
                "Fatais": get("Fatais"),
                "Motociclet": get("Motociclet"),
                "primary": d <= PRIMARY_M,
            })

    print(f"records_scanned={count_read}, matches_within_{CONTEXT_M}m={len(matches)}")

with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    if matches:
        w = csv.DictWriter(f, fieldnames=list(matches[0].keys()))
        w.writeheader()
        w.writerows(matches)

print(f"wrote {OUT_CSV}")
