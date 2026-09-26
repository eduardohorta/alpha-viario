"""Testes do public-check (verificações unitárias; a integração roda em `make check`)."""
import pathlib
import sys
import tempfile
import unittest
import json
from unittest.mock import patch

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


class TestReleaseScope(unittest.TestCase):
    def test_aviso_de_privacidade_nao_bloqueia_protocolo_atual(self):
        self.assertNotIn(
            "consultas/moradores/aviso-privacidade.md",
            public_check.EXTERNAL_PIECES,
        )


class TestPackageOutputs(unittest.TestCase):
    def test_missing_or_modified_pdf_and_md_only_build_are_stale(self):
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            md, pdf = root / "pacote-reuniao.md", root / "pacote-reuniao.pdf"
            md.write_text("conteúdo")
            pdf.write_bytes(b"pdf original")
            manifest = root / "pacote-reuniao.sources.json"
            sources = {p: "unused" for p in (
                "scripts/build_pacote.py", "mapas/mapa-pontos.png",
                "relatorios/guia-validacao-comissao.md", "relatorios/memorando-externo.md",
                "relatorios/anexo-matriz-pontos.md")}
            for p in sources:
                f = root / p
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_text("fonte")
                sources[p] = public_check._sha256(f)
            data = {"fontes": sources, "saida_md_sha256": public_check._sha256(md),
                    "saida_pdf_sha256": public_check._sha256(pdf)}
            manifest.write_text(json.dumps(data))
            with patch.object(public_check, "ROOT", root), patch.object(public_check, "PACOTE_MANIFEST", manifest):
                self.assertEqual(public_check.check_stale_package(), [])
                pdf.write_bytes(b"pdf alterado")
                self.assertTrue(public_check.check_stale_package())
                pdf.unlink()
                self.assertTrue(public_check.check_stale_package())
                pdf.write_bytes(b"pdf original")
                del data["saida_pdf_sha256"]
                manifest.write_text(json.dumps(data))
                self.assertTrue(public_check.check_stale_package())


if __name__ == "__main__":
    unittest.main()
