#!/usr/bin/env python3
"""Sonda multi-fonte de tempos de viagem (TomTom · HERE · Waze · Google).

Complementa a sonda Google (scripts/coletar_tempos_google.py) medindo as MESMAS
rotas de dados/rotas-sonda-tempos.csv por fontes independentes, para validação
cruzada — "três fontes confirmam +X min no pico" é muito mais forte do que uma.
Grava em formato longo (uma linha por rota × fonte) em
dados/brutos/tempos_viagem/tempos_multifonte.csv (fora do versionamento, como a
sonda Google; os agregados entram no dossiê ao fim da campanha).

Fontes e custo (todas no nível gratuito; o script nunca ultrapassa a cota):
  - TomTom Routing   grátis ~2.500/dia   duração com trânsito + tempo livre → índice
  - HERE Routing v8  grátis (freemium)    duração com trânsito + baseDuration (livre)
  - Waze (não oficial)   opcional          requer `pip install WazeRouteCalculator`
  - Google Routes    só com --com-google   já coberto pela sonda Google; aqui só p/ cruzar

Chaves via ambiente (NUNCA no repositório):
  TOMTOM_API_KEY, HERE_API_KEY, GOOGLE_MAPS_API_KEY
Sem a chave de uma fonte, ela é pulada (registrada como SEM_CHAVE). Ver o setup
completo em campo/sonda-tempos-multifonte.md.

Travas de custo (camada adicional; a cota do provedor é a trava dura):
  1. só roda dentro das janelas de pico (06–09h / 17–20h), salvo --force;
  2. teto diário por fonte (--max-dia, padrão 300) num livro-razão local persistente;
  3. sem a chave da fonte, ela roda a seco (é pulada).

Uso:
  python3 scripts/coletar_tempos_multifonte.py              # uma rodada (cron)
  python3 scripts/coletar_tempos_multifonte.py --dry-run    # simula, sem chamadas
  python3 scripts/coletar_tempos_multifonte.py --force      # ignora a janela de pico
  python3 scripts/coletar_tempos_multifonte.py --force --com-google
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROTAS = ROOT / "dados/rotas-sonda-tempos.csv"
OUT_DIR = ROOT / "dados/brutos/tempos_viagem"
OUT_CSV = OUT_DIR / "tempos_multifonte.csv"
LEDGER = OUT_DIR / "ledger_multifonte.json"

TIMEOUT = 20
WAZE_REGION = "EU"        # servidor do Waze que responde para Porto Alegre
WAZE_DELAY_S = 0.6        # pausa entre chamadas (gentil com o endpoint não oficial)

# Janelas de pico (hora local). Google só coleta aqui (SKU Pro, cota curta).
PICOS = [(6, 9), (17, 20)]
LOOP_STEP_MIN = 5          # o loop da stack chama a sonda a cada 5 min
GOOGLE_CADENCIA_MIN = 30   # Google só no pico e neste ritmo (mantém < 5k/mês)

# Teto diário POR FONTE — folga sob o grátis (ver campo/sonda-tempos-multifonte.md):
#   TomTom 2500/dia · HERE ~1000/dia (30k/mês) · Waze ilimitado (anti-bloqueio) · Google ~166/dia (5k/mês Pro)
CAPS = {"tomtom": 2000, "here": 950, "waze": 900, "google": 150}

CAMPOS_SAIDA = ["timestamp", "rota_id", "ponto_id", "fonte",
                "duracao_s", "duracao_livre_s", "distancia_m", "status"]


# ---------------------------------------------------------------- infraestrutura
def carregar_rotas(path: Path = ROTAS) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as f:
        rotas = [r for r in csv.DictReader(f) if r.get("ativa", "").strip() == "1"]
    if not rotas:
        raise SystemExit(f"nenhuma rota ativa em {path}")
    return rotas


def em_pico(agora: dt.datetime) -> bool:
    return any(ini <= agora.hour < fim for ini, fim in PICOS)


def cadencia_min(agora: dt.datetime) -> int:
    """Minutos entre coletas por período: pico denso, madrugada esparso."""
    if em_pico(agora):
        return 10
    if (9 <= agora.hour < 11) or (14 <= agora.hour < 16):
        return 20
    if 0 <= agora.hour < 6:
        return 60
    return 30


def deve_coletar(agora: dt.datetime, force: bool) -> bool:
    return force or (agora.minute % cadencia_min(agora) < LOOP_STEP_MIN)


def google_agora(agora: dt.datetime, force: bool) -> bool:
    """Google só no pico e a cada GOOGLE_CADENCIA_MIN (SKU Pro tem cota curta)."""
    return force or (em_pico(agora) and agora.minute % GOOGLE_CADENCIA_MIN < LOOP_STEP_MIN)


def ler_ledger(path: Path = LEDGER) -> dict[str, int]:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def pode_gastar(ledger: dict[str, int], fonte: str, agora: dt.datetime,
                n: int, max_dia: int) -> bool:
    dia = f"{fonte}:{agora:%Y-%m-%d}"
    return ledger.get(dia, 0) + n <= max_dia


def registrar_gasto(ledger: dict[str, int], fonte: str, agora: dt.datetime,
                    n: int, path: Path = LEDGER) -> None:
    for chave in (f"{fonte}:{agora:%Y-%m-%d}", f"{fonte}:{agora:%Y-%m}"):
        ledger[chave] = ledger.get(chave, 0) + n
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")


def gravar_linhas(linhas: list[dict], path: Path = OUT_CSV) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    novo = not path.exists()
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS_SAIDA)
        if novo:
            w.writeheader()
        w.writerows(linhas)


# ------------------------------------------------------------------------ fontes
# Cada fonte retorna (duracao_s, duracao_livre_s, distancia_m, status).
# duracao_livre_s/distancia_m podem vir vazios ("") quando a fonte não os informa.

def via_tomtom(rota: dict[str, str], key: str) -> tuple:
    o = f"{rota['origem_lat']},{rota['origem_lon']}"
    d = f"{rota['destino_lat']},{rota['destino_lon']}"
    params = urllib.parse.urlencode({
        "key": key, "traffic": "true", "computeTravelTimeFor": "all",
        "routeType": "fastest", "travelMode": "car"})
    url = f"https://api.tomtom.com/routing/1/calculateRoute/{o}:{d}/json?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "alpha-viario/1.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        s = json.load(resp)["routes"][0]["summary"]
    live = s["travelTimeInSeconds"]
    free = s.get("noTrafficTravelTimeInSeconds", live)
    return live, free, s.get("lengthInMeters", ""), "OK"


def via_here(rota: dict[str, str], key: str) -> tuple:
    # HERE v8 recusa 'now'; para trânsito ao vivo, passa o horário local ISO 8601.
    dep = dt.datetime.now().astimezone().replace(microsecond=0).isoformat()
    params = urllib.parse.urlencode({
        "transportMode": "car", "return": "summary", "departureTime": dep,
        "origin": f"{rota['origem_lat']},{rota['origem_lon']}",
        "destination": f"{rota['destino_lat']},{rota['destino_lon']}", "apikey": key})
    url = f"https://router.hereapi.com/v8/routes?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "alpha-viario/1.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        secoes = json.load(resp)["routes"][0]["sections"]
    dur = sum(s["summary"]["duration"] for s in secoes)
    base = sum(s["summary"].get("baseDuration", s["summary"]["duration"]) for s in secoes)
    dist = sum(s["summary"].get("length", 0) for s in secoes)
    return dur, base, dist or "", "OK"


def via_waze(rota: dict[str, str]) -> tuple:
    import WazeRouteCalculator  # dependência opcional (não oficial)
    o = f"{rota['origem_lat']},{rota['origem_lon']}"
    d = f"{rota['destino_lat']},{rota['destino_lon']}"
    calc = WazeRouteCalculator.WazeRouteCalculator(o, d, WAZE_REGION)
    minutos, km = calc.calc_route_info()
    return round(minutos * 60), "", round(km * 1000), "OK"


def via_google(rota: dict[str, str], key: str) -> tuple:
    body = json.dumps({
        "origin": {"location": {"latLng": {
            "latitude": float(rota["origem_lat"]),
            "longitude": float(rota["origem_lon"])}}},
        "destination": {"location": {"latLng": {
            "latitude": float(rota["destino_lat"]),
            "longitude": float(rota["destino_lon"])}}},
        "travelMode": "DRIVE", "routingPreference": "TRAFFIC_AWARE"}).encode("utf-8")
    req = urllib.request.Request(
        "https://routes.googleapis.com/directions/v2:computeRoutes",
        data=body, method="POST",
        headers={"Content-Type": "application/json", "X-Goog-Api-Key": key,
                 "X-Goog-FieldMask": "routes.duration,routes.staticDuration,routes.distanceMeters"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        r = (json.load(resp).get("routes") or [{}])[0]
    dur = int(r.get("duration", "0s").rstrip("s")) or ""
    free = int(r.get("staticDuration", "0s").rstrip("s")) or ""
    return dur, free, r.get("distanceMeters", ""), "OK" if dur else "SEM_ROTA"


# --------------------------------------------------------------------------- main
def fontes_ativas() -> list[tuple]:
    """(nome, callable(rota), disponivel, motivo). Google sempre listado; o gate de
    pico/cadência é aplicado no main (SKU Pro tem cota curta)."""
    tomtom_key = os.environ.get("TOMTOM_API_KEY", "")
    here_key = os.environ.get("HERE_API_KEY", "")
    google_key = os.environ.get("GOOGLE_MAPS_API_KEY", "")
    try:
        import WazeRouteCalculator  # noqa: F401
        waze_ok, waze_motivo = True, ""
    except ImportError:
        waze_ok, waze_motivo = False, "SEM_LIB (pip install WazeRouteCalculator)"

    return [
        ("tomtom", lambda r: via_tomtom(r, tomtom_key), bool(tomtom_key), "SEM_CHAVE"),
        ("here", lambda r: via_here(r, here_key), bool(here_key), "SEM_CHAVE"),
        ("waze", via_waze, waze_ok, waze_motivo),
        ("google", lambda r: via_google(r, google_key), bool(google_key), "SEM_CHAVE"),
    ]


def _selftest() -> int:
    """Projeta o volume de um dia e confere contra os tetos (guarda anti-cobrança)."""
    try:
        n = len(carregar_rotas())
    except SystemExit:
        n = 12
    vol = {"tomtom": 0, "here": 0, "waze": 0, "google": 0}
    for h in range(24):
        for m in range(0, 60, LOOP_STEP_MIN):
            agora = dt.datetime(2026, 1, 1, h, m)
            if deve_coletar(agora, False):
                for f in ("tomtom", "here", "waze"):
                    vol[f] += n
            if google_agora(agora, False):
                vol["google"] += n
    ok = True
    for f, cap in CAPS.items():
        estoura = vol[f] > cap
        ok = ok and not estoura
        print(f"  {f:7} {vol[f]:5}/dia  teto {cap:5}  {'ESTOURA' if estoura else 'OK'}")
    mes_g = vol["google"] * 31
    print(f"  google ~{mes_g}/mês (grátis 5000 Pro)  {'ESTOURA' if mes_g > 5000 else 'OK'}")
    assert ok and mes_g <= 5000, "projeção estoura teto — ajuste CAPS/cadência"
    assert cadencia_min(dt.datetime(2026, 1, 1, 8, 0)) == 10       # pico denso
    assert cadencia_min(dt.datetime(2026, 1, 1, 3, 0)) == 60       # madrugada esparso
    assert not google_agora(dt.datetime(2026, 1, 1, 3, 0), False)  # google não madrugada
    assert google_agora(dt.datetime(2026, 1, 1, 8, 0), False)      # google no pico :00
    print("selftest OK")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true",
                        help="não chama nenhuma API; mostra o que faria")
    parser.add_argument("--force", action="store_true",
                        help="força coleta agora (ignora cadência; respeita os tetos)")
    parser.add_argument("--selftest", action="store_true",
                        help="valida cadência/tetos/volume projetado e sai")
    args = parser.parse_args(argv)

    if args.selftest:
        return _selftest()

    agora = dt.datetime.now()
    rotas = carregar_rotas()
    fontes = fontes_ativas()

    if not deve_coletar(agora, args.force):
        print(f"Não é hora ({agora:%H:%M}; cadência {cadencia_min(agora)}min) — nada a fazer.")
        return 0

    ledger = ler_ledger()
    ts = agora.strftime("%Y-%m-%dT%H:%M:%S")
    linhas, erros = [], 0

    for nome, chamar, disponivel, motivo in fontes:
        if not disponivel:
            print(f"[{nome}] indisponível: {motivo} — pulando.", file=sys.stderr)
            continue
        if nome == "google" and not google_agora(agora, args.force):
            print("[google] fora do pico/cadência — pulando.", file=sys.stderr)
            continue
        cap = CAPS.get(nome, 500)
        if not pode_gastar(ledger, nome, agora, len(rotas), cap):
            print(f"[{nome}] teto diário atingido ({cap}) — pulando.", file=sys.stderr)
            continue
        if args.dry_run:
            print(f"[seco] {nome}: {len(rotas)} rotas seriam consultadas.")
            continue

        # Registra o gasto ANTES das chamadas: a tentativa conta contra o teto,
        # mesmo que falhe — falha de rede não pode virar estouro de orçamento.
        registrar_gasto(ledger, nome, agora, len(rotas))
        for r in rotas:
            linha = {"timestamp": ts, "rota_id": r["rota_id"], "ponto_id": r["ponto_id"],
                     "fonte": nome, "duracao_s": "", "duracao_livre_s": "",
                     "distancia_m": "", "status": "OK"}
            try:
                dur, free, dist, status = chamar(r)
                linha.update(duracao_s=dur, duracao_livre_s=free,
                             distancia_m=dist, status=status)
            except urllib.error.HTTPError as e:
                linha["status"] = f"HTTP_{e.code}"; erros += 1
            except Exception as e:  # noqa: BLE001  (rede/lib não oficial)
                linha["status"] = f"ERRO_{type(e).__name__}"; erros += 1
            linhas.append(linha)
            print(f"[{nome}] {r['rota_id']} ({r['ponto_id']}): "
                  f"{linha['duracao_s'] or '-'}s [{linha['status']}]")
            if nome == "waze":
                time.sleep(WAZE_DELAY_S)

    if args.dry_run:
        return 0
    if not linhas:
        print("Nenhuma fonte disponível — nada coletado.", file=sys.stderr)
        return 1
    gravar_linhas(linhas)
    print(f"{len(linhas)} medições ({erros} erro(s)) -> {OUT_CSV.relative_to(ROOT)}")
    return 0 if erros == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
