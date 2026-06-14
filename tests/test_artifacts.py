"""Os artefatos versionados precisam corresponder ao que seus geradores produzem.

Impede que GeoJSON, pacote-reuniao.md e as listas dos questionários fiquem
defasados em relação ao cadastro/fontes (deriva silenciosa).
"""
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import pontos  # noqa: E402
import build_pacote  # noqa: E402


class TestGeoJSON(unittest.TestCase):
    def test_geojson_versionado_bate_com_cadastro(self):
        rows = pontos.load()
        esperado = json.dumps(pontos.to_geojson(rows), ensure_ascii=False, indent=2) + "\n"
        atual = (ROOT / "dados/tratados/pontos.geojson").read_text(encoding="utf-8")
        self.assertEqual(atual, esperado, "pontos.geojson desatualizado — rode 'make geojson'")


class TestPacote(unittest.TestCase):
    def test_pacote_md_versionado_bate_com_build(self):
        atual = (ROOT / "pacote-reuniao.md").read_text(encoding="utf-8")
        self.assertEqual(atual, build_pacote.build_markdown(),
                         "pacote-reuniao.md desatualizado — rode 'make pacote'")


class TestSync(unittest.TestCase):
    def test_regioes_marcadas_em_dia(self):
        rows = pontos.load()
        for relp, style in pontos.SYNC_TARGETS:
            text = (ROOT / relp).read_text(encoding="utf-8")
            novo, encontrado = pontos.inject(text, rows, style)
            self.assertTrue(encontrado, f"região '{style}' não encontrada em {relp}")
            self.assertEqual(novo, text, f"{relp} [{style}] desatualizado — rode 'scripts/pontos.py sync'")


if __name__ == "__main__":
    unittest.main()
