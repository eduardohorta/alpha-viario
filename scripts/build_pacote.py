#!/usr/bin/env python3
"""Gera pacote-reuniao.md (e .pdf) a partir dos documentos-fonte.

Sem conteúdo copiado à mão: o pacote é a concatenação dos documentos-fonte, com
os links relativos reescritos para resolver a partir da raiz do repositório
(onde o pacote vive) e quebras de página entre as seções. Grava também o
manifesto de fontes (pacote-reuniao.sources.json) usado pelo public-check para
detectar quando o pacote fica defasado em relação às fontes.

Uso:
  python3 scripts/build_pacote.py            # gera .md, manifesto e .pdf (se houver pandoc)
  python3 scripts/build_pacote.py --no-pdf   # só .md e manifesto
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_MD = ROOT / "pacote-reuniao.md"
OUT_PDF = ROOT / "pacote-reuniao.pdf"
MANIFEST = ROOT / "pacote-reuniao.sources.json"

# Documentos-fonte, na ordem em que aparecem no pacote.
SOURCES = [
    "relatorios/guia-validacao-comissao.md",
    "relatorios/memorando-externo.md",
    "relatorios/anexo-matriz-pontos.md",
    "campo/plano-coleta-campo.md",
]

# Mantido fixo (não derivado da data de hoje) para que o build seja determinístico
# e os testes de reprodução byte a byte funcionem. A comissão atualiza quando quiser.
DATE = "Junho de 2026"

FRONTMATTER = f"""---
title: "Projeto Viário — Vila Nova / Zona Sul"
subtitle: "Pacote de reunião — Comissão de Mobilidade"
author: "Comissão de Mobilidade — Moradores do Alphaville Porto Alegre"
date: "{DATE}"
lang: pt-BR
geometry: margin=2.2cm
fontsize: 11pt
---"""

NEWPAGE = "```{=latex}\n\\newpage\n```"

LINK_RE = re.compile(r"(\]\()([^)]+)(\))")


def rewrite_links(text: str, src_relpath: str) -> str:
    """Reescreve links relativos de `src_relpath` para serem relativos à raiz."""
    src_dir = (ROOT / src_relpath).parent

    def repl(m: re.Match) -> str:
        url = m.group(2)
        title = ""
        if " " in url:  # [txt](url "título")
            url, title = url.split(" ", 1)
            title = " " + title
        if re.match(r"^[a-z][a-z0-9+.-]*://", url) or url.startswith(("#", "mailto:", "tel:", "//")):
            return m.group(0)
        anchor = ""
        if "#" in url:
            url, frag = url.split("#", 1)
            anchor = "#" + frag
        if not url:
            return m.group(0)
        target = (src_dir / url).resolve()
        try:
            relpath = target.relative_to(ROOT).as_posix()
        except ValueError:
            return m.group(0)  # aponta para fora do repo; deixa como está
        return f"{m.group(1)}{relpath}{anchor}{title}{m.group(3)}"

    return LINK_RE.sub(repl, text)


def build_markdown() -> str:
    provenance = (
        "<!-- GERADO por scripts/build_pacote.py — NÃO editar à mão. "
        "Fontes: " + ", ".join(SOURCES) + " -->"
    )
    parts = [FRONTMATTER, "", provenance]
    for src in SOURCES:
        content = rewrite_links((ROOT / src).read_text(encoding="utf-8").rstrip(), src)
        parts += ["", NEWPAGE, "", content]
    return "\n".join(parts) + "\n"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_manifest() -> None:
    fontes = {src: _sha256(ROOT / src) for src in SOURCES}
    fontes["scripts/build_pacote.py"] = _sha256(Path(__file__).resolve())
    manifest = {
        "gerado_por": "scripts/build_pacote.py",
        "comando": "python3 scripts/build_pacote.py",
        "saida": ["pacote-reuniao.md", "pacote-reuniao.pdf"],
        "fontes": fontes,
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_pdf() -> bool:
    if not shutil.which("pandoc"):
        print("pandoc não encontrado — pulei o PDF (o .md foi gerado).", file=sys.stderr)
        return False
    cmd = ["pandoc", str(OUT_MD), "-o", str(OUT_PDF), "--pdf-engine=xelatex"]
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        print("Falha ao gerar PDF:\n" + result.stderr, file=sys.stderr)
        return False
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-pdf", action="store_true", help="não gerar o PDF")
    args = parser.parse_args(argv)

    missing = [s for s in SOURCES if not (ROOT / s).exists()]
    if missing:
        print(f"Fontes ausentes: {missing}", file=sys.stderr)
        return 1

    OUT_MD.write_text(build_markdown(), encoding="utf-8")
    write_manifest()
    print(f"Gerado {OUT_MD.name} a partir de {len(SOURCES)} fontes + manifesto.")

    if not args.no_pdf:
        if build_pdf():
            print(f"Gerado {OUT_PDF.name}.")
        else:
            print("PDF não gerado (veja acima).", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
