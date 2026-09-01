# Sonda de tempos de viagem — resumo agregado

> **Gerado por `scripts/agregar_sonda.py`.** Janela: **2026-07-04 a 2026-09-01**; **8582 medições** válidas em 12 rotas. Fonte: **Google Routes API** (sonda própria do projeto, coleta nos picos e fins de semana). **Indicativo, não substitui medição da EPTC** — pede-se vistoria e contagens oficiais.
> Índice de atraso = duração real ÷ duração em fluxo livre (>1 = mais lento). Apenas **agregados**; os registros brutos da Google não são publicados.

## Rotas mais lentas no pico (dia útil)

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

## Assimetria direcional no pico

| Par | Sentido A | Sentido B | Razão A/B (tempo) |
|-----|----------:|----------:|------------------:|
| P4 — corredor Vicente Monteggia | 7.9min (R01) | 9.9min (R02) | 0.80× |
| P4 — trecho S06 (João Vedana↔João Passuelo) | 1.4min (R03) | 1.4min (R04) | 0.95× |
| P7 — acesso à Costa Gama | 4.7min (R05) | 2.3min (R06) | 2.02× |
| P8 — semáforo Costa Gama × Mariante | 3.0min (R07) | 3.6min (R08) | 0.84× |
| P1–P2 — eixo Cristiano Kraemer | 3.0min (R09) | 3.1min (R10) | 0.99× |

## Destaque — P7 (retorno distante)

A rota **legalmente disponível** de Três Meninas→Costa Gama (R05, incluindo o retorno distante) leva **4.7 min / 3.0 km** no pico, contra **2.3 min / 1.9 km** do movimento direto permitido (R06) — o desvio **2.0× o tempo** e **1.6× a distância**. É a medida empírica do custo imposto aos moradores pela ausência da conversão/alça.

## Limitações
- Rotas R13/R14 (P9) entraram na coleta em 14/08/2026, mais tarde que as demais (04/07/2026) — amostra menor (centenas de medições, não milhares) para esse ponto.
- Tempos do Google refletem estimativa de tráfego, não contagem volumétrica.
- Índice <1 em rotas curtas ocorre quando a duração em fluxo livre é conservadora; os agregados (mediana/p85) são robustos a esses casos.

