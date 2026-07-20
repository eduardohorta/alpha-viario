# Sonda multi-fonte de tempos de viagem (TomTom · HERE · Waze · Google)

> Mede as **mesmas 12 rotas** de [dados/rotas-sonda-tempos.csv](../dados/rotas-sonda-tempos.csv)
> por **fontes independentes**, para **validação cruzada**: *"três fontes confirmam +X min
> no pico"* tem peso probatório muito maior do que uma só. Complementa a
> [sonda Google](sonda-tempos-google.md) — que mede as mesmas rotas — somando TomTom, HERE
> e Waze. Script: [`scripts/coletar_tempos_multifonte.py`](../scripts/coletar_tempos_multifonte.py)
> (`make sonda-multi`).
>
> **Peso probatório:** dado *indicativo* de fontes neutras e reproduzíveis; entra no dossiê
> com metodologia declarada e — o diferencial — com **concordância entre fontes** como
> medida de confiança. Não substitui contagem da EPTC; complementa.

## As fontes e a garantia de custo zero

Todas rodam **apenas no nível gratuito** e o script nunca ultrapassa a cota. Chaves via
ambiente (`TOMTOM_API_KEY`, `HERE_API_KEY`, `GOOGLE_MAPS_API_KEY`); sem a chave, a fonte é pulada.

| Fonte | Cota gratuita (jul/2026) | Estoura vira cobrança? | Teto no script (`CAPS`) |
|-------|--------------------------|------------------------|--------------------------|
| **TomTom** Routing | 2.500 req/dia | não — retorna `429` | **2.000/dia** |
| **HERE** Routing v8 | 30.000 transações/mês (~1.000/dia) | cartão exigido; só cobra se passar | **950/dia** |
| **Waze** (não oficial) | ilimitado (sem billing) | nunca | **900/dia** (anti-bloqueio) |
| **Google** Routes | `TRAFFIC_AWARE` = **SKU Pro = 5.000/mês** (~166/dia) | **SIM, cobra se passar** ⚠️ | **150/dia** · só no pico |

**Cadência adaptativa** (o loop chama a sonda a cada 5 min; ela decide): pico (06–09/17–20h)
**10 min** · ombro (09–11/14–16h) 20 · entrepico 30 · madrugada 60. **Google só no pico, a
cada 30 min** → ~144/dia (~4.500/mês, sob os 5.000). Projeção validável: `python3
scripts/coletar_tempos_multifonte.py --selftest`.

**Camadas de custo:** (1) cadência acima; (2) **teto diário por fonte** (`CAPS` no script) num
livro-razão local `dados/brutos/tempos_viagem/ledger_multifonte.json` — a fonte é recusada ao
atingir o teto; (3) sem a chave, a fonte é pulada.

> ### ⚠️ Google — a trava DURA é no Console (obrigatória)
> O teto do script é a 2ª camada. A garantia de **custo zero** é do lado do Google:
> 1. **Cotas:** APIs & Services → Routes API → *Quotas* → **Compute Routes requests/day = 150**
>    (acima disso a API retorna `429` e **não cobra**).
> 2. **Orçamento:** Billing → Budgets → orçamento de **US$ 1** com alerta 50/90/100%.
>    Qualquer e-mail = algo errado, pare tudo.
> Sem esses dois passos, NÃO ative a fonte Google.

## Waze (opcional)

O acesso ao Waze usa a biblioteca não oficial `WazeRouteCalculator`
(`pip install WazeRouteCalculator`). Sem ela, a fonte Waze é pulada automaticamente
(`SEM_LIB`) e as demais seguem. É **zona cinzenta de ToS** e pode mudar/limitar — por isso
entra com pausa entre chamadas e é apenas confirmação, nunca o backbone.

### Fuso horario (armadilha em container/cron)

A sonda decide a cadencia pela hora **local do sistema** (`datetime.now()`). Containers Docker
rodam em **UTC por padrao** — nesse caso as janelas de pico caem 3h fora (no Brasil), e a sonda
coleta denso na madrugada e esparso no pico real. Vale o mesmo para a
[sonda Google](sonda-tempos-google.md), que usa a mesma premissa.

- **Container:** defina `TZ=America/Sao_Paulo` no `environment` do servico.
- **Cron:** garanta `TZ=America/Sao_Paulo` no topo do crontab.
- **Confira** com `docker exec <container> date` antes de confiar na serie.

Se a serie ja foi coletada em UTC, ela continua valida — basta normalizar (deslocar -3h) antes
de analisar, para nao misturar fusos no mesmo arquivo.

## Setup (uma vez, ~10 min)

1. **TomTom:** conta grátis em [developer.tomtom.com](https://developer.tomtom.com) →
   criar chave → `export TOMTOM_API_KEY=...`.
2. **HERE:** conta grátis em [platform.here.com](https://platform.here.com) → criar
   *API key* (REST) → `export HERE_API_KEY=...`.
3. *(Opcional)* **Waze:** `pip install WazeRouteCalculator`.
4. Testar a seco (nenhuma chamada): `python3 scripts/coletar_tempos_multifonte.py --force --dry-run`
5. Testar 1 rodada real fora de pico: `python3 scripts/coletar_tempos_multifonte.py --force`
6. Agendar via cron, a cada 30 min nos picos, todos os dias (domingo serve de linha de base):

```cron
*/30 6-8,17-19 * * * cd $HOME/alpha-viario && TOMTOM_API_KEY=... HERE_API_KEY=... /usr/bin/python3 scripts/coletar_tempos_multifonte.py >> dados/brutos/tempos_viagem/cron.log 2>&1
```

*(No macOS, dar "Full Disk Access" ao `cron` ou usar `launchd` se o log ficar vazio.)*

## Saída e governança

- Brutos em `dados/brutos/tempos_viagem/tempos_multifonte.csv` — **fora do versionamento**
  (como a sonda Google). Formato **longo** (uma linha por rota × fonte); colunas:
  `timestamp, rota_id, ponto_id, fonte, duracao_s, duracao_livre_s, distancia_m, status`.
- As chaves de API **não entram em nenhum arquivo do repositório** — só no ambiente/cron.
- Ao fim da campanha, o gabinete agrega (perfil por hora × dia, atraso vs. `duracao_livre_s`,
  **concordância entre fontes**) e **só os agregados** entram no dossiê, com a janela de
  coleta e as fontes declaradas.
- Termos de uso: dados para análise interna e agregados no dossiê; não republicar conteúdo
  bruto de mapa/rotas das fontes.

## Leitura cruzada (o que a concordância entre fontes indica)

- **Fontes concordam** (dispersão baixa) no pico → o atraso é robusto, forte no dossiê.
- **Fontes divergem** muito numa rota/hora → sinalizar para verificação em campo antes de
  usar o número (pode ser modelagem distinta de uma via específica).
- Combina com a leitura por rota da [sonda Google](sonda-tempos-google.md#interpretação-por-rota-o-que-cada-uma-responde)
  (R01–R02 corredor P4, R05×R06 assimetria do P7, etc.) — aqui, cada linha ganha o reforço
  das outras fontes no mesmo instante.
