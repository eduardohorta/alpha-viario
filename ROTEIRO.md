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
| **B — Comissão** | Decisões mínimas: quem assina, canal, D2/D3, P9, volume mínimo do questionário | agenda da comissão | comissão |
| **C — Campo e consulta** | Evidência leve (fotos, vídeos, pins, cronometragens) + questionário | parcialmente B (aviso de privacidade preenchido para o questionário); o resto, **nada** | moradores voluntários |
| **D — Gabinete** | Mapa, matriz, pipeline de respostas, incorporação das respostas LAI | insumos de A e C | CLAUDE/CODEX |

**Dependências reais (e só estas):**

```
A (LAI) ────────────────┐
C (campo + questionário) ┼─→ consolidação na matriz ─→ release-check verde ─→ PROTOCOLO
B (assinatura + canal) ──┘                                                        │
                                                             acompanhamento ←─────┘
                                                     (técnico + político, ver interno/)
```

O questionário depende da comissão **apenas** para preencher responsável/retenção do
[aviso de privacidade](consultas/moradores/aviso-privacidade.md) — uma decisão de 10
minutos que pode ser tomada por mensagem, sem reunião.

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
| **10/jul** | Pedidos LAI 1–6 protocolados no e-SIC; formulário online do questionário curto montado (rascunho) | A, D |
| **15/jul** | Decisões mínimas da comissão obtidas (reunião ou mensagem): aviso de privacidade preenchido, quem assina, canal, D2/D3, P9, volume mínimo | B |
| **20/jul** | Questionário circulando; campo solo iniciado (P7 cronometrado, pins D1–D4, fotos de pico em P4-S06/P1/P2/P5) | C |
| **10/ago** | Respostas LAI incorporadas à [matriz de status](relatorios/matriz-publica-status-plano-funcional.md); questionário no volume mínimo; evidência leve nos pontos prioritários registrada no [inventário](campo/observacoes/inventario-evidencias.csv) | A→D, C |
| **20/ago** | `make release-check` verde; **protocolo na EPTC** | convergência |
| **set–out** | Acompanhamento: cobrança de prazos, reunião técnica, vistoria conjunta; acionamento do canal político **depois** do protocolo (sequência em `interno/`) | — |

## 4. Plano B — se a comissão continuar lenta

A pausa atual (aguardando a comissão desde meados de junho) não pode paralisar as trilhas
A, C e D. Se não houver reunião até **15/jul**:

1. **Reduzir a pauta a 3 decisões** e colhê-las por mensagem (WhatsApp/e-mail), sem
   reunião: (a) responsável + retenção do aviso de privacidade; (b) quem assina;
   (c) canal de protocolo. Todo o resto tem default proposto pelo gabinete.
2. **Campo e LAI não esperam** — são atos individuais de morador, não da comissão.
3. **Última alternativa** (decisão a registrar): protocolo como **grupo de moradores
   nominados** em vez de "comissão", com adesões colhidas no questionário. Pior que o
   ideal, melhor que perder a janela da LOA.

## 5. Defaults propostos pelo gabinete (a confirmar pela comissão)

- **Volume mínimo do questionário:** **50 respostas, sendo ≥ 10 de fora do condomínio**
  (entorno/trabalhadores/usuários). Racional: estabiliza o ranking dos 9 pontos e
  demonstra que a demanda não é só interna; é atingível em ~2 semanas de divulgação.
- **Retenção das respostas:** 24 meses após o encerramento do projeto.
- **Canal de protocolo:** EPTC – Solicitações de Trânsito, com cópia à Subprefeitura
  Centro-Sul.

## 6. O que já está pronto e não bloqueia nada

- Peças externas em rascunho ([memorando](relatorios/memorando-externo.md) ·
  [ofício](relatorios/oficio-eptc-rascunho.md) · [anexo](relatorios/anexo-matriz-pontos.md))
  — faltam apenas os campos da comissão.
- [Pedidos LAI redigidos](relatorios/pedidos-informacao-lai.md) — prontos para colar no e-SIC.
- [Mapa dos pontos](mapas/mapa-pontos.png) — gerado do cadastro canônico (`make mapa`).
- [Pipeline de respostas do questionário](consultas/respostas/README.md) — tabulação
  automática quando as respostas chegarem (`make respostas`).
- Governança: `make check` / `make release-check` / testes / CI.
