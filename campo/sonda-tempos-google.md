# Sonda de tempos de viagem (Google Routes API) — setup sem cobrança

> Coleta série histórica própria de **tempo de viagem com trânsito** nas 12 rotas de
> [dados/rotas-sonda-tempos.csv](../dados/rotas-sonda-tempos.csv) (corredor P4 e trecho
> S06 nos dois sentidos, travessia do P7 nos dois sentidos, semáforo do P8, nós P1/P2,
> conversão do P5, acesso do P3). Rodando 2–4 semanas nos picos, produz: perfil de
> atraso por hora/dia, assimetria direcional (insumo do critério da faixa reversível) e
> o custo em minutos do retorno do P7.
>
> **Peso probatório:** dado *indicativo* de fonte neutra e reproduzível — entra no dossiê
> com metodologia declarada ("tempos estimados pela Routes API do Google"), como os
> sinistros. Não substitui contagem da EPTC; complementa.

## Garantia de custo zero — 3 camadas

A garantia **dura** é do lado do Google (camada 1); o script é redundância.

1. **Teto de cota no Console** *(obrigatório — bloqueio do lado do Google)*:
   em *APIs & Services → Routes API → Quotas*, definir **"Compute Routes requests
   per day" = 200**. Acima disso a API retorna erro `429` — **não cobra**.
2. **Orçamento com alerta**: em *Billing → Budgets*, criar orçamento de **US$ 1**
   com alerta em 50/90/100%. Se algum e-mail chegar, algo está errado — pare tudo.
3. **Tetos do coletor**: recusa a rodada se exceder **160 chamadas/dia** ou
   **4.500/mês**, e só coleta nas janelas 06–09h / 17–20h.

Dimensionamento: 12 rotas × 2 coletas/h × 6 h de pico = **144 chamadas/dia ≈
4.320/mês** — abaixo do teto do script e da ordem da **faixa gratuita mensal** do
Google Maps Platform (~10 mil chamadas/SKU nas SKUs Essentials na tabela de 2025;
**conferir a tabela vigente** e o SKU da `computeRoutes` com `TRAFFIC_AWARE` antes
de ligar a sonda — se o SKU for de faixa menor, os tetos acima ainda mantêm folga).

## Execução e armazenamento — Google Cloud + repositório privado

A sonda **é executada por serviços Google Cloud** nas janelas de pico. O repositório
privado `alpha-viario-sonda` recebe os registros produzidos por essa execução para
armazenamento e auditoria; **não é o executor da coleta**. Nem o notebook nem GitHub
Actions integram a operação corrente.

- **Google Cloud (operação corrente):** executa as consultas agendadas e mantém os
  controles de cota, orçamento e credencial fora do repositório público.
- **`alpha-viario-sonda` (destino privado):** recebe os registros brutos/operacionais
  encaminhados pela coleta em nuvem; serve para acompanhar continuidade e preparar
  agregados, sem expor a chave.
- **Local:** útil apenas para teste seco, diagnóstico ou reprodução manual; não deve ser
  considerado fonte da série em produção.

## Setup (uma vez, ~20 min)

1. Criar projeto no [Google Cloud Console](https://console.cloud.google.com) (precisa
   de conta de billing — não haverá cobrança com as travas acima).
2. Ativar **somente** a *Routes API*.
3. Criar **API key restrita**: *Credentials → API key → API restrictions → Routes API*.
4. Definir o **teto de cota** (camada 1) e o **orçamento** (camada 2).
5. Testar a seco (sem chave, nenhuma chamada): `python3 scripts/coletar_tempos_google.py --dry-run`
6. Testar 1 rodada real fora de pico: `GOOGLE_MAPS_API_KEY=SUA_CHAVE python3 scripts/coletar_tempos_google.py --force`
7. Na operação corrente, manter o agendamento e o encaminhamento dos registros nos
   **serviços Google Cloud**. O exemplo de cron abaixo serve somente para diagnóstico
   local, não para a coleta em produção:

```cron
*/30 6-8,17-19 * * * cd $HOME/alpha-viario && GOOGLE_MAPS_API_KEY=SUA_CHAVE /usr/bin/python3 scripts/coletar_tempos_google.py >> dados/brutos/tempos_viagem/cron.log 2>&1
```

*(No macOS, dar "Full Disk Access" ao `cron` ou usar `launchd`, se o log ficar vazio.)*

## Saída e governança

- Os registros da operação corrente são encaminhados ao repositório privado
  `alpha-viario-sonda`, fora deste repositório público; incluem `timestamp`, `rota_id`,
  `ponto_id`, `duracao_s`, `duracao_livre_s`, `distancia_m` e `status`.
- A chave de API **não entra em nenhum arquivo de repositório**; fica apenas no ambiente
  privado dos serviços Google Cloud.
- Ao fim da campanha (2–4 semanas), o gabinete agrega (perfil por hora × dia, atraso
  vs. `duracao_livre_s`, assimetria por sentido) e **só os agregados** entram no dossiê,
  com a janela de coleta declarada.
- Termos de uso: os dados servem à análise interna e a agregados no dossiê; não
  republicar conteúdo bruto de mapa/rotas do Google.

## Interpretação por rota (o que cada uma responde)

| Rotas | Pergunta respondida |
|-------|---------------------|
| R01–R02 | Perfil e assimetria do corredor P4 por hora (critério 1 da faixa reversível) |
| R03–R04 | O trecho S06 (crítico em sinistros) também concentra atraso? |
| R05 vs R06 | Custo real do retorno distante do P7 (assimetria dos sentidos) |
| R07–R08 | Atraso na travessia do semáforo do P8 no pico |
| R09–R10 | Atraso conjunto dos nós P1+P2 |
| R11 | Tempo da conversão do P5 no pico |
| R12 | Dificuldade de acesso à Monteggia (P3) |
