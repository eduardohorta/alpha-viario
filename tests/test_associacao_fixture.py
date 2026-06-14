"""Testa o algoritmo de associação por distância numa fixture pequena.

Roda em cada push no CI (não precisa do bruto de 15 MB): aponta o script para
uma amostra controlada e confere as associações esperadas, exercitando os três
caminhos — acerto por coordenada, registro sem coordenada por logradouro, e
registro distante/ inválido sem associação.
"""
import csv
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests/fixtures/cat_acidentes_sample.csv"
sys.path.insert(0, str(ROOT / "scripts"))
import processar_sinistros_distancia as proc  # noqa: E402


def _rows(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


class TestAssociacaoFixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = pathlib.Path(self.tmp.name)
        orig_csv, orig_out = proc.CSV_PATH, proc.OUT_DIR
        proc.CSV_PATH, proc.OUT_DIR = FIXTURE, d
        try:
            proc.main()
        finally:
            proc.CSV_PATH, proc.OUT_DIR = orig_csv, orig_out
        self.d = d
        self.resumo = {r["ponto"]: r for r in _rows(d / "acidentes_resumo_distancia_pontos.csv")}
        self.assoc = _rows(d / "acidentes_associados_distancia.csv")
        self.sem_coord = _rows(d / "acidentes_sem_coordenada_revisao.csv")
        self.meta = json.loads((d / "acidentes_distancia_metadata.json").read_text(encoding="utf-8"))

    def tearDown(self):
        self.tmp.cleanup()

    def test_totais(self):
        t = self.meta["totais_csv"]
        self.assertEqual(t["rows"], 5)
        self.assertEqual(t["valid_coord"], 3)
        self.assertEqual(t["invalid_coord"], 2)
        self.assertEqual(t["relevant_no_coord"], 1)

    def test_acertos_por_coordenada(self):
        # Registro 1 cai exatamente em P1; registro 2 em P8.
        self.assertEqual(int(self.resumo["P1"]["ocorrencias_principal"]), 1)
        self.assertEqual(int(self.resumo["P8"]["ocorrencias_principal"]), 1)
        ids = {r["idacidente"] for r in self.assoc}
        self.assertEqual(ids, {"1", "2"})

    def test_pontos_sem_acerto_ficam_zerados(self):
        for pid in ("P2", "P3", "P4", "P5", "P6", "P7"):
            self.assertEqual(int(self.resumo[pid]["ocorrencias_principal"]), 0, pid)

    def test_registro_sem_coordenada_por_logradouro(self):
        # Registro 3 (Vicente Monteggia, sem coord) entra na revisão como P4.
        self.assertEqual(len(self.sem_coord), 1)
        self.assertEqual(self.sem_coord[0]["ponto"], "P4")
        self.assertEqual(self.sem_coord[0]["idacidente"], "3")

    def test_registro_distante_nao_associa(self):
        # Registros 4 (longe) e 5 (coord inválida) não entram em nenhuma associação.
        ids = {r["idacidente"] for r in self.assoc}
        self.assertNotIn("4", ids)
        self.assertNotIn("5", ids)


if __name__ == "__main__":
    unittest.main()
