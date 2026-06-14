"""Testes do public-check (verificações unitárias; a integração roda em `make check`)."""
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import public_check  # noqa: E402
import pontos  # noqa: E402


class TestCleanLink(unittest.TestCase):
    def test_externos_e_ancoras(self):
        for raw in ("https://x.org", "http://x", "#sec", "mailto:a@b", "//cdn"):
            self.assertIsNone(public_check._clean_link(raw))

    def test_normaliza(self):
        self.assertEqual(public_check._clean_link('foo.md "t"'), "foo.md")
        self.assertEqual(public_check._clean_link("foo.md#x"), "foo.md")


class TestLinks(unittest.TestCase):
    def test_detecta_link_quebrado(self):
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / "a.md"
            f.write_text("[x](nao-existe.md)\n", encoding="utf-8")
            issues = public_check.check_links([f])
            self.assertTrue(any(i.check == "broken-link" for i in issues))

    def test_link_valido_nao_acusa(self):
        with tempfile.TemporaryDirectory() as d:
            (pathlib.Path(d) / "alvo.md").write_text("ok", encoding="utf-8")
            f = pathlib.Path(d) / "a.md"
            f.write_text("[x](alvo.md)\n", encoding="utf-8")
            self.assertEqual(public_check.check_links([f]), [])


class TestRegistry(unittest.TestCase):
    def test_registro_real_valido(self):
        self.assertEqual(public_check.check_registry(pontos.load()), [])

    def test_point_set_detecta_omissao(self):
        # Documento sintético sem P9 deve ser cobrado se estiver na allowlist.
        # Aqui validamos a lógica via public_ids: P9 está no conjunto esperado.
        self.assertIn("P9", pontos.public_ids(pontos.load()))


if __name__ == "__main__":
    unittest.main()
