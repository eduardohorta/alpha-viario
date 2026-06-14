# Dados brutos

Origem, URL, SHA-256, licença e janela temporal de cada insumo estão em [`manifest.json`](manifest.json).

- **`cat_acidentes.csv` não é versionado** (~15 MB, CC-BY). Reproduza com `make fetch-data` (baixa + confere o SHA-256) e depois `make data` (gera os derivados). Detalhes em [`../tratados/acidentes_metodologia.md`](../tratados/acidentes_metodologia.md).
- `osm_vias_alpha_viario.json` — recorte de vias (OSM/Overpass, ODbL).
- `acidentes_resumo_pontos_api.json` — resposta bruta da API CKAN (Rodada 01).

Conferir integridade dos insumos presentes: `make verify-data`.
