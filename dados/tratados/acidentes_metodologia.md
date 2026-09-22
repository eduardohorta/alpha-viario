# Metodologia preliminar - acidentes de trânsito

Fonte consultada: Dados Abertos POA, conjunto "Acidentes de Trânsito - Acidentes", recurso CSV/API `b56f8123-716a-4893-9348-23945f1ea1b9`. Licença **CC-BY**. Origem, URL, SHA-256 e comando de download em [`dados/brutos/manifest.json`](../brutos/manifest.json); reprodução via `make data`.

Consultas realizadas em: 2026-06-04.

**Janela temporal da base.** O arquivo bruto `cat_acidentes.csv` cobre **2020-01-01 a 2025-08-31** (75.176 registros; fonte atualizada em 2025-09-01). Toda a análise abaixo está limitada a essa janela — sinistros anteriores a 2020 ou posteriores a ago/2025 não entram.

## Arquivos

- `dados/brutos/cat_acidentes.csv`: CSV completo baixado do recurso oficial.
- `dados/brutos/osm_vias_alpha_viario.json`: recorte OSM/Overpass das vias usadas como geometria preliminar.
- `dados/brutos/acidentes_resumo_pontos_api.json`: resposta bruta da API CKAN para a consulta agregada por ponto.
- `dados/tratados/acidentes-resumo-query.sql`: consulta SQL enviada ao datastore CKAN.
- `dados/tratados/acidentes_resumo_pontos.csv`: tabela tratada da Rodada 01, por bounding box/logradouro.
- `scripts/processar_sinistros_distancia.py`: script da Rodada 02 para associação por distância.
- `dados/tratados/acidentes_resumo_distancia_pontos.csv`: resumo refinado por distância geométrica.
- `dados/tratados/acidentes_associados_distancia.csv`: registros com coordenada associados aos pontos por distância.
- `dados/tratados/acidentes_revisao_manual_proximos.csv`: até 20 registros mais próximos por ponto, para revisão manual.
- `dados/tratados/acidentes_revisao_manual_notas.md`: notas da revisão manual preliminar dos registros mais próximos.
- `dados/tratados/acidentes_sem_coordenada_revisao.csv`: registros sem coordenada válida, mas com logradouros relevantes.
- `dados/tratados/acidentes_distancia_metadata.json`: metadados do processamento.
- `scripts/segmentar_p4_monteggia.py`: script da Rodada 03 para segmentação longitudinal do P4.
- `dados/tratados/acidentes_p4_segmentos.csv`: resumo do P4 por trechos entre marcos de interseção.
- `dados/tratados/acidentes_p4_registros_segmentados.csv`: registros P4 com estação longitudinal e segmento.
- `dados/tratados/acidentes_p4_hotspots_250m.csv`: janelas auxiliares de 250 m ordenadas por gravidade.
- `dados/tratados/acidentes_p4_marcos_intersecoes.csv`: marcos de logradouros secundários observados nos registros P4.
- `dados/tratados/acidentes_p4_segmentacao_metadata.json`: metadados da segmentação P4.

## Rodada 01 - triagem por bounding box/logradouro

- P1, P2, P3, P5, P7 e P8: janela geográfica aproximada de cerca de 200 m em torno da interseção identificada no OpenStreetMap.
- P4: busca por logradouro contendo `VICENTE MONTEGGIA`, pois é um corredor e não um ponto único.
- P6: busca por logradouro contendo `FLORESTAN FERNANDES`, `KANAZAWA` ou `KANASAWA`, pois a hipótese envolve rota secundária.

Essa triagem foi útil para priorizar a vistoria, mas nao deve ser usada como número final: ela pode supercontar por incluir acidentes próximos que não pertencem ao ponto, especialmente nos recortes por bounding box.

## Rodada 02 - refinamento por distância geométrica

O CSV completo foi validado em nível básico:

- 75.176 registros;
- 64.003 registros com coordenada válida aproximada dentro de Porto Alegre;
- 11.173 registros sem coordenada válida, vazia ou zerada;
- 25 registros sem coordenada válida tinham logradouros relevantes para P1-P8 e foram separados para revisão.

Critérios principais:

- P1, P2, P3, P5, P7 e P8: distância do registro ao ponto de referência da interseção.
- P4: distância do registro à geometria OSM da `Avenida Vicente Monteggia`.
- P6: distância do registro às geometrias OSM de `Rua Florestan Fernandes` e `Estrada Kanazawa`.
- Para interseções, o limiar principal foi 100 m e o contexto ampliado 200 m.
- Para corredores/rotas, o limiar principal foi 50 m e o contexto ampliado 100 m.

Resumo refinado pelo limiar principal:

| Ponto | Critério | Ocorrências | Feridos | Feridos graves | Fatais | Motos |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| P1 | até 100 m da referência | 29 | 11 | 4 | 0 | 6 |
| P2 | até 100 m da referência | 58 | 25 | 7 | 0 | 23 |
| P3 | até 100 m da referência | 44 | 24 | 4 | 0 | 20 |
| P4 | até 50 m da Av. Vicente Monteggia | 409 | 215 | 36 | 2 | 186 |
| P5 | até 100 m da referência | 71 | 29 | 3 | 0 | 14 |
| P6 | até 50 m da rota Florestan/Kanazawa | 8 | 9 | 0 | 0 | 5 |
| P7 | até 100 m da referência | 18 | 5 | 1 | 0 | 3 |
| P8 | até 100 m da referência | 36 | 15 | 4 | 0 | 17 |

Observação sobre P5: a fatalidade capturada na triagem por bounding box fica a cerca de 128 m da referência P5 e aparece apenas no contexto ampliado, associada a `AV CAVALHADA` sem logradouro secundário. Portanto, ela deve ser tratada como alerta de contexto, não como evidência direta da conversão João Salomoni -> Cavalhada sem revisão manual.

**Sobreposição entre pontos (totais não somáveis).** Considerando todas as associações (limiar principal + contexto ampliado), há **858 linhas** em `acidentes_associados_distancia.csv` para **800 sinistros distintos**: **58 sinistros aparecem em mais de um ponto** (o mesmo registro fica perto de duas referências, p. ex. P1/P9 na Cristiano Kraemer ou P7/P8 no eixo Costa Gama). **Logo, os totais por ponto não podem ser somados** — a soma superestima o total real. Restringindo às associações principais (`associacao_principal=sim`), são 673 linhas para 647 sinistros distintos (26 em mais de um ponto). Use sempre a contagem de sinistros **distintos** ao falar de um total agregado.

## Rodada 03 - segmentação do P4 por trecho

A Rodada 03 segmentou os 409 registros principais do P4 ao longo da geometria OSM da `Avenida Vicente Monteggia`. O script projeta cada sinistro no eixo longitudinal Cavalhada/Nonoai -> João Salomoni/Rodrigues da Fonseca e usa marcos observados nos próprios logradouros dos registros para formar trechos preliminares entre interseções.

Critérios:

- Entrada: apenas registros `P4` com `associacao_principal=sim` em `acidentes_associados_distancia.csv`.
- Geometria: caminho OSM da `Avenida Vicente Monteggia` no recorte local já validado na Rodada 02.
- Marcos: logradouros secundários recorrentes nos registros geocodificados, tratados como aproximações longitudinais, não como cadastro oficial.
- Total reconciliado: 409 ocorrências, 36 feridos graves, 2 fatais e 186 motos, igual ao resumo refinado do P4.

Resumo por trecho:

| Segmento | Trecho | Ocorrências | Feridos graves | Fatais | Motos |
| --- | --- | ---: | ---: | ---: | ---: |
| P4-S01 | Av. da Cavalhada / Av. Nonoai / R. Dr. Campos Velho -> Av. Fabio Araujo Santos | 104 | 11 | 0 | 34 |
| P4-S02 | Av. Fabio Araujo Santos -> Av. Otto Niemeyer | 42 | 3 | 0 | 18 |
| P4-S03 | Av. Otto Niemeyer -> Estr. Aracaju | 65 | 2 | 0 | 29 |
| P4-S04 | Estr. Aracaju -> Rua Amapa | 44 | 3 | 1 | 21 |
| P4-S05 | Rua Amapa -> Estr. Joao Vedana | 48 | 4 | 0 | 23 |
| P4-S06 | Estr. Joao Vedana -> Estr. Joao Passuelo | 67 | 9 | 1 | 41 |
| P4-S07 | Estr. Joao Passuelo -> Av. Joao Salomoni / Av. Rodrigues da Fonseca | 39 | 4 | 0 | 20 |

Leitura preliminar:

- O maior volume bruto aparece em P4-S01, no entorno Cavalhada/Nonoai/Campos Velho, com 104 ocorrências e 11 feridos graves.
- A maior concentração combinada de gravidade aparece em P4-S06, entre João Vedana e João Passuelo, com 67 ocorrências, 9 feridos graves, 1 fatal e 41 motos.
- P4-S04 também tem 1 fatal, mas menor volume absoluto.
- As janelas auxiliares de 250 m reforçam três pontos de atenção: 0-250 m, 1250-1500 m e 1750-2000 m.

Limite adicional: esta segmentação é suficiente para priorizar vistoria e mapas, mas não substitui base cadastral municipal, aerofoto, análise de boletins individualizados nem inspeção de campo.

## Rodada 05 - inclusão do P9 (rótula Cristiano Kraemer x Juca Batista)

Até a Rodada 03 o P9 não tinha coordenada confirmada e ficava fora da associação por distância; a matriz registrava "sinistros: a levantar". Em 20/07/2026 a transversal foi confirmada visualmente (OSM/Street View) como **Av. Juca Batista**, e o ponto entrou no pipeline com **os mesmos limiares das demais interseções** (principal 100 m, contexto 200 m), na coordenada -30.1476851, -51.2045098.

| Ponto | Critério | Ocorrências | Feridos | Feridos graves | Fatais | Motos |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| P9 | até 100 m da referência | 33 | 11 | 1 | 0 | 8 |

Contexto ampliado (200 m): 57 ocorrências. Distância mínima registrada: 3,8 m.

**Validação cruzada.** Os registros foram selecionados apenas por distância, sem usar nomes de logradouro. Ainda assim, **56 dos 57** no contexto de 200 m citam "AV JUCA BATISTA" e/ou "ESTR CRISTIANO KRAEMER" — corroboração independente de que a coordenada está no cruzamento correto.

**Cautela na leitura.** As 33 ocorrências são comparáveis às dos demais pontos de interseção porque usam o mesmo critério, mas herdam as mesmas limitações: associação por proximidade não é prova de causa, e parte das coordenadas do CSV vem de geocodificação por logradouro. Além disso, a Av. Juca Batista é um corredor de tráfego intenso: parte dos registros pode pertencer ao corredor e não à rótula. Antes de usar o número em peça externa, revisar os registros individuais em `acidentes_revisao_manual_proximos.csv`.

## Limitações atuais

- Esta é uma triagem preliminar, não um estudo de segurança viária completo.
- A associação por distância reduz o ruído da bounding box, mas ainda não prova causalidade.
- A geometria OSM é preliminar e precisa ser validada contra base oficial municipal/SMAMUS.
- Coordenadas do CSV podem ser derivadas de geocodificação por logradouro e podem coincidir em pontos repetidos; isso exige revisão manual.
- Registros sem coordenada válida não foram inventados nem posicionados artificialmente.
- A grafia dos logradouros precisa ser confirmada com base municipal oficial antes de protocolo.
- Os totais não devem ser usados como prova causal sem inspeção dos registros individuais, mapa e vistoria de campo.
- **Totais por ponto não são somáveis:** 58 dos 857 sinistros distintos associam-se a mais de um ponto (ver "Sobreposição entre pontos"). Para um agregado, conte sinistros distintos.

## Próximo passo técnico

Revisar manualmente `acidentes_revisao_manual_proximos.csv` e `acidentes_p4_registros_segmentados.csv`, validar a geometria em imagem aérea/base municipal e, se necessário, ajustar os pontos de referência, limiares e marcos do P4. Para relatório externo, usar os números refinados apenas como "indícios preliminares por proximidade", nunca como prova causal.

## Rodada 04: base oficial EPTC via Pedido 17 (22/09/2026)

**Fonte nova, distinta da Rodada 02.** O Pedido 17 (protocolo 017904-26-00), pedindo o "Relatório
de Ocorrências" citado no processo judicial do P7, foi respondido em 22/09/2026 com um
redirecionamento ao portal **ObservaMOB** e um link para um shapefile bruto da própria EPTC:
`ACIDENTES_TRANSITO_2010_202609` — **264.567 registros, todo o município, de 2010 a
setembro/2026**, incluindo sinistros só com danos materiais (não apenas os com vítima, como na
base "Dados Abertos POA" usada na Rodada 02). O arquivo bruto (~560 MB) fica em
`retornos-protocolos/017904-26-00/` (gitignored, fora do repositório público).

**Duas passagens.** Uma primeira extração cobriu só o P7 (`scripts/extrair_eptc_p7.py`), para
responder diretamente ao Pedido 17. Em seguida, `scripts/processar_sinistros_eptc_distancia.py`
reaplicou o **mesmo método da Rodada 02** (mesma fórmula de distância, mesmos limiares: 100 m
principal / 200 m contexto para interseções; 50 m / 100 m para corredores e rotas) aos **9 pontos
completos**, lendo o DBF diretamente via `struct` (sem bibliotecas GIS — o arquivo tem Latitude/
Longitude como campos de atributo, dispensando a leitura da geometria do shapefile). Tempo de
execução: ~34 s para 264.567 registros.

**Resultado — limiar principal (100 m / 50 m conforme o ponto), 2010–2026:**

| Ponto | Rodada 02 (2020–2025, c/ vítima) | Rodada 04/EPTC (2010–2026, todas) | Graves | Fatais | Motos |
|---|---:|---:|---:|---:|---:|
| P1 | 29 | 58 | 3 | 0 | 18 |
| P2 | 58 | 150 | 14 | 0 | 50 |
| P3 | 44 | 136 | 12 | 0 | 57 |
| P4 | 409 | 1.648 | 94 | 8 | 640 |
| P5 | 71 | 311 | 6 | 0 | 57 |
| P6 | 8 | 36 | 2 | 0 | 15 |
| P7 | 18 | 67 | 6 | 1 | 17 |
| P8 | 36 | 124 | 11 | 0 | 44 |
| P9 | 17 | 55 | 6 | 1 | 26 |

Os números sobem entre 2× e 4,5× em todos os pontos. A explicação dominante é metodológica, não
uma piora real: **janela 2,7× mais longa (16 anos contra 6)** e **inclusão de sinistros só com
danos materiais** (na extração do P7, 73% dos 67 registros não tinham vítima registrada — a
Rodada 02 não os capturava). Overlap entre pontos não recalculado nesta rodada; assumir a mesma
ordem de grandeza da Rodada 02 (registros perto de mais de uma referência) até nova checagem.

**Campo `Fatais` esclarecido — não é mais "achado a confirmar".** A checagem cruzada mostrou que
`Fatais = Morte + MortePoste` (óbito no local + óbito posterior à internação) em todos os casos
testados, inclusive no registro específico do P7 (id 579827, 25/02/2014: `Morte=0`,
`MortePoste=1`, `Fatais=1`). Ou seja, **é um óbito confirmado**, só que posterior ao acidente —
não um erro ou inconsistência de cadastro. Esse registro está fora da janela do relatório
judicial do P7 (2019–2024). Os fatais novos que a Rodada 02 não capturava: **P4 salta de 2 para
8**; **P7 e P9, de 0 para 1 cada**.

**2025–2026 no P7 (item "c" do Pedido 17):** 13 ocorrências no limiar principal, incluindo um
agrupamento recorrente a 24,1 m do ponto de referência (Três Meninas × Costa Gama,
`Cruzamento=Sim`) em 6 datas distintas entre abr/2025 e ago/2026 — pode indicar geocodificação num
ponto fixo do cruzamento, não a localização exata de cada ocorrência; não inflar a leitura sem
checar os boletins individuais.

**Limitações desta rodada (além das já listadas para a Rodada 02):**

- P4 e P6 não foram resegmentados com a base nova — a Rodada 03 (segmentação do P4) segue
  baseada na Rodada 02; refazê-la com 1.648 registros é trabalho futuro, não feito aqui.
- Overlap entre pontos (mesmo sinistro perto de duas referências) não recalculado para a base
  EPTC.
- "Fatais" é o campo mais confiável para óbitos (soma local + posterior); no dossiê público,
  preferir esse campo a "Morte" isoladamente.
- **Decisão em aberto:** se os números da Rodada 04 substituem os da Rodada 02 nas peças já
  aprovadas pela comissão (memorando, ofício, 13/08/2026), ou se os dois conjuntos convivem com a
  ressalva de janela/critério.

**Arquivos desta rodada:**

- `scripts/extrair_eptc_p7.py` — extração inicial, só P7.
- `scripts/processar_sinistros_eptc_distancia.py` — extração completa, 9 pontos.
- `dados/tratados/eptc_acidentes_p7_2010_202609.csv` — 86 registros (contexto 200 m) do P7,
  primeira passagem.
- `dados/tratados/eptc_acidentes_resumo_distancia_pontos.csv` — resumo por ponto, 9 pontos.
- `dados/tratados/eptc_acidentes_associados_distancia.csv` — registros individuais associados,
  9 pontos.
- `dados/tratados/eptc_acidentes_distancia_metadata.json` — metadados da extração completa.

Nenhum dos dois scripts é reexecutável sem o DBF bruto local (gitignored); servem como registro
auditável do método, não como pipeline reproduzível via `make data`.
