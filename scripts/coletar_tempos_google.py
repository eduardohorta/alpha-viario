#!/usr/bin/env python3
"""Sonda de tempos de viagem via Google Routes API (com travas de custo).

Consulta as rotas de dados/rotas-sonda-tempos.csv e registra duração com
trânsito, duração livre e distância em dados/brutos/tempos_viagem/ (fora do
versionamento). Rodada típica: cron a cada 30 min nas janelas de pico —
ver campo/sonda-tempos-google.md para o setup completo (inclusive as travas
de cobrança do lado do Google, que são a garantia dura).

Travas de custo NESTE script (camada adicional, não a única):
  1. só roda dentro das janelas de pico (06–09h / 17–20h), salvo --force;
  2. teto diário (--max-dia, padrão 160) e mensal (--max-mes, padrão 4500)
     de chamadas, controlado por um livro-razão local persistente;
  3. sem GOOGLE_MAPS_API_KEY no ambiente, roda a seco (lista o que faria).

Uso:
  python3 scripts/coletar_tempos_google.py            # uma rodada (cron)
  python3 scripts/coletar_tempos_google.py --dry-run  # simula, sem chamadas
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROTAS = ROOT / "dados/rotas-sonda-tempos.csv"
OUT_DIR = ROOT / "dados/brutos/tempos_viagem"
OUT_CSV = OUT_DIR / "tempos_google.csv"
LEDGER = OUT_DIR / "ledger.json"

API_URL = "https://routes.googleapis.com/directions/v2:computeRoutes"
FIELD_MASK = "routes.duration,routes.staticDuration,routes.distanceMeters"

# Janelas de coleta (hora local, início inclusivo / fim exclusivo).
JANELAS = [(6, 9), (17, 20)]

CAMPOS_SAIDA = ["timestamp", "rota_id", "ponto_id", "duracao_s",
                "duracao_livre_s", "distancia_m", "status"]


def carregar_rotas(path: Path = ROTAS) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as f:
        rotas = [r for r in csv.DictReader(f) if r.get("ativa", "").strip() == "1"]
    if not rotas:
        raise SystemExit(f"nenhuma rota ativa em {path}")
    return rotas


def dentro_da_janela(agora: dt.datetime) -> bool:
    return any(ini <= agora.hour < fim for ini, fim in JANELAS)


def ler_ledger(path: Path = LEDGER) -> dict[str, int]:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def pode_gastar(ledger: dict[str, int], agora: dt.datetime, n: int,
                max_dia: int, max_mes: int) -> list[str]:
    """Critérios de orçamento violados se gastássemos +n chamadas (vazio = ok)."""
    dia, mes = agora.strftime("%Y-%m-%d"), agora.strftime("%Y-%m")
    problemas = []
    if ledger.get(dia, 0) + n > max_dia:
        problemas.append(f"teto diário: {ledger.get(dia, 0)}+{n} > {max_dia}")
    if ledger.get(mes, 0) + n > max_mes:
        problemas.append(f"teto mensal: {ledger.get(mes, 0)}+{n} > {max_mes}")
    return problemas


def registrar_gasto(ledger: dict[str, int], agora: dt.datetime, n: int,
                    path: Path = LEDGER) -> None:
    dia, mes = agora.strftime("%Y-%m-%d"), agora.strftime("%Y-%m")
    ledger[dia] = ledger.get(dia, 0) + n
    ledger[mes] = ledger.get(mes, 0) + n
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")


def parse_duracao(valor: str | None) -> int | None:
    """'123s' -> 123 (formato Duration da Routes API)."""
    if not valor or not valor.endswith("s"):
        return None
    try:
        return round(float(valor[:-1]))
    except ValueError:
        return None


def consultar_rota(rota: dict[str, str], api_key: str, timeout: int = 20) -> dict:
    corpo = {
        "origin": {"location": {"latLng": {
            "latitude": float(rota["origem_lat"]),
            "longitude": float(rota["origem_lon"])}}},
        "destination": {"location": {"latLng": {
            "latitude": float(rota["destino_lat"]),
            "longitude": float(rota["destino_lon"])}}},
        "travelMode": "DRIVE",
        "routingPreference": "TRAFFIC_AWARE",
    }
    req = urllib.request.Request(
        API_URL, data=json.dumps(corpo).encode("utf-8"),
        headers={"Content-Type": "application/json",
                 "X-Goog-Api-Key": api_key,
                 "X-Goog-FieldMask": FIELD_MASK})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def gravar_linhas(linhas: list[dict], path: Path = OUT_CSV) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    novo = not path.exists()
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS_SAIDA)
        if novo:
            w.writeheader()
        w.writerows(linhas)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true",
                        help="não chama a API; mostra o que faria")
    parser.add_argument("--force", action="store_true",
                        help="ignora a janela de pico (não ignora os tetos)")
    parser.add_argument("--max-dia", type=int, default=160)
    parser.add_argument("--max-mes", type=int, default=4500)
    args = parser.parse_args(argv)

    agora = dt.datetime.now()
    rotas = carregar_rotas()
    api_key = os.environ.get("GOOGLE_MAPS_API_KEY", "")
    seco = args.dry_run or not api_key
    if not api_key and not args.dry_run:
        print("GOOGLE_MAPS_API_KEY ausente — rodando a seco.", file=sys.stderr)

    if not args.force and not dentro_da_janela(agora):
        print(f"Fora da janela de pico ({JANELAS}) às {agora:%H:%M} — nada a fazer. "
              "Use --force para coletar mesmo assim.")
        return 0

    ledger = ler_ledger()
    problemas = pode_gastar(ledger, agora, len(rotas), args.max_dia, args.max_mes)
    if problemas:
        print("Orçamento de chamadas esgotado — coleta recusada: "
              + "; ".join(problemas), file=sys.stderr)
        return 1

    if seco:
        for r in rotas:
            print(f"[seco] {r['rota_id']} ({r['ponto_id']}): "
                  f"{r['origem_lat']},{r['origem_lon']} -> "
                  f"{r['destino_lat']},{r['destino_lon']}")
        print(f"[seco] {len(rotas)} chamadas seriam feitas "
              f"(hoje: {ledger.get(agora.strftime('%Y-%m-%d'), 0)}/{args.max_dia}; "
              f"mês: {ledger.get(agora.strftime('%Y-%m'), 0)}/{args.max_mes}).")
        return 0

    # Registra o gasto ANTES das chamadas: tentativa conta contra o teto,
    # mesmo que falhe — falha de rede não pode virar estouro de orçamento.
    registrar_gasto(ledger, agora, len(rotas))

    linhas, erros = [], 0
    ts = agora.strftime("%Y-%m-%dT%H:%M:%S")
    for r in rotas:
        linha = {"timestamp": ts, "rota_id": r["rota_id"], "ponto_id": r["ponto_id"],
                 "duracao_s": "", "duracao_livre_s": "", "distancia_m": "",
                 "status": "OK"}
        try:
            resp = consultar_rota(r, api_key)
            rota_resp = (resp.get("routes") or [{}])[0]
            linha["duracao_s"] = parse_duracao(rota_resp.get("duration")) or ""
            linha["duracao_livre_s"] = parse_duracao(rota_resp.get("staticDuration")) or ""
            linha["distancia_m"] = rota_resp.get("distanceMeters", "")
            if linha["duracao_s"] == "":
                linha["status"] = "SEM_ROTA"
        except urllib.error.HTTPError as e:
            linha["status"] = f"HTTP_{e.code}"
            erros += 1
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            linha["status"] = f"ERRO_{type(e).__name__}"
            erros += 1
        linhas.append(linha)

    gravar_linhas(linhas)
    print(f"{len(linhas)} rotas coletadas ({erros} erro(s)) -> "
          f"{OUT_CSV.relative_to(ROOT)}")
    return 0 if erros == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
