"""Reprodução byte a byte dos derivados (pulado se o bruto não estiver presente)."""
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
TRAT = ROOT / "dados/tratados"
RAW = ROOT / "dados/brutos/cat_acidentes.csv"
sys.path.insert(0, str(ROOT / "scripts"))

OUTPUTS = [
    "acidentes_resumo_distancia_pontos.csv",
    "acidentes_associados_distancia.csv",
    "acidentes_revisao_manual_proximos.csv",
    "acidentes_sem_coordenada_revisao.csv",
    "acidentes_distancia_metadata.json",
]


@unittest.skipUnless(RAW.exists(), "bruto cat_acidentes.csv ausente — rode 'make fetch-data'")
class TestReproducao(unittest.TestCase):
    def test_outputs_identicos(self):
        import processar_sinistros_distancia as proc

        orig = proc.OUT_DIR
        with tempfile.TemporaryDirectory() as d:
            proc.OUT_DIR = pathlib.Path(d)
            try:
                proc.main()
            finally:
                proc.OUT_DIR = orig
            for name in OUTPUTS:
                got = (pathlib.Path(d) / name).read_bytes()
                want = (TRAT / name).read_bytes()
                self.assertEqual(got, want, f"{name} divergiu da versão versionada")


if __name__ == "__main__":
    unittest.main()
