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

## Limitações atuais

- Esta é uma triagem preliminar, não um estudo de segurança viária completo.
- A associação por distância reduz o ruído da bounding box, mas ainda não prova causalidade.
- A geometria OSM é preliminar e precisa ser validada contra base oficial municipal/SMAMUS.
- Coordenadas do CSV podem ser derivadas de geocodificação por logradouro e podem coincidir em pontos repetidos; isso exige revisão manual.
- Registros sem coordenada válida não foram inventados nem posicionados artificialmente.
- A grafia dos logradouros precisa ser confirmada com base municipal oficial antes de protocolo.
- Os totais não devem ser usados como prova causal sem inspeção dos registros individuais, mapa e vistoria de campo.
- **Totais por ponto não são somáveis:** 58 dos 800 sinistros distintos associam-se a mais de um ponto (ver "Sobreposição entre pontos"). Para um agregado, conte sinistros distintos.

## Próximo passo técnico

Revisar manualmente `acidentes_revisao_manual_proximos.csv` e `acidentes_p4_registros_segmentados.csv`, validar a geometria em imagem aérea/base municipal e, se necessário, ajustar os pontos de referência, limiares e marcos do P4. Para relatório externo, usar os números refinados apenas como "indícios preliminares por proximidade", nunca como prova causal.
