# Projeto Viário — reprodução e verificação
#
# Alvos principais:
#   make all          registra pontos (GeoJSON), reproduz dados e gera o pacote
#   make check        roda o public-check (porteiro de publicação)
#   make test         roda os testes
#
# Reprodução dos dados de sinistros (insumo bruto não versionado):
#   make fetch-data   baixa cat_acidentes.csv dos Dados Abertos POA
#   make verify-data  confere o SHA-256 dos insumos contra o manifesto
#   make data         reproduz os derivados em dados/tratados/

PY := python3
RAW := dados/brutos/cat_acidentes.csv
URL := https://dadosabertos.poa.br/dataset/d6cfbe48-ee1f-450f-87f5-9426f6a09328/resource/b56f8123-716a-4893-9348-23945f1ea1b9/download/cat_acidentes.csv

.PHONY: all geojson pacote data fetch-data verify-data check test clean help

help:
	@awk 'sub(/^# ?/, "")' Makefile

all: geojson data pacote

geojson:
	$(PY) scripts/pontos.py validate
	$(PY) scripts/pontos.py geojson

pacote:
	$(PY) scripts/build_pacote.py

fetch-data:
	curl -fSL -o $(RAW) '$(URL)'
	$(MAKE) verify-data

verify-data:
	$(PY) scripts/verify_data.py

data:
	@test -f $(RAW) || { echo "Ausente: $(RAW). Rode 'make fetch-data'."; exit 1; }
	$(PY) scripts/verify_data.py
	$(PY) scripts/processar_sinistros_distancia.py
	$(PY) scripts/segmentar_p4_monteggia.py
	@echo "Derivados reproduzidos em dados/tratados/."

check:
	$(PY) scripts/public_check.py

test:
	$(PY) -m unittest discover -s tests -v

clean:
	rm -f dados/tratados/pontos.geojson pacote-reuniao.pdf
