# Georreferenciamento preliminar - P9, D1-D4 e P7

> Rodada 05. Este arquivo registra referencias preliminares para orientar fotos, pins GPS e vistoria. Coordenadas de baixa confianca **nao devem** ser usadas como posicao oficial; servem apenas para organizar a coleta.

## Arquivo tabular

- `dados/tratados/georreferenciamento_referencias_demandas.csv`

## Metodologia

- **P9** foi localizado na base OSM local (`dados/brutos/osm_vias_alpha_viario.json`) como rótula/circular na Estrada Cristiano Kraemer. A coordenada e o centroide aproximado dos segmentos OSM com `junction=circular`.
- **P7/alça** foi registrada no ponto de referência já usado para o encontro Estrada das 3 Meninas x Estrada Costa Gama. Esta coordenada **não** representa o traçado da alça relatada; apenas o nó operacional de referência.
- **Clube** foi localizado via Nominatim/OSM como `Alphaville Clube`, no endereço 1701 da Estrada das 3 Meninas.
- **Toscana** e **Vêneto** foram associados a endereços públicos encontrados em páginas imobiliárias; o Nominatim retornou segmentos da Estrada das 3 Meninas, não portarias ou polígonos. Portanto, confiança baixa.
- **Lombardia** aparece em fontes públicas associado a mais de um endereço; usei o 1701 apenas como referência provisória porque também coincide com o Alphaville/Clube. Confiança baixa.
- **Reserva** não teve coordenada pública confiável nesta rodada.

## Recomendações de campo

- Coletar pin GPS específico para: P9, entrada/saída da rótula, quebra-molas de chegada/saída, Veneto, Lombardia, Clube, Reserva e Toscana.
- Para D1, registrar o ponto exato "antes do Veneto" e "antes do Lombardia"; o nome do residencial não basta.
- Para D2, registrar origem, destino, retorno atualmente usado e o ponto onde se imagina a nova manobra.
- Para P7, solicitar o desenho da alça; até lá, qualquer coordenada e apenas referência de entorno.

## Fontes públicas usadas

- OSM/Nominatim: busca por endereços e `Alphaville Clube`.
- Vera Bernardes: endereço geral do Alphaville Porto Alegre em Estrada das Três Meninas, 1701.
- Attria: endereço público do Alphaville Toscana em Estrada das Três Meninas, 1501.
- Attria: endereço público do Alphaville Vêneto em Estrada das Três Meninas, 2000.
- Imobiliárias/listagens públicas: referências conflitantes para Lombardia; pendente de validação por pin.
