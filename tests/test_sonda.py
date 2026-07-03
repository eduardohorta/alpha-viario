"""Testes das travas de custo e do cadastro de rotas da sonda de tempos."""
import datetime as dt
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import coletar_tempos_google as sonda  # noqa: E402
import pontos  # noqa: E402


class TestRotas(unittest.TestCase):
    def test_cadastro_valido(self):
        rotas = sonda.carregar_rotas()
        self.assertGreaterEqual(len(rotas), 10)
        ids = [r["rota_id"] for r in rotas]
        self.assertEqual(len(ids), len(set(ids)), "rota_id duplicado")
        lat_min, lat_max, lon_min, lon_max = pontos.POA_BBOX
        pids = pontos.public_ids(pontos.load())
        for r in rotas:
            self.assertIn(r["ponto_id"], pids, f"{r['rota_id']}: ponto desconhecido")
            for lado in ("origem", "destino"):
                lat, lon = float(r[f"{lado}_lat"]), float(r[f"{lado}_lon"])
                self.assertTrue(lat_min <= lat <= lat_max, f"{r['rota_id']} {lado} lat")
                self.assertTrue(lon_min <= lon <= lon_max, f"{r['rota_id']} {lado} lon")


class TestTravasDeCusto(unittest.TestCase):
    def test_janela(self):
        self.assertTrue(sonda.dentro_da_janela(dt.datetime(2026, 7, 6, 7, 30)))
        self.assertTrue(sonda.dentro_da_janela(dt.datetime(2026, 7, 6, 17, 0)))
        self.assertFalse(sonda.dentro_da_janela(dt.datetime(2026, 7, 6, 9, 0)))
        self.assertFalse(sonda.dentro_da_janela(dt.datetime(2026, 7, 6, 12, 0)))
        self.assertFalse(sonda.dentro_da_janela(dt.datetime(2026, 7, 6, 21, 0)))

    def test_teto_diario_e_mensal(self):
        agora = dt.datetime(2026, 7, 6, 7, 0)
        ledger = {"2026-07-06": 150, "2026-07": 100}
        self.assertTrue(sonda.pode_gastar(ledger, agora, 12, 160, 4500))  # estoura dia
        ledger = {"2026-07-06": 0, "2026-07": 4495}
        self.assertTrue(sonda.pode_gastar(ledger, agora, 12, 160, 4500))  # estoura mês
        ledger = {"2026-07-06": 100, "2026-07": 3000}
        self.assertEqual(sonda.pode_gastar(ledger, agora, 12, 160, 4500), [])

    def test_registro_persiste(self):
        agora = dt.datetime(2026, 7, 6, 7, 0)
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "ledger.json"
            ledger = {}
            sonda.registrar_gasto(ledger, agora, 12, path)
            sonda.registrar_gasto(ledger, agora, 12, path)
            gravado = json.loads(path.read_text())
            self.assertEqual(gravado["2026-07-06"], 24)
            self.assertEqual(gravado["2026-07"], 24)

    def test_parse_duracao(self):
        self.assertEqual(sonda.parse_duracao("123s"), 123)
        self.assertEqual(sonda.parse_duracao("88.5s"), 88)
        self.assertIsNone(sonda.parse_duracao(None))
        self.assertIsNone(sonda.parse_duracao("abc"))

    def test_dry_run_sem_chave_nao_chama_rede(self):
        # main() sem GOOGLE_MAPS_API_KEY e com --dry-run deve sair 0 sem tocar a rede.
        import os
        os.environ.pop("GOOGLE_MAPS_API_KEY", None)
        self.assertEqual(sonda.main(["--dry-run", "--force"]), 0)


if __name__ == "__main__":
    unittest.main()
