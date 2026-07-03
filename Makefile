# Projeto Viário — reprodução e verificação
#
# Alvos principais:
#   make all          registra pontos (GeoJSON), reproduz dados, gera mapa e pacote
#   make check        public-check em modo desenvolvimento (avisos não bloqueiam)
#   make release-check  public-check ESTRITO — antes de publicar/protocolar (avisos bloqueiam)
#   make test         roda os testes
#   make mapa         gera mapas/mapa-pontos.png do cadastro canônico
#   make respostas    tabula as respostas do questionário (consultas/respostas/)
#
# Reprodução dos dados de sinistros (insumo bruto não versionado):
#   make fetch-data   baixa cat_acidentes.csv dos Dados Abertos POA
#   make verify-data  confere o SHA-256 dos insumos contra o manifesto
#   make data         reproduz os derivados em dados/tratados/

PY := python3
RAW := dados/brutos/cat_acidentes.csv
URL := https://dadosabertos.poa.br/dataset/d6cfbe48-ee1f-450f-87f5-9426f6a09328/resource/b56f8123-716a-4893-9348-23945f1ea1b9/download/cat_acidentes.csv

.PHONY: all geojson mapa respostas pacote pacote-md data fetch-data verify-data check release-check test clean help

help:
	@awk 'sub(/^# ?/, "")' Makefile

all: geojson data mapa pacote

geojson:
	$(PY) scripts/pontos.py validate
	$(PY) scripts/pontos.py geojson

mapa:
	$(PY) scripts/gerar_mapa.py

respostas:
	@test -f consultas/respostas/respostas.csv || { echo "Ausente: consultas/respostas/respostas.csv (exporte do formulário — ver consultas/respostas/README.md)."; exit 1; }
	$(PY) scripts/processar_respostas.py

pacote:           # build de liberação: Markdown + PDF (exige Pandoc/XeLaTeX)
	$(PY) scripts/build_pacote.py

pacote-md:        # build de desenvolvimento: só Markdown
	$(PY) scripts/build_pacote.py --no-pdf

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

# Gate de liberação: avisos (placeholders, lista de termos sensíveis ausente)
# passam a bloquear. Use antes de circular o questionário ou protocolar na EPTC.
release-check:
	$(PY) scripts/pontos.py sync --check
	$(PY) scripts/public_check.py --strict

test:
	$(PY) -m unittest discover -s tests -v

clean:
	rm -f dados/tratados/pontos.geojson pacote-reuniao.pdf
