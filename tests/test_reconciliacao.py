"""Casos adversos: presença no bruto não equivale a presença no recorte."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import reconciliar_sinistros as rec


class TestReconciliacao(unittest.TestCase):
    def row(self, date="20200101", lat="-30.11831", lon="-51.20319"):
        return {"data": date, "latitude": lat, "longitude": lon}

    def test_absence_is_not_missing_geocode(self):
        self.assertEqual(rec.classify([], "P1", {}), "id_ausente_no_bruto")
        self.assertEqual(rec.classify([self.row(lat="0", lon="0")], "P1", {}), "coordenada_invalida")

    def test_window_precedes_spatial_classification(self):
        self.assertEqual(rec.classify([self.row(date="20191231")], "P1", {}), "data_fora_da_janela")
        self.assertTrue(rec.in_window(self.row(date="2025-08-31 00:00:00")))
        self.assertFalse(rec.in_window(self.row(date="2025-09-01 00:00:00")))

    def test_changed_location_explains_spatial_exclusion(self):
        self.assertEqual(rec.classify([self.row(lat="-30.2")], "P1", {}), "coordenada_fora_do_limiar")

    def test_unexplained_missing_association_fails(self):
        # Inclui caso com mais de uma contraparte: uma está dentro do recorte.
        with self.assertRaises(ValueError):
            rec.classify([self.row(lat="-30.2"), self.row()], "P1", {})


if __name__ == "__main__":
    unittest.main()
