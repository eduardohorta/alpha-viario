"""Paridade entre o cadastro canônico e as definições embutidas nos scripts.

Enquanto processar_sinistros_distancia.py mantém suas próprias coordenadas e
nomes de via para P1-P8, estes testes impedem divergência silenciosa em relação
a dados/pontos.csv (a fonte única).
"""
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import pontos  # noqa: E402
import processar_sinistros_distancia as proc  # noqa: E402


class TestParidade(unittest.TestCase):
    def setUp(self):
        self.reg = {r["id"]: r for r in pontos.load()}

    def test_pontos_do_script_existem_no_cadastro(self):
        for pid in proc.POINTS:
            self.assertIn(pid, self.reg, f"{pid} está no script mas não no cadastro")

    def test_coordenadas_batem(self):
        for pid, spec in proc.POINTS.items():
            if spec["type"] != "point":
                continue
            self.assertAlmostEqual(float(self.reg[pid]["lat"]), float(spec["lat"]), places=6, msg=f"{pid} lat")
            self.assertAlmostEqual(float(self.reg[pid]["lon"]), float(spec["lon"]), places=6, msg=f"{pid} lon")

    def test_tipo_geometria_bate(self):
        mapa = {"point": "point", "polyline": "polyline"}
        for pid, spec in proc.POINTS.items():
            self.assertEqual(self.reg[pid]["geometria"], mapa[spec["type"]], pid)

    def test_nomes_de_via_dos_corredores_batem(self):
        # As vias OSM usadas no mapa (CORRIDOR_WAYS) e na associação de sinistros
        # (POINTS[...]["road_names"]) precisam ser idênticas.
        for pid, names in pontos.CORRIDOR_WAYS.items():
            self.assertEqual(proc.POINTS[pid]["road_names"], names, f"{pid} road_names")


if __name__ == "__main__":
    unittest.main()
