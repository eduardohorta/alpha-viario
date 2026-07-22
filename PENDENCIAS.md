# Pendências e próximos passos

> Status consolidado do projeto. Itens de **estratégia jurídica** ficam em `interno/` (não versionado).
> **Ordem, dependências e datas:** [ROTEIRO.md](ROTEIRO.md).
> **Checklist de liberação** (preencher antes de circular/protocolar): [LIBERACAO.md](LIBERACAO.md).
> **Responsável:** **[C]** comissão · **[G]** gabinete (CLAUDE/CODEX). Coleta física
> comunitária está em espera e não é requisito de protocolo neste ciclo.

## A. Documentos e órgãos
> **Atalho:** os cinco itens marcados *(LAI)* têm **pedido pronto para protocolar** em [relatorios/pedidos-informacao-lai.md](relatorios/pedidos-informacao-lai.md) — pessoa física protocola no e-SIC, sem depender da comissão; prazo legal de resposta: 20 dias.

- [x] **[G]** Examinar os Expedientes Únicos `002.302984.00.0`, `002.322284.00.5` e `002.322291.00.8` e consolidar as obrigações viárias documentadas. Ver [projetos documentados](relatorios/projetos-viarios-ja-aprovados.md).
- [x] **[G]** Redigir os **pedidos LAI** para as informações que só a Prefeitura tem: [pedidos-informacao-lai.md](relatorios/pedidos-informacao-lai.md).
- [x] **[C/F]** **Protocolar os pedidos LAI 1–7** no e-SIC e registrar números/datas na tabela de acompanhamento (o 7 cobre dados de tráfego da EPTC: Waze for Cities, contagens, planos semafóricos). Protocolados em 10/07/2026, prazo 03/08/2026 — ver [tabela de acompanhamento](relatorios/pedidos-informacao-lai.md#acompanhamento).
- [ ] **[C]** *(LAI — pedido 1)* Obter cópia **identificada e legível dos desenhos vigentes** do Plano Funcional — inclusive Anexo 7, projeto geométrico reaprovado em 2013 e eventuais substituições — via EPTC/SMMU/SMAMUS.
- [ ] **[C/G]** *(LAI — pedido 2)* **Respondido parcialmente (21/07/2026):** SMOI forneceu o TRP de 2013 e **remeteu o saldo das obrigações à PGM**. Falta o quadro oficial de **execução por trecho/interseção** e a reconciliação de estacas → cobrado no **Pedido 8 (PGM)**.
- [ ] **[G]** Atualizar o **checklist interno de status do Plano Funcional** (`interno/checklist-status-plano-funcional.md`) com os achados dos expedientes e completá-lo quando os desenhos identificados chegarem.
- [ ] **[G]** *(LAI — pedido 5)* Confirmar o **status atual do projeto da Av. Monte Cristo** com a EPTC (afeta P2).
- [x] **[C/G]** *(LAI — pedido 3)* **Respondido (21/07/2026):** desenho da **conexão Três Meninas ↔ Costa Gama (P7) obtido** — 1ª etapa (proc. …09884) e solução definitiva com **conector a oeste** (proc. …0980); projeto **caducado** (Dec. 20.659/2020); desapropriações remetidas à PGM. Geometria da “alça” **identificada** e incorporada aos [projetos documentados](relatorios/projetos-viarios-ja-aprovados.md).
- [x] **[C/F]** **Pedido 8 (PGM) protocolado em 22/07/2026** (nº 017520-26-22, prazo 11/08/2026) — saldo das obrigações do Termo de Compromisso e status das desapropriações do P7, incluindo se a caducidade do projeto extingue a obrigação de fazer. Desdobramento das respostas 2 e 3. Ver [acompanhamento](relatorios/pedidos-informacao-lai.md#acompanhamento).
- [ ] **[G]** *(LAI — pedido 6)* **Zoneamento de Vila Nova no novo PDUS** (Anexo 5 / Plataforma do Regramento Construtivo) — há adensamento previsto no entorno?
- [x] **[G]** **Subprefeitura/região de cada ponto — confirmado (22/07/2026)** por consulta geoespacial à camada oficial de bairros: 7 dos 9 pontos ficam integralmente na Região 12 – Centro-Sul (RP6); só o P8 e a extremidade do P6 caem na Região 9 – Glória (RP5). Ver [tabela e metodologia](relatorios/revisao-documental.md#62-enquadramento-territorial-e-canais-de-protocolo).
- [x] **[G]** **Grafia oficial** "Cristiano Kraemer" — confirmada pela comissão.

## B. Evidência documental e de dados
- [x] **[G]** **Sonda de tempos de viagem ATIVA desde 2026-07-04** (serviços Google Cloud nos picos, com registros encaminhados ao repositório privado `alpha-viario-sonda`): [travas de custo](campo/sonda-tempos-google.md) todas configuradas (cota 200/dia no Console, orçamento com alertas, chave restrita à Routes API, tetos do coletor). Rotas em [dados/rotas-sonda-tempos.csv](dados/rotas-sonda-tempos.csv). Meta: 2–4 semanas de série antes do protocolo.
- [ ] **[G]** Verificar a continuidade/qualidade da coleta da sonda e gerar agregados por rota e janela horária (atraso versus fluxo livre, assimetria e custo do retorno do P7), sem expor dados brutos ou chave.
- [x] **[G]** **Capturas do trânsito típico** (Google Maps) por ponto/horário: 18 registros em 03/07 no [inventário](campo/observacoes/inventario-evidencias.csv) e no [roteiro](campo/observacoes/transito-tipico/README.md).
- [ ] **[G]** Incorporar à matriz e às peças externas os agregados da sonda e as respostas LAI — ou registrar explicitamente os pedidos em prazo/prorrogação.

### Em espera — mobilização comunitária

Questionário, fotos/vídeos, pins, cronometragens manuais, registros 360° e mapa de
alagamento não serão exigidos antes do protocolo: não há pessoal nem mobilização para uma
coleta física executável. Os instrumentos permanecem como contingência ou apoio a uma
vistoria técnica da EPTC, sem função de gate.

## C. Decisões da comissão
> **Plano B acionado em 15/07/2026** (reunião não ocorreu até a data-alvo do [ROTEIRO](ROTEIRO.md#4-plano-b--se-a-comissão-continuar-lenta)): mensagem com as decisões mínimas de assinatura, canal e confirmação de pontos/D2–D3 enviada à comissão no mesmo dia. Aguardando resposta.
- [ ] **[C]** Validar a lista de pontos (**8 + P9**) e confirmar o P9.
- [ ] **[C]** Aprovar/editar **memorando externo** e **ofício**; preencher contatos.
- [ ] **[C]** Definir o **destino de D2/D3** (manter internas até prova de benefício público).
- [ ] **[C]** Definir **postura e canais** de encaminhamento e **o que tornar público**.
- [ ] **[C]** Definir **quem assina/protocola**.
- [x] **[C/G]** Inbox bruto **internalizado** (movido para `interno/`); publicada [versão neutra](consultas/contribuicoes-comunitarias-publico.md).
- [x] **[G]** Validação **automática** de publicação no CI a cada push (**`public-check`**): links quebrados, vazamento de `interno/`/`revisoes/`, placeholders e consistência dos pontos.
- [ ] **[C/G]** **Revisão humana final** antes de publicar/protocolar: rodar **`make release-check`** (estrito) e resolver os avisos restantes (placeholders, `interno/termos-sensiveis.txt`).
- [x] **[C]** Histórico do git reescrito para remover o inbox bruto; **não reintroduzir** conteúdo sensível em arquivos públicos.

## D. Técnico / gabinete
- [x] **[G]** **Reconciliar os 10 temas do Morador C** com os P1–P9 (+ drenagem): ver [tabela de reconciliação](consultas/temas-morador-c-reconciliacao.md).
- [x] **[G]** **Georreferenciar preliminarmente P9/D1–D4/P7**: ver [georreferenciamento](dados/tratados/georreferenciamento_referencias_demandas.md). Referências de baixa confiança seguem sujeitas à validação por bases oficiais, imagem aérea ou vistoria técnica da EPTC.
- [x] **[G]** Esboçar **matriz pública de status** do Plano Funcional: ver [matriz pública](relatorios/matriz-publica-status-plano-funcional.md).
- [x] **[G]** Incorporar à matriz as previsões textuais, o aditamento de 2013 e a evidência de execução parcial localizadas nos expedientes.
- [ ] **[G]** Incorporar à matriz os **desenhos identificados** do Plano Funcional e mapear suas estacas quando obtidos. **P7 feito (jul/2026)** — projeto Costa Gama incorporado; os demais desenhos dependem dos Pedidos 1 e 4.
- [ ] **[G]** Manter a **versão enxuta da matriz** ([anexo](relatorios/anexo-matriz-pontos.md)) atualizada.
- [x] **[G]** Reclassificar o [plano de evidência leve](campo/plano-evidencia-leve.md) e o roteiro de campo como referências de contingência/vistoria técnica, sem função de gate.
- [x] **[G]** Gerar o **mapa dos pontos P1–P9** do cadastro canônico ([mapa](mapas/mapa-pontos.png), `make mapa`) e incluí-lo no anexo externo.
- [x] **[G]** Montar o **pipeline de tabulação das respostas** do questionário ([respostas](consultas/respostas/README.md), `make respostas`), mantido em espera e sem gate de volume.
- [x] **[G]** Consolidar o **roteiro operacional com caminho crítico e datas-alvo**: [ROTEIRO.md](ROTEIRO.md).

## E. Estratégia (alavancas — detalhe em `interno/`)
- Execução direta do Município; **contrapartidas urbanísticas** de novos empreendimentos (Zona Sul / novo PDUS); **conclusão dos projetos já aprovados** no eixo Três Meninas.

---
*Atualize este arquivo conforme os itens forem concluídos. Pendências sensíveis adicionais: ver `interno/`.*
