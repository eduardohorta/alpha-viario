# Checklist de liberação — antes de protocolar

> Companheiro humano do `make release-check` (a verificação automática). Aqui ficam as
> **decisões e preenchimentos da comissão** que a automação não faz sozinha.
> **Decisões da reunião de 13/08/2026 incorporadas** (ata em `interno/ata-reuniao-2026-08-13.md`).
> Backlog completo do projeto: [PENDENCIAS.md](PENDENCIAS.md).

## 0. Verificação automática
- [ ] `make release-check` **verde** (modo estrito: links, vazamento de `interno/`/`revisoes/`,
      placeholders e consistência dos pontos). *(residuais conhecidos: número/data do ofício e
      pacote a rebuildar — ver §4.)*

## 1. Decisões da comissão (13/08/2026) — destravam o `release-check`
- [x] **Identidade e assinatura:** peças assinadas por **Eduardo de Oliveira Horta (representante)**
      pela **Comissão Viária Estrada das Três Meninas**; contato **comissao.viaria@outlook.com**.
      *(número e data do ofício ficam para o ato do protocolo.)*
      Peças atualizadas: [memorando](relatorios/memorando-externo.md) ·
      [ofício](relatorios/oficio-eptc-rascunho.md) · [anexo](relatorios/anexo-matriz-pontos.md).
- [x] **Canal de protocolo:** **SMAMUS (principal)**, com cópia à **EPTC/SMMU** e às
      **Subprefeituras Centro-Sul e Glória**. As peças pedem que a SMAMUS articule a EPTC para a
      parte de trânsito (vistoria, contagens, semáforos).
- [x] **Lista de pontos:** **P1–P8 + novo P9** (entroncamento Rua Santuário × Av. Oscar Pereira);
      o antigo P9 (rótula Cristiano Kraemer × Juca Batista) foi **retirado**.
- [x] **Demandas D2/D3:** **incluídas** nas peças em **versão genérica** (retorno seguro; avaliação
      de capacidade da Cristiano Kraemer), sem detalhe de condomínio.
- [x] **Questionário:** **em espera** (não é condição do protocolo).
- [x] **Sensibilidade (o que tornar público):** itens 1–5 **privados por ora** (peças em versão
      conservadora); material de contextualização **restrito aos membros**; **repositório privado**;
      sinistros **só agregados**.
- [x] **Termos sensíveis:** `interno/termos-sensiveis.txt` **criado**
      — ⚠️ **preencher com os nomes reais** (proprietários desapropriados / moradores) antes do protocolo.

## 2. Rechecagem institucional datada (imediatamente antes de protocolar)
Confirmar, com data, antes de enviar — detalhe e responsáveis em [PENDENCIAS §A](PENDENCIAS.md):
- [ ] **Respostas do e-SIC** (decisão: aguardar antes de protocolar): **responderam 1, 4, 5, 6, 7
      e 8** (1 e 5, parciais) e o **9** (01/09, parcial: depósito remetido à SMF); o **10** está
      prorrogado até **10/09**; **11** vence 02/09; **12–15** vencem 08/09 (o 15, protocolo
      017822-26-45, desdobra o 1 e vai à SMMU); **16–17** vencem 14/09 (desdobram os Pedidos 8 e
      7); **18** (018008-26-10, SMF) vence 21/09.
      **Decisão de 20/08:** protocolar em **01/09/2026**, sem esperar os derivados 11–17 (prazos
      08/09 e 14/09) — dá tempo aos pedidos originais ainda no prazo (9, 10) sem empurrar o
      protocolo para depois da janela confortável da LOA 2027.
- [ ] **Janela da LOA 2027:** o Executivo envia a proposta à Câmara **por volta de 15/out**
      (a confirmar no texto da Lei Orgânica) — **início de setembro ainda alcança o orçamento 2027.**
- [ ] **PDUS/LUOS** — sanção/publicação e transição (Pedido 6 respondido: ZOT 1/3/14/15, não é vetor de adensamento).
- [ ] **Projeto da Av. Monte Cristo** — status atual: **Pedido 5 respondeu (24/08)**. Sinalização
      concluída em projeto, implantação parcial (SMSURB parado desde set/2024); o nó específico
      do P2 tem projeto próprio da GPTC-EPTC, com manifestação ainda pendente. Afeta P2.
- [ ] **Plano Funcional** — desenhos vigentes e status de implantação: **Pedido 4 respondeu**
      (quadro de expedientes complementares) e **Pedido 1 respondeu, parcial** (EPTC: sem
      sinalização aprovada para a nova interseção Costa Gama; processo migrou à SMMU — Pedido
      15). Os desenhos gráficos do corredor completo (Anexo 7) não vieram em nenhuma das duas.
- [ ] **Canais institucionais** — setor de protocolo na SMAMUS e encaminhamento das cópias.

## 3. Base de evidência e enquadramento técnico
- [ ] **Sonda de tempos:** agregados consolidados (janela 04–16/jul, 1.440 medições) — ver
      [resumo](dados/tratados/sonda_tempos_resumo.md). Reprocessar perto do protocolo.
- [ ] **LAIs:** incorporar as respostas conforme chegarem; registrar as pendentes.
- [x] **Novo P9:** georreferenciado por **pin (14/08)** e associado (~17 sinistros; 2 graves, 6 motos) — incorporado ao pipeline, à matriz e ao mapa.
- [ ] **Pedido à SMAMUS/EPTC:** manter explícito que o dossiê é indicativo e solicita vistoria,
      contagens, planos semafóricos e demais validações.

## 4. Residuais para o dia do protocolo
- Número e data do **ofício** (hoje `nº 01/2026`, "setembro de 2026" — confirmar).
- **Rebuild do pacote** (`make pacote`, exige Pandoc/XeLaTeX) para refletir as peças atualizadas.

Coleta física comunitária e questionário não são gates deste ciclo.
