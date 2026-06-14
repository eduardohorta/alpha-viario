"""Testes do cadastro canônico de pontos."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import pontos  # noqa: E402


class TestRegistry(unittest.TestCase):
    def setUp(self):
        self.rows = pontos.load()

    def test_registry_valid(self):
        self.assertEqual(pontos.validate(self.rows), [])

    def test_ids_sequential(self):
        ids = sorted(int(r["id"][1:]) for r in self.rows)
        self.assertEqual(ids, list(range(1, len(ids) + 1)))

    def test_unique_ids(self):
        ids = [r["id"] for r in self.rows]
        self.assertEqual(len(ids), len(set(ids)))

    def test_geojson_shape(self):
        gj = pontos.to_geojson(self.rows)
        self.assertEqual(gj["type"], "FeatureCollection")
        self.assertEqual(len(gj["features"]), len(self.rows))
        # GeoJSON exige [lon, lat].
        lon, lat = gj["features"][0]["geometry"]["coordinates"]
        self.assertTrue(-52 < lon < -50)
        self.assertTrue(-31 < lat < -29)

    def test_lista_inclui_p9_preliminar(self):
        out = pontos.render_list(self.rows, "questionario-curto")
        self.assertIn("P9", out)
        self.assertIn("(preliminar)", out)

    def test_validate_detecta_problema(self):
        bad = [dict(self.rows[0]), dict(self.rows[0])]  # ID duplicado
        self.assertTrue(any("duplicado" in e for e in pontos.validate(bad)))

    def test_inject_substitui_regiao(self):
        text = f"antes\n{pontos.BEGIN.format(style='readme')}\nx\n{pontos.END.format(style='readme')}\ndepois\n"
        new, found = pontos.inject(text, self.rows, "readme")
        self.assertTrue(found)
        self.assertIn("**P1**", new)
        self.assertTrue(new.startswith("antes"))
        self.assertTrue(new.rstrip().endswith("depois"))


if __name__ == "__main__":
    unittest.main()
