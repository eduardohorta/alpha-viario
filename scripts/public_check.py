#!/usr/bin/env python3
"""public-check — porteiro de publicação do repositório.

Verifica o que pode quebrar ou vazar quando o repositório é clonado publicamente:

  1. links relativos quebrados (alvo inexistente no disco);
  2. links apontando para áreas privadas (interno/, revisoes/) — gitignored,
     portanto quebram no clone público;
  3. placeholders ([nome], [link], ____) nas peças externas;
  4. pacote/PDF desatualizado em relação às fontes (via manifesto do build);
  5. termos sensíveis fora da área interna (lista privada opcional);
  6. inconsistência entre os pontos enumerados nos documentos e o cadastro
     canônico (ex.: P1-P8 onde deveria constar P1-P9);
  7. cadastro de pontos (dados/pontos.csv) inválido.

Só percorre arquivos versionados (`git ls-files`), que já excluem interno/ e
revisoes/. ERRO => código de saída 1. AVISO não falha, salvo com --strict.

Uso: python3 scripts/public_check.py [--strict]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import pontos  # mesmo diretório scripts/

ROOT = Path(__file__).resolve().parents[1]

# Peças do protocolo atual (EPTC ou circulação) que não podem sair com placeholder.
# O aviso de privacidade do questionário permanece no repositório como instrumento em
# espera; só volta a esta lista se a comissão decidir circular o formulário.
EXTERNAL_PIECES = [
    "relatorios/memorando-externo.md",
    "relatorios/oficio-eptc-rascunho.md",
    "relatorios/anexo-matriz-pontos.md",
    "pacote-reuniao.md",
]

PRIVATE_DIRS = ("interno", "revisoes")

# Manifesto de fontes do pacote (escrito pelo build do pacote — Fase 2).
PACOTE = "pacote-reuniao.md"
PACOTE_MANIFEST = ROOT / "pacote-reuniao.sources.json"

# Lista privada de termos sensíveis (nomes reais etc.), fora do versionamento.
SENSITIVE_LIST = ROOT / "interno/termos-sensiveis.txt"

PLACEHOLDER_PATTERNS = [
    re.compile(r"\[nome\b", re.IGNORECASE),
    re.compile(r"\[link\]", re.IGNORECASE),
    re.compile(r"\[campos? ", re.IGNORECASE),
    re.compile(r"\[.*?a preencher.*?\]", re.IGNORECASE),
    re.compile(r"\[a (definir|confirmar|preencher)", re.IGNORECASE),
    re.compile(r"_{4,}"),
    re.compile(r"\bTODO\b|\bTBD\b|XXX"),
]

LINK_RE = re.compile(r"\[(?:[^\]]*)\]\(([^)]+)\)")
PID_RE = re.compile(r"\bP(\d+)\b")

# Documentos cuja lista de pontos é voltada ao leitor/respondente e DEVE espelhar
# o cadastro canônico. (Arquivos de dados de sinistros legitimamente só têm P1-P8
# enquanto P9 não foi georreferenciado; matrizes temáticas cobrem subconjuntos de
# propósito — por isso a verificação é por allowlist, não heurística.)
ENUMERATION_DOCS = [
    "README.md",
    "consultas/moradores/questionario-curto.md",
    "consultas/moradores/questionario-base.md",
    "campo/observacoes/modelo-observacao-campo.csv",
    "propostas/problemas-priorizados.md",
]


@dataclass
class Issue:
    severity: str  # "ERRO" | "AVISO"
    check: str
    path: str
    line: int | None
    message: str


def tracked_files() -> list[Path]:
    out = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout
    return [ROOT / line for line in out.splitlines() if line.strip()]


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


def _clean_link(raw: str) -> str | None:
    """Normaliza o alvo de um link markdown; None se for externo/âncora."""
    url = raw.strip()
    # Remove título opcional: [txt](url "título")
    if " " in url:
        url = url.split(" ", 1)[0]
    url = url.split("#", 1)[0]  # remove âncora
    if not url:
        return None
    if re.match(r"^[a-z][a-z0-9+.-]*://", url) or url.startswith(("mailto:", "tel:", "//")):
        return None
    return url


def check_links(md_files: list[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for f in md_files:
        text = f.read_text(encoding="utf-8")
        for n, line in enumerate(text.splitlines(), 1):
            for m in LINK_RE.finditer(line):
                url = _clean_link(m.group(1))
                if url is None:
                    continue
                target = (f.parent / url).resolve()
                relpath = None
                try:
                    relpath = target.relative_to(ROOT).as_posix()
                except ValueError:
                    relpath = None
                if relpath is not None and relpath.split("/", 1)[0] in PRIVATE_DIRS:
                    issues.append(
                        Issue("ERRO", "private-ref", rel(f), n,
                              f"link para área privada (quebra no clone público): {url}")
                    )
                elif not target.exists():
                    issues.append(
                        Issue("ERRO", "broken-link", rel(f), n, f"link quebrado: {url}")
                    )
    return issues


def check_placeholders() -> list[Issue]:
    issues: list[Issue] = []
    for relp in EXTERNAL_PIECES:
        f = ROOT / relp
        if not f.exists():
            continue
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            for pat in PLACEHOLDER_PATTERNS:
                if pat.search(line):
                    issues.append(
                        Issue("AVISO", "placeholder", relp, n,
                              f"placeholder a preencher antes de publicar: {line.strip()[:80]}")
                    )
                    break
    return issues


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_stale_package() -> list[Issue]:
    pacote = ROOT / PACOTE
    if not pacote.exists():
        return []
    if not PACOTE_MANIFEST.exists():
        return [Issue("AVISO", "stale-package", PACOTE, None,
                      "pacote sem manifesto de fontes — não dá para garantir que está atualizado "
                      "(gere com o build do pacote).")]
    manifest = json.loads(PACOTE_MANIFEST.read_text(encoding="utf-8"))
    issues: list[Issue] = []
    for relp, recorded in manifest.get("fontes", {}).items():
        f = ROOT / relp
        if not f.exists():
            issues.append(Issue("AVISO", "stale-package", PACOTE, None,
                                f"fonte do pacote sumiu: {relp}"))
        elif _sha256(f) != recorded:
            issues.append(Issue("AVISO", "stale-package", PACOTE, None,
                                f"fonte mudou desde o último build do pacote: {relp}"))
    return issues


def check_sensitive(text_files: list[Path]) -> list[Issue]:
    if not SENSITIVE_LIST.exists():
        return [Issue("AVISO", "sensitive", "interno/termos-sensiveis.txt", None,
                      "lista de termos sensíveis ausente — verificação de vazamento de nomes "
                      "reais desativada (crie o arquivo, um termo por linha).")]
    terms = [t.strip() for t in SENSITIVE_LIST.read_text(encoding="utf-8").splitlines()
             if t.strip() and not t.startswith("#")]
    if not terms:
        return []
    issues: list[Issue] = []
    for f in text_files:
        for n, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for term in terms:
                if term.lower() in line.lower():
                    issues.append(Issue("ERRO", "sensitive", rel(f), n,
                                        f"termo sensível em arquivo público: '{term}'"))
    return issues


def check_point_set(registry: list[dict]) -> list[Issue]:
    expected = pontos.public_ids(registry)
    issues: list[Issue] = []
    for relp in ENUMERATION_DOCS:
        f = ROOT / relp
        if not f.exists():
            issues.append(Issue("AVISO", "point-set", relp, None,
                                "documento de enumeração ausente"))
            continue
        present = {f"P{m.group(1)}" for m in PID_RE.finditer(f.read_text(encoding="utf-8", errors="replace"))}
        present &= expected
        missing = sorted(expected - present, key=lambda i: int(i[1:]))
        if missing:
            issues.append(Issue("ERRO", "point-set", relp, None,
                                f"omite {', '.join(missing)} (presentes no cadastro canônico)"))
    return issues


def check_registry(registry: list[dict]) -> list[Issue]:
    return [Issue("ERRO", "registry", "dados/pontos.csv", None, e)
            for e in pontos.validate(registry)]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="trata AVISO como falha")
    args = parser.parse_args(argv)

    files = tracked_files()
    md_files = [f for f in files if f.suffix == ".md" and f.exists()]
    text_files = [f for f in files if f.suffix in (".md", ".csv") and f.exists()]
    registry = pontos.load()

    issues: list[Issue] = []
    issues += check_registry(registry)
    issues += check_links(md_files)
    issues += check_point_set(registry)
    issues += check_placeholders()
    issues += check_stale_package()
    issues += check_sensitive([f for f in text_files if f.name != "pontos.csv"])

    errors = [i for i in issues if i.severity == "ERRO"]
    warns = [i for i in issues if i.severity == "AVISO"]

    by_check: dict[str, list[Issue]] = {}
    for i in issues:
        by_check.setdefault(i.check, []).append(i)

    for check in sorted(by_check):
        group = by_check[check]
        print(f"\n## {check} ({len(group)})")
        for i in group:
            loc = f"{i.path}:{i.line}" if i.line else i.path
            print(f"  [{i.severity}] {loc} — {i.message}")

    print(f"\n{'='*60}")
    print(f"public-check: {len(errors)} ERRO, {len(warns)} AVISO")
    if errors:
        return 1
    if warns and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
