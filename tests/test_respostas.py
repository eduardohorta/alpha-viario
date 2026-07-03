"""Testes da tabulação de respostas do questionário."""
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import pontos  # noqa: E402
import processar_respostas as pr  # noqa: E402

FIXTURE = ROOT / "tests/fixtures/respostas_sample.csv"


class TestTabulacao(unittest.TestCase):
    def setUp(self):
        self.ids = pontos.public_ids(pontos.load())
        self.rows = pr.carregar(FIXTURE)
        self.tab = pr.tabular(self.rows, self.ids)

    def test_totais(self):
        self.assertEqual(self.tab["total"], 6)
        # entorno = perfis fora do condomínio (entorno, trabalha, usuario, outro)
        self.assertEqual(self.tab["entorno"], 3)
        self.assertEqual(self.tab["com_observacao"], 2)

    def test_ranking_pontos(self):
        self.assertEqual(self.tab["ponto"]["P4"], 2)
        self.assertEqual(self.tab["ponto"]["P1"], 1)
        self.assertEqual(self.tab["ponto"]["outro"], 1)
        # P99 não existe no cadastro → contado como inválido e avisado.
        self.assertEqual(self.tab["ponto"]["(inválido)"], 1)
        self.assertTrue(any("P99" in a for a in self.tab["avisos"]))

    def test_campos_multiplos(self):
        self.assertEqual(self.tab["problemas"]["congestionamento"], 3)
        self.assertEqual(self.tab["medidas"]["ajuste_semaforo"], 3)

    def test_gate(self):
        self.assertEqual(pr.gate(self.tab, 5, 3), [])  # atingido
        pendente = pr.gate(self.tab, 50, 10)
        self.assertEqual(len(pendente), 2)  # total e entorno abaixo do mínimo

    def test_render_inclui_nomes_do_cadastro(self):
        md = pr.render_md(self.tab, pontos.load())
        self.assertIn("**P4**", md)
        self.assertIn("GERADO por scripts/processar_respostas.py", md)
        self.assertIn("6 respostas", md)

    def test_csv_sem_colunas_falha(self):
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as tf:
            tf.write("a,b\n1,2\n")
        with self.assertRaises(SystemExit):
            pr.carregar(pathlib.Path(tf.name))


if __name__ == "__main__":
    unittest.main()
