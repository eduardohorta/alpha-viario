"""Testes dos derivados de sinistros já versionados (não precisam do bruto)."""
import csv
import json
import pathlib
import unittest
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
TRAT = ROOT / "dados/tratados"

# Totais principais documentados na metodologia (limiar principal).
EXPECTED_PRINCIPAL = {
    "P1": (29, 4, 0, 6),
    "P2": (58, 7, 0, 23),
    "P3": (44, 4, 0, 20),
    "P4": (409, 36, 2, 186),
    "P5": (71, 3, 0, 14),
    "P6": (8, 0, 0, 5),
    "P7": (18, 1, 0, 3),
    "P8": (36, 4, 0, 17),
}


def read_csv(name):
    with (TRAT / name).open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


class TestResumo(unittest.TestCase):
    def test_totais_principais(self):
        rows = {r["ponto"]: r for r in read_csv("acidentes_resumo_distancia_pontos.csv")}
        for pid, (occ, gr, fa, mo) in EXPECTED_PRINCIPAL.items():
            r = rows[pid]
            self.assertEqual(int(r["ocorrencias_principal"]), occ, pid)
            self.assertEqual(int(r["feridos_graves_principal"]), gr, pid)
            self.assertEqual(int(r["fatais_principal"]), fa, pid)
            self.assertEqual(int(r["motos_principal"]), mo, pid)

    def test_schema(self):
        rows = read_csv("acidentes_resumo_distancia_pontos.csv")
        for col in ("ponto", "ocorrencias_principal", "feridos_graves_principal", "fatais_principal"):
            self.assertIn(col, rows[0])


class TestAssociados(unittest.TestCase):
    def setUp(self):
        self.rows = read_csv("acidentes_associados_distancia.csv")

    def _overlap(self, rows):
        by_id = defaultdict(set)
        for r in rows:
            by_id[r["idacidente"]].add(r["ponto"])
        multi = sum(1 for pts in by_id.values() if len(pts) > 1)
        return len(rows), len(by_id), multi

    # Rodada 05: P9 entrou na associação por distância (+57 no contexto de 200 m,
    # +33 no limiar principal). Nenhum sinistro do P9 se sobrepõe a outro ponto —
    # a rótula fica ~3,2 km ao sul do P1 —, por isso 'multi' não muda.
    def test_overlap_todas(self):
        self.assertEqual(self._overlap(self.rows), (915, 857, 58))

    def test_overlap_principais(self):
        princ = [r for r in self.rows if r["associacao_principal"] == "sim"]
        self.assertEqual(self._overlap(princ), (706, 680, 26))

    def test_schema(self):
        for col in ("ponto", "idacidente", "dist_m", "associacao_principal", "data"):
            self.assertIn(col, self.rows[0])

    def test_totais_nao_somaveis(self):
        # A soma das linhas é maior que os sinistros distintos => não somável.
        linhas, distintos, _ = self._overlap(self.rows)
        self.assertGreater(linhas, distintos)


class TestP4Segmentos(unittest.TestCase):
    def test_reconciliacao(self):
        rows = read_csv("acidentes_p4_segmentos.csv")
        self.assertEqual(len(rows), 7)
        s = lambda c: sum(int(r[c]) for r in rows)
        self.assertEqual(s("ocorrencias"), 409)
        self.assertEqual(s("feridos_graves"), 36)
        self.assertEqual(s("fatais"), 2)
        self.assertEqual(s("motos"), 186)

    def test_ids_sequenciais(self):
        rows = read_csv("acidentes_p4_segmentos.csv")
        ids = [r["segmento_id"] for r in rows]
        self.assertEqual(ids, [f"P4-S0{i}" for i in range(1, 8)])


class TestMetadata(unittest.TestCase):
    def test_metadata_bate_com_csv(self):
        meta = json.loads((TRAT / "acidentes_distancia_metadata.json").read_text(encoding="utf-8"))
        todas = meta["associacoes"]["todas"]
        self.assertEqual(
            (todas["linhas"], todas["sinistros_distintos"], todas["sinistros_multi_ponto"]),
            (915, 857, 58),
        )
        jan = meta["janela_temporal_fonte"]
        self.assertEqual((jan["inicio"], jan["fim"]), ("2020-01-01", "2025-08-31"))


if __name__ == "__main__":
    unittest.main()
