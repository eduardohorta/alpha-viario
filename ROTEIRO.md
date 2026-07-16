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
| **C — Dados independentes** | Série da [sonda de tempos](campo/sonda-tempos-google.md) nas 12 rotas e capturas já registradas do trânsito típico | **nada** | serviços Google Cloud → repositório privado |
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

- **LOA 2027.** O Executivo municipal elabora a proposta orçamentária de 2027 tipicamente
  entre **agosto e setembro de 2026**. Pleito protocolado e em análise técnica **até meados
  de agosto** ainda pode disputar previsão de recursos para 2027; depois disso, a mira
  realista passa a ser 2028. *(Confirmar as datas da LDO/LOA municipais na época.)*
- **Regulamentação do PDUS/LUOS.** Sanção, publicação e transição em curso em 2026. É a
  janela para vincular **contrapartidas viárias de novos empreendimentos** da Zona Sul aos
  pontos do projeto (alavanca §E do PENDENCIAS) — depois que os primeiros licenciamentos
  passarem sem essa vinculação, a oportunidade se perde caso a caso.
- **Respostas LAI têm prazo legal de 20 dias** (+10 de prorrogação): protocolando na
  primeira quinzena de julho, as respostas chegam **até o início de agosto** — a tempo de
  entrar no dossiê.

## 3. Datas-alvo

| Até | Entrega | Trilha |
|-----|---------|--------|
| **10/jul** ✅ | Pedidos LAI 1–7 protocolados no e-SIC ([acompanhamento](relatorios/pedidos-informacao-lai.md#acompanhamento)); instrumentos de questionário montados, mas em espera; sonda de tempos de viagem ligada ([setup](campo/sonda-tempos-google.md)) | A, C |
| **15/jul** ⚠️ | Decisões mínimas da comissão por reunião ou mensagem: quem assina, canal, D2/D3 e P9. **Não houve reunião — Plano B acionado em 15/07** (mensagem com as decisões reduzidas enviada; aguardando resposta). | B |
| **20/jul–03/ago** | Sonda acumula série nos picos; gabinete confere continuidade e qualidade. Acompanhar os pedidos LAI até o prazo ordinário de resposta. | A, C, D |
| **03/ago** | Respostas LAI recebidas, ou prorrogações/atrasos registrados no [acompanhamento](relatorios/pedidos-informacao-lai.md#acompanhamento). | A |
| **10/ago** | Agregados preliminares da sonda + respostas LAI incorporados à [matriz de status](relatorios/matriz-publica-status-plano-funcional.md); pré-pauta e peças para a reunião de 13/8. | A→D, C→D |
| **13/ago** | Comissão valida pontos e peças, define assinatura/canal e encaminha o protocolo com pedido explícito de vistoria e dados técnicos da EPTC. | B |
| **20/ago** | `make release-check` verde; **protocolo na EPTC**, sem dependência de coleta física ou questionário. | convergência |
| **set–out** | Acompanhamento: cobrança de prazos, reunião técnica, vistoria conjunta; acionamento do canal político **depois** do protocolo (sequência em `interno/`) | — |

## 4. Plano B — se a comissão continuar lenta

> **ACIONADO em 15/07/2026.** A reunião não aconteceu até a data-alvo; a mensagem com
> as 3 decisões reduzidas foi enviada à comissão (WhatsApp/e-mail) no mesmo dia.
> Aguardando resposta — atualizar esta seção e o [LIBERACAO.md](LIBERACAO.md) assim que
> ela chegar.

A pausa atual (aguardando a comissão desde meados de junho) não pode paralisar as trilhas
A, C e D. Se não houver reunião até **15/jul**:

1. ✅ **Reduzir a pauta a 3 decisões** e colhê-las por mensagem (WhatsApp/e-mail), sem
   reunião: (a) quem assina; (b) canal de protocolo; (c) confirmação dos pontos/D2–D3.
   Todo o resto tem default proposto pelo gabinete.
   *(mensagem enviada em 15/07 — rascunho arquivado em `interno/`, não versionado)*
2. **Sonda e LAI não esperam** — a coleta automática e a resposta institucional não
   dependem da comissão.
3. **Última alternativa** (decisão a registrar): protocolo como **grupo de moradores
   nominados** em vez de "comissão". Pior que o ideal, melhor que perder a janela da LOA.

## 5. Defaults propostos pelo gabinete (a confirmar pela comissão)

- **Canal de protocolo:** EPTC – Solicitações de Trânsito, com cópia à Subprefeitura
  Centro-Sul.
- **Questionário:** manter em espera; só definir responsável, retenção e meta de respostas
  se a comissão decidir reabrir essa frente.

## 6. O que já está pronto e não bloqueia nada

- Peças externas em rascunho ([memorando](relatorios/memorando-externo.md) ·
  [ofício](relatorios/oficio-eptc-rascunho.md) · [anexo](relatorios/anexo-matriz-pontos.md))
  — faltam apenas os campos da comissão.
- [Pedidos LAI redigidos](relatorios/pedidos-informacao-lai.md) — prontos para colar no e-SIC.
- [Sonda de tempos de viagem](campo/sonda-tempos-google.md) — 12 rotas cadastradas, coletor com travas de custo (`make sonda`).
- [Mapa dos pontos](mapas/mapa-pontos.png) — gerado do cadastro canônico (`make mapa`).
- [Pipeline de respostas do questionário](consultas/respostas/README.md) — mantido em
  espera, sem função de gate no ciclo atual.
- Governança: `make check` / `make release-check` / testes / CI.
