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
ambiente (`TOMTOM_API_KEY`, `HERE_API_KEY`); sem a chave, a fonte é pulada.

| Fonte | Papel | Cota gratuita | Trava dura |
|-------|-------|---------------|------------|
| **TomTom** Routing | tempo com trânsito + tempo livre → índice | ~2.500/dia | chave freemium; teto do script |
| **HERE** Routing v8 | tempo com trânsito + `baseDuration` (livre) | freemium | chave freemium; teto do script |
| **Waze** (não oficial) | confirmação da comunidade | grátis | pausa entre chamadas; *zona cinzenta de ToS* |
| **Google** (opcional) | árbitro; só com `--com-google` | já coberto pela [sonda Google](sonda-tempos-google.md) | teto da Routes API |

**Camadas de custo no script:** (1) só roda nas janelas **06–09h / 17–20h** (salvo
`--force`); (2) **teto diário por fonte** (`--max-dia`, padrão 300) num livro-razão local
`dados/brutos/tempos_viagem/ledger_multifonte.json`; (3) sem a chave da fonte, ela é pulada.

Dimensionamento: 12 rotas × 2 coletas/h × 6 h de pico = **144 chamadas/dia por fonte** —
folgado dentro de todas as cotas acima.

> **Por que Google fica de fora por padrão:** a [sonda Google](sonda-tempos-google.md) já
> mede estas mesmas rotas. O multi-fonte adiciona TomTom + HERE + Waze (gratuitas) e a
> consolidação junta tudo na análise. Use `--com-google` só para uma janela de calibração.

## Waze (opcional)

O acesso ao Waze usa a biblioteca não oficial `WazeRouteCalculator`
(`pip install WazeRouteCalculator`). Sem ela, a fonte Waze é pulada automaticamente
(`SEM_LIB`) e as demais seguem. É **zona cinzenta de ToS** e pode mudar/limitar — por isso
entra com pausa entre chamadas e é apenas confirmação, nunca o backbone.

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
