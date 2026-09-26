# Sonda de tempos de viagem (Google Routes API) — coleta, limites e custos

> Coleta série histórica própria de **tempo de viagem com trânsito** nas 14 rotas de
> [dados/rotas-sonda-tempos.csv](../dados/rotas-sonda-tempos.csv) (corredor P4 e trecho
> S06 nos dois sentidos, travessia do P7 nos dois sentidos, semáforo do P8, nós P1/P2,
> conversão do P5, acesso do P3 e dois sentidos do P9). Rodando 2–4 semanas nos picos, produz: perfil de
> atraso por hora/dia, assimetria direcional (insumo do critério da faixa reversível) e
> a assimetria entre sentidos no P7, sem isolar o efeito da alça.
>
> **Peso probatório:** dado *indicativo* de fonte neutra e reproduzível — entra no dossiê
> com metodologia declarada ("tempos estimados pela Routes API do Google"), como os
> sinistros. Não substitui contagem da EPTC; complementa.

## Controles de custo — sem garantia automática de gratuidade

O script local usa `TRAFFIC_AWARE`, recurso da SKU **Compute Routes Pro**, conforme [documentação de faturamento](https://developers.google.com/maps/documentation/routes/usage-and-billing). A [tabela de preços](https://developers.google.com/maps/billing-and-pricing/pricing), consultada em 25/09/2026, informa franquia mensal de **5.000 eventos** para essa SKU. Conferir condições, consumo agregado da conta e tabela vigente antes de executar.

- Os tetos **locais** documentados são 160 chamadas/dia e 4.500/mês. A operação em nuvem usa outro ambiente; não se pode inferir sua configuração a partir deste script.
- O bruto local registra **4.884 medições em agosto**, com **17 dias acima de 160**, máximo 168. Esses dados não provam cobrança, mas mostram que o teto de 160/4.500 não descreve um limite efetivo de toda a série. Conferir tentativas, outros projetos e faturamento no Cloud.
- Uma cota de 200/dia não garante ficar abaixo de 5.000/mês. Configurar limites disponíveis no Console e monitorar o consumo total; a aplicabilidade da cota diária precisa ser verificada no serviço em produção.
- Orçamento com alertas é mecanismo de acompanhamento, não bloqueio automático de cobrança. Manter chave restrita à Routes API.

Não foram alteradas cotas, agendamentos ou serviços em produção nesta revisão.

## Conferência no Console (26/09/2026, somente leitura)

- **Coleta ativa.** Os dois jobs do Cloud Scheduler (`*/30 6-8` e `*/30 17-19`, horário de Brasília) estão habilitados e a última execução de cada um terminou com sucesso. A série continua depois de 01/09; o bruto local é apenas a última cópia.
- **Tráfego da Routes API.** 5.122 solicitações em 30 dias (27/08 a 26/09), sem erros, média de cerca de 171 por dia. Nas últimas 24 horas o painel mostrou 266, valor que não expliquei; a média e o item seguinte indicam cerca de 168 por dia (12 rodadas por 14 rotas).
- **Cota diária.** A cota `ComputeRoutesRequestsPerDay` existe e está com uso de 84% (cerca de 168 de 200). O Console mostra o alerta "uso de cota elevado".
- **Faturamento (1 a 25/09).** R$ 0,36 no total: Secret Manager e Cloud Run Functions, já descontada a franquia. Não há linha da Routes API. O orçamento mensal de R$ 5 alerta em 50%, 90% e 100%; é um alerta, não uma trava de gasto.
- **Risco.** A revisão de 25/09 registrou, pela tabela de preços do Google, franquia mensal de 5.000 eventos para o recurso com tráfego (preço a confirmar na tabela vigente). A 168 por dia, um mês de 30 dias soma cerca de 5.040 e um de 31 dias, cerca de 5.208: o excedente seria pequeno, mas passa a haver cobrança. Agosto (4.884 medições) ficou abaixo, sem custo. Opções: reduzir uma rodada por dia (154 por dia, 4.774 em 31 dias) ou pausar os jobs ao fim da campanha, prevista para 2 a 4 semanas e já com cerca de 12.

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
   de conta de billing; conferir limites e preço antes de executar).
2. Ativar **somente** a *Routes API*.
3. Criar **API key restrita**: *Credentials → API key → API restrictions → Routes API*.
4. Definir o **limites de cota disponíveis** e o **orçamento com alertas**.
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
- Agregação: `make sonda-agg` baixa a série do repo privado (via `gh`) e roda
  [`scripts/agregar_sonda.py`](../scripts/agregar_sonda.py), gerando
  `dados/tratados/sonda_tempos_agregado.csv` (por rota × janela) e
  `dados/tratados/sonda_tempos_resumo.md` (índice de atraso, p85, assimetria por sentido).
  **Só os agregados** entram no dossiê, com a janela de coleta declarada; o bruto da Google
  fica gitignored. Reprocessar perto do protocolo, quando a série estiver cheia.
- Termos de uso: os dados servem à análise interna e a agregados no dossiê; não
  republicar conteúdo bruto de mapa/rotas do Google.

## Interpretação por rota (o que cada uma responde)

| Rotas | Pergunta respondida |
|-------|---------------------|
| R01–R02 | Perfil e assimetria do corredor P4 por hora (critério 1 da faixa reversível) |
| R03–R04 | O trecho S06 (crítico em sinistros) também concentra atraso? |
| R05 vs R06 | Assimetria estimada entre sentidos do P7; não estima isoladamente o efeito do retorno |
| R07–R08 | Atraso na travessia do semáforo do P8 no pico |
| R09–R10 | Atraso conjunto dos nós P1+P2 |
| R11 | Tempo da conversão do P5 no pico |
| R12 | Dificuldade de acesso à Monteggia (P3) |

O campo legado `duracao_livre_s` corresponde a `staticDuration`: estimativa **sem considerar tráfego**, não fluxo livre medido. Definições na [API](https://developers.google.com/maps/documentation/routes/reference/rest/v2/TopLevel/computeRoutes). R13/R14 cobrem o P9 desde 14/08/2026; as demais rotas, desde 04/07.
