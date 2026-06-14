#!/usr/bin/env python3
"""Confere o SHA-256 dos insumos brutos contra dados/brutos/manifest.json.

Por padrão verifica apenas os insumos presentes no disco (o cat_acidentes.csv
não é versionado). Use --all para exigir que todos os insumos existam.

Uso: python3 scripts/verify_data.py [--all]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "dados/brutos/manifest.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="exigir todos os insumos presentes")
    args = parser.parse_args(argv)

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    ok = True
    for item in manifest["insumos"]:
        path = ROOT / item["arquivo"]
        if not path.exists():
            if args.all or item.get("versionado"):
                print(f"AUSENTE  {item['arquivo']}")
                ok = False
            else:
                print(f"pulado   {item['arquivo']} (não versionado; rode 'make fetch-data')")
            continue
        got = sha256(path)
        if got == item["sha256"]:
            print(f"OK       {item['arquivo']}")
        else:
            print(f"DIVERGE  {item['arquivo']}\n  esperado: {item['sha256']}\n  obtido:   {got}")
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
