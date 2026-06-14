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


P4_OUTPUTS = [
    "acidentes_p4_marcos_intersecoes.csv",
    "acidentes_p4_segmentos.csv",
    "acidentes_p4_registros_segmentados.csv",
    "acidentes_p4_hotspots_250m.csv",
    "acidentes_p4_segmentacao_metadata.json",
]


def _compare(out_dir, names, case):
    for name in names:
        got = (pathlib.Path(out_dir) / name).read_bytes()
        want = (TRAT / name).read_bytes()
        case.assertEqual(got, want, f"{name} divergiu da versão versionada")


@unittest.skipUnless(RAW.exists(), "bruto cat_acidentes.csv ausente — rode 'make fetch-data'")
class TestReproducaoSinistros(unittest.TestCase):
    """Reprodução do primeiro script (precisa do bruto de 15 MB)."""

    def test_outputs_identicos(self):
        import processar_sinistros_distancia as proc

        orig = proc.OUT_DIR
        with tempfile.TemporaryDirectory() as d:
            proc.OUT_DIR = pathlib.Path(d)
            try:
                proc.main()
            finally:
                proc.OUT_DIR = orig
            _compare(d, OUTPUTS, self)


class TestReproducaoP4(unittest.TestCase):
    """Reprodução da segmentação do P4 — usa apenas insumos versionados (sem bruto)."""

    def test_outputs_identicos(self):
        import segmentar_p4_monteggia as seg

        orig = seg.OUT_DIR
        with tempfile.TemporaryDirectory() as d:
            seg.OUT_DIR = pathlib.Path(d)
            try:
                seg.main()
            finally:
                seg.OUT_DIR = orig
            _compare(d, P4_OUTPUTS, self)


if __name__ == "__main__":
    unittest.main()
