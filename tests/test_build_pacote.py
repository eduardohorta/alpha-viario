"""Testes do build do pacote de reunião."""
import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_pacote  # noqa: E402

LINK_RE = re.compile(r"\]\(([^)]+)\)")


class TestBuild(unittest.TestCase):
    def test_deterministico(self):
        self.assertEqual(build_pacote.build_markdown(), build_pacote.build_markdown())

    def test_links_reescritos(self):
        # Link relativo dentro de relatorios/ vira relativo à raiz.
        out = build_pacote.rewrite_links("[m](memorando-externo.md)", "relatorios/guia-validacao-comissao.md")
        self.assertEqual(out, "[m](relatorios/memorando-externo.md)")
        out = build_pacote.rewrite_links("[p](../propostas/x.md)", "relatorios/guia-validacao-comissao.md")
        self.assertEqual(out, "[p](propostas/x.md)")

    def test_links_externos_e_ancoras_preservados(self):
        self.assertEqual(
            build_pacote.rewrite_links("[a](https://x.org)", "relatorios/a.md"),
            "[a](https://x.org)",
        )
        out = build_pacote.rewrite_links("[a](memorando-externo.md#sec)", "relatorios/a.md")
        self.assertEqual(out, "[a](relatorios/memorando-externo.md#sec)")

    def test_todos_os_links_resolvem(self):
        md = build_pacote.build_markdown()
        for link in LINK_RE.findall(md):
            url = link.split("#", 1)[0].split(" ", 1)[0]
            if url.startswith(("http://", "https://", "#", "mailto:")):
                continue
            self.assertTrue((ROOT / url).exists(), f"link quebrado no pacote: {url}")


if __name__ == "__main__":
    unittest.main()
