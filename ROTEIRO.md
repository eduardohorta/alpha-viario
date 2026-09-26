# Roteiro operacional — caminho crítico e janelas (jul–out 2026)

> **Espinha operacional do projeto.** Complementa o [PENDENCIAS.md](PENDENCIAS.md) (backlog
> por responsável) e o [LIBERACAO.md](LIBERACAO.md) (gate final): aqui está **a ordem, as
> dependências e as datas-alvo**. Atualizar conforme a realidade — datas-alvo são
> compromissos de ritmo, não promessas.

## 1. Princípio: quatro trilhas paralelas

O erro a evitar é tratar o projeto como uma fila única atrás da comissão. As trilhas abaixo
andam **em paralelo**; só convergem no protocolo.

| Trilha | O que é | Bloqueada por | Quem toca |
|--------|---------|----------------|-----------|
| **A — Informação (LAI)** | [Pedidos de acesso à informação](relatorios/pedidos-informacao-lai.md) sobre Plano Funcional, execução, Costa Gama, Monte Cristo, PDUS | **nada** — pessoa física protocola hoje | 1 morador (gabinete apoia) |
| **B — Comissão** | Decisões mínimas: quem assina, canal, D2/D3 e P9 | agenda da comissão | comissão |
| **C — Dados independentes** | Série da [sonda de tempos](campo/sonda-tempos-google.md) nas 14 rotas e capturas já registradas do trânsito típico | **nada** | serviços Google Cloud → repositório privado |
| **D — Gabinete** | Agregação da sonda, mapa, matriz e incorporação das respostas LAI | insumos de A e C | CLAUDE/CODEX |

**Dependências reais (e só estas):**

```
A (LAI) ───────────────────┐
C (sonda + capturas) ──────┼─→ consolidação na matriz ─→ release-check verde ─→ PROTOCOLO
B (assinatura + canal) ────┘                                                        │
                                                                acompanhamento ←─────┘
                                                        (vistoria técnica EPTC + demais ações)
```

Coleta física e questionário **não são premissas operacionais deste ciclo**: a mobilização
necessária não está disponível. Permanecem documentados como instrumentos de contingência
ou apoio a uma vistoria técnica, mas não condicionam a consolidação nem o protocolo.

## 2. Janelas de calendário (por que não dá para esperar indefinidamente)

- **LOA 2027.** A [página oficial municipal](https://prefeitura.poa.br/smpg/lei-orcamentaria-anual-loa), consultada em 25/09/2026, informa envio do projeto até **15/out** e votação até **5/dez**. Não há fundamento nesta fonte para um corte absoluto em agosto. Essas datas não garantem dotação: confirmar com o Município os requisitos e a viabilidade de inclusão do pleito.

- **Regulamentação do PDUS/LUOS.** Sanção, publicação e transição em curso em 2026. É a
  janela para vincular **contrapartidas viárias de novos empreendimentos** da Zona Sul aos
  pontos do projeto (alavanca §E do PENDENCIAS) — depois que os primeiros licenciamentos
  passarem sem essa vinculação, a oportunidade se perde caso a caso.
- **Respostas LAI têm prazo legal de 20 dias** (+10 de prorrogação): protocolando na
  primeira quinzena de julho, as respostas chegam **até o início de agosto** — a tempo de
  entrar no dossiê.

## 3. Histórico das metas (jul–set/2026)

> Metas e status registrados à época, preservados para rastreabilidade; não são a lista de pendências atual. A meta de 01/09 não comprova protocolo. A relação fundiária do P7 foi reconciliada em 24/09.

| Até | Entrega | Trilha |
|-----|---------|--------|
| **10/jul** ✅ | Pedidos LAI 1–7 protocolados no e-SIC ([acompanhamento](relatorios/pedidos-informacao-lai.md#acompanhamento)); instrumentos de questionário montados, mas em espera; sonda de tempos de viagem ligada ([setup](campo/sonda-tempos-google.md)) | A, C |
| **15/jul** ⚠️ | Decisões mínimas da comissão por reunião ou mensagem: quem assina, canal, D2/D3 e P9. **Não houve reunião — Plano B acionado em 15/07** (mensagem com as decisões reduzidas enviada; aguardando resposta). | B |
| **20/jul–03/ago** | Sonda acumula série nos picos; gabinete confere continuidade e qualidade. Acompanhar os pedidos LAI até o prazo ordinário de resposta. **Pedidos 2 e 3 já respondidos em 21/07** — P7: projeto aprovado obtido e **caducado**, incorporado ao dossiê; desdobrou-se o **Pedido 8 à PGM** (saldo das obrigações + desapropriações), **protocolado em 22/07 (017520-26-22, prazo 11/08)**. | A, D |
| **03/ago** | ~~Respostas LAI recebidas~~ **Prorrogadas em 22/07:** Pedidos 1, 4, 5, 6 e 7 tiveram prazo estendido em 10 dias (art. 14 §3º Dec. Mun. 19.990/2018, "informação não sistematizada") — novo prazo 13/08. Responderam: **Pedido 7 adiantado (10/08)** — Waze desde 2019, ObservaMOB, planos semafóricos de P5 e P8; **Pedido 6 no prazo (13/08)** — zoneamento PDUS e mapa de contrapartidas viárias; **Pedido 4 um dia após (14/08)** — quadro de expedientes complementares; **Pedido 1 em 17/08** — EPTC sem projeto de sinalização para a nova interseção Costa Gama, processo migrado à SMMU (novo Pedido 15); **Pedido 5 em 24/08** — SMMU: sinalização da Av. Monte Cristo concluída em projeto mas implantação parcial (SMSURB parado desde set/2024), nó do P2 encaminhado à EPTC. **Os cinco pedidos da prorrogação de 22/07 estão todos respondidos.** Ver [acompanhamento](relatorios/pedidos-informacao-lai.md#acompanhamento). | A |
| **07/ago** ✅ | **Documentação da administração do Alphaville** (TC integral, aditivos, Parecer CTAAPS 093/2020, decretos de desapropriação de 2020) analisada e incorporada ao dossiê. **Pedidos 9 e 10 protocolados** (nº 017700-26-00 e 017701-26-68, ambos com prazo 31/08): efetivação das desapropriações e depósito da Cláusula Nona; mapa das desapropriações e atualização do Parecer CTAAPS 093/2020. **Trilha A completa — 10 pedidos protocolados, nada pendente de nossa parte.** | A, D |
| **10/ago** | Agregados preliminares da sonda + respostas LAI **disponíveis até então** (2, 3, possivelmente 8) incorporados à [matriz de status](relatorios/matriz-publica-status-plano-funcional.md); pré-pauta e peças para a reunião de 13/8. A base documental está **muito mais forte** que o previsto — a lacuna que resta é o **status de 2026** (Pedidos 8, 9 e 10), não o histórico. | A→D, C→D |
| **11/ago** | **Pedido 8 prorrogado pela PGM** por 10 dias (mesma base legal e justificativa dos Pedidos 1, 4, 5, 6 — art. 14 §3º Dec. Mun. 19.990/2018, "informação não sistematizada"). Novo prazo: **21/08/2026**. Ver [acompanhamento](relatorios/pedidos-informacao-lai.md#acompanhamento). | A |
| **21/ago** ✅ | **Pedido 8 respondido pela PGM**, no próprio novo prazo. Confirma o **Termo de Compromisso vigente**; detalha **quatro desapropriações** em andamento (P7: uma por acordo, outra judicial; eixo (Três Meninas 1085) judicial; P6 aguardando novo decreto); revela **demolição judicial pendente desde 2014** no P7. Ver [leitura completa](relatorios/projetos-viarios-ja-aprovados.md#resposta-lai-ao-pedido-8-21082026-pgm-detalha-as-quatro-desapropriações-pendentes-e-confirma-o-termo-vigente). | A |
| **01/set** ✅ | **Pedido 9 respondido parcialmente pela PGM.** Imóvel diretamente referido no Decreto 20.860/P7 concluído por acordo em 2025; eixo (Três Meninas 1085) judicializado, sem imissão provisória; P6 com DUP caducada em 28/12/2025 e novo decreto previsto a partir de dez/2026. O depósito da Cláusula Nona foi remetido à SMF → **Pedido 18 protocolado** no mesmo dia (018008-26-10, prazo 21/09). A relação entre os processos fundiários do P7 citados nas respostas 8 e 9 exige reconciliação. | A, D |
| **13/ago** ✅ | Comissão validou pontos e peças, define assinatura/canal e encaminha o protocolo com pedido explícito de vistoria e dados técnicos da EPTC. | B |
| ~~20/ago~~ **01/set** | `make release-check` **já verde em 20/08** — decisão de 20/08: aguardar mais alguns dias antes de protocolar, para dar tempo às respostas ainda em prazo (~~Pedido 5, vencido~~ **respondido em 24/08**; ~~8, 21/08~~ **respondido em 21/08**; **9 respondido parcialmente em 01/09; 10 prorrogado até 10/09**). Novo alvo: **protocolo na EPTC em 01/09/2026**, sem dependência de coleta física ou questionário. | convergência |
| **set–out** | Acompanhamento: cobrança de prazos, reunião técnica, vistoria conjunta; acionamento do canal político **depois** do protocolo (sequência em `interno/`) | — |

## 4. Decisões vigentes e próximos passos

O Plano B acionado em 15/07 é histórico: as decisões mínimas foram tomadas em **13/08**. Assina Eduardo de Oliveira Horta, pela **Comissão Viária Estrada das Três Meninas**; canal principal **SMAMUS**, com cópia à EPTC/SMMU e às Subprefeituras Centro-Sul/Glória. O enquadramento territorial do novo P9 ainda requer confirmação.

1. Incorporar a **ata em preparação pela comissão** (informação de 25/09), sem antecipar deliberações.
2. Confirmar o **protocolo principal**: envio, número, data e comprovante ainda não confirmados aqui.
3. Acompanhar os **23 pedidos LAI** pela [tabela atual](relatorios/pedidos-informacao-lai.md#acompanhamento): faltam resposta de 14, documentos de 16, reexame de 18 e respostas 19/20/22/23. Pedido 21 respondeu em 16/09.
4. Consolidar novas evidências, gerar o pacote e fazer revisão factual, `make release-check` e inspeção visual do PDF antes de novo envio.

## 5. O que está disponível

Peças institucionais preenchidas, cadastro P1–P9, mapa, sinistros EPTC e auxiliares reconciliados, sonda com 8.582 medições em 14 rotas até 01/09 e documentação administrativa de 24–25/09 incorporada. A coleta e as cotas atuais de produção devem ser verificadas no ambiente privado. Questionário e coleta física permanecem em espera.
