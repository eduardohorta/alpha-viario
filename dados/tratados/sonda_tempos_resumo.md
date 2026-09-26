# Sonda de tempos de viagem — resumo agregado

> **Gerado por `scripts/agregar_sonda.py`.** Janela: **2026-07-04 a 2026-09-01**; **8582 medições** válidas em 14 rotas. Fonte: **Google Routes API** (sonda própria do projeto, coleta nos picos e fins de semana). **Indicativo, não substitui medição da EPTC** — pede-se vistoria e contagens oficiais.
> Índice = duração estimada com tráfego ÷ duração estimada sem considerar tráfego (`duration/staticDuration`). Apenas **agregados**; os registros brutos da Google não são publicados.

## Rotas mais lentas no pico (dia útil)

Série disponível de cada rota; janelas diferentes não constituem comparação controlada. Ver janela comum abaixo.

| Rota | Ponto | Índice de atraso (mediana) | p85 | Duração mediana | Trecho |
|------|-------|---------------------------:|----:|----------------:|--------|
| R13 | P9 | 1.67 | 2.74 | 1min12s | Santuario para Oscar Pereira atravessando o entroncamento (conversao a esquerda relatada) |
| R01 | P4 | 1.34 | 1.89 | 7min55s | Corredor Monteggia completo — Salomoni para Cavalhada/Nonoai |
| R02 | P4 | 1.32 | 1.74 | 9min55s | Corredor Monteggia completo — Cavalhada/Nonoai para Salomoni |
| R08 | P8 | 1.31 | 1.60 | 3min35s | Mariante leste para Costa Gama sul atravessando o semaforo |
| R04 | P4 | 1.19 | 2.51 | 1min25s | Trecho S06 — Joao Passuelo para Joao Vedana |
| R05 | P7 | 1.16 | 1.36 | 4min39s | Tres Meninas para Costa Gama sentido centro (rota legal inclui o retorno distante) |
| R12 | P3 | 1.16 | 2.58 | 3min18s | Rodrigues da Fonseca para Monteggia norte (acesso do P3) |
| R03 | P4 | 1.14 | 2.01 | 1min21s | Trecho S06 — Joao Vedana para Joao Passuelo |
| R10 | P2 | 1.13 | 1.47 | 3min05s | Monte Cristo oeste do P2 para Tres Meninas leste do P1 (atravessa P2 e P1) |
| R09 | P1 | 1.12 | 1.24 | 3min03s | Tres Meninas leste do P1 para Monte Cristo oeste do P2 (atravessa P1 e P2) |
| R11 | P5 | 1.11 | 1.61 | 2min18s | Salomoni para Cavalhada norte (inclui a conversao a direita do P5) |
| R14 | P9 | 1.08 | 1.79 | 0min42s | Oscar Pereira para Santuario atravessando o entroncamento (linha de base) |
| R07 | P8 | 1.05 | 1.15 | 3min00s | Costa Gama sul para Mariante leste atravessando o semaforo |
| R06 | P7 | 0.90 | 0.93 | 2min18s | Costa Gama para Tres Meninas (movimento permitido — linha de base) |

## Comparação em timestamps comuns a todas as rotas

2026-08-14–2026-09-01, somente picos de dias úteis: **145 observações por rota**, com datas e horários idênticos. Isso controla a composição temporal, não diferenças entre percursos nem o efeito de obras.

| Rota | Ponto | n | Índice mediano | p85 | Duração mediana (s) |
|---|---|---:|---:|---:|---:|
| R13 | P9 | 145 | 1.67 | 2.74 | 72 |
| R01 | P4 | 145 | 1.36 | 1.90 | 487 |
| R08 | P8 | 145 | 1.30 | 1.67 | 213 |
| R02 | P4 | 145 | 1.27 | 1.68 | 571 |
| R04 | P4 | 145 | 1.19 | 2.53 | 86 |
| R11 | P5 | 145 | 1.19 | 1.76 | 147 |
| R05 | P7 | 145 | 1.17 | 1.34 | 280 |
| R10 | P2 | 145 | 1.16 | 1.50 | 191 |
| R12 | P3 | 145 | 1.15 | 2.89 | 195 |
| R09 | P1 | 145 | 1.14 | 1.26 | 187 |
| R03 | P4 | 145 | 1.13 | 2.01 | 80 |
| R14 | P9 | 145 | 1.08 | 1.79 | 42 |
| R07 | P8 | 145 | 1.04 | 1.14 | 177 |
| R06 | P7 | 145 | 0.90 | 0.93 | 138 |

## Assimetria direcional no pico

| Par | Sentido A | Sentido B | Razão A/B (tempo) |
|-----|----------:|----------:|------------------:|
| P4 — corredor Vicente Monteggia | 7.9min (R01) | 9.9min (R02) | 0.80× |
| P4 — trecho S06 (João Vedana↔João Passuelo) | 1.4min (R03) | 1.4min (R04) | 0.95× |
| P7 — acesso à Costa Gama | 4.7min (R05) | 2.3min (R06) | 2.02× |
| P8 — semáforo Costa Gama × Mariante | 3.0min (R07) | 3.6min (R08) | 0.84× |
| P1–P2 — eixo Cristiano Kraemer | 3.0min (R09) | 3.1min (R10) | 0.99× |

## Destaque — P7 (retorno distante)

Três Meninas→Costa Gama (R05) tem estimativa mediana de **4.7 min / 3.0 km** no pico, contra **2.3 min / 1.9 km** no sentido oposto (R06): razões de **2.02× no tempo** e **1.61× na distância**. A assimetria é compatível com diferenças de percurso e tráfego, mas não isola o efeito da ausência da alça. Não compara a mesma viagem com e sem a intervenção. O coletor não armazena a geometria das rotas, portanto os campos de duração e distância não comprovam por si sós o trajeto do retorno.

## Limitações
- Rotas R13/R14 (P9) entraram na coleta em 14/08/2026, mais tarde que as demais (04/07/2026) — amostra menor (centenas de medições, não milhares) para esse ponto.
- Tempos do Google refletem estimativa de tráfego, não contagem volumétrica.
- Índices menores que 1 podem refletir diferenças entre as estimativas da API. Mediana e p85 não corrigem eventual viés sistemático do denominador.
- Definições: [Google Routes API](https://developers.google.com/maps/documentation/routes/reference/rest/v2/TopLevel/computeRoutes). O nome legado `duracao_livre_s` no CSV corresponde a `staticDuration`, não a fluxo livre medido.

