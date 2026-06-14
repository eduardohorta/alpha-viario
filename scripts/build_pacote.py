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
import tempfile
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
        "fontes": fontes,
        # Determinístico (o .md não embute timestamp). O .pdf embute data de
        # criação, então não é byte-reprodutível e não tem hash registrado aqui.
        "saida_md_sha256": _sha256(OUT_MD),
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-pdf", action="store_true", help="não gerar o PDF")
    args = parser.parse_args(argv)

    missing = [s for s in SOURCES if not (ROOT / s).exists()]
    if missing:
        print(f"Fontes ausentes: {missing}", file=sys.stderr)
        return 1

    md_text = build_markdown()

    # Sem PDF (ou sem pandoc): atualiza Markdown + manifesto e sai.
    if args.no_pdf or not shutil.which("pandoc"):
        OUT_MD.write_text(md_text, encoding="utf-8")
        write_manifest()
        print(f"Gerado {OUT_MD.name} a partir de {len(SOURCES)} fontes + manifesto.")
        if not args.no_pdf:
            print("pandoc não encontrado — PDF NÃO atualizado.", file=sys.stderr)
        return 0

    # Com PDF: build transacional. Gera .md e .pdf em arquivos temporários e só
    # substitui os definitivos se o Pandoc/XeLaTeX tiver sucesso — assim nunca
    # fica um PDF obsoleto ao lado de um Markdown novo, nem um sucesso silencioso.
    with tempfile.NamedTemporaryFile("w", suffix=".md", dir=str(ROOT), delete=False, encoding="utf-8") as tf:
        tf.write(md_text)
        tmp_md = Path(tf.name)
    tmp_pdf = tmp_md.with_suffix(".pdf")
    try:
        result = subprocess.run(
            ["pandoc", str(tmp_md), "-o", str(tmp_pdf), "--pdf-engine=xelatex"],
            cwd=ROOT, capture_output=True, text=True,
        )
        if result.returncode != 0 or not tmp_pdf.exists() or tmp_pdf.stat().st_size == 0:
            print("Falha ao gerar PDF — nada foi alterado.\n" + result.stderr, file=sys.stderr)
            return 1
        tmp_md.replace(OUT_MD)
        tmp_pdf.replace(OUT_PDF)
    finally:
        for leftover in (tmp_md, tmp_pdf):
            if leftover.exists():
                leftover.unlink()

    write_manifest()
    print(f"Gerado {OUT_MD.name} + {OUT_PDF.name} a partir de {len(SOURCES)} fontes + manifesto.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
