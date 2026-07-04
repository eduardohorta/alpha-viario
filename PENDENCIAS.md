# Pendências e próximos passos

> Status consolidado do projeto. Itens de **estratégia jurídica** ficam em `interno/` (não versionado).
> **Ordem, dependências e datas:** [ROTEIRO.md](ROTEIRO.md).
> **Checklist de liberação** (preencher antes de circular/protocolar): [LIBERACAO.md](LIBERACAO.md).
> **Responsável:** **[C]** comissão · **[F]** campo/comunidade · **[G]** gabinete (CLAUDE/CODEX).

## A. Documentos e órgãos
> **Atalho:** os cinco itens marcados *(LAI)* têm **pedido pronto para protocolar** em [relatorios/pedidos-informacao-lai.md](relatorios/pedidos-informacao-lai.md) — pessoa física protocola no e-SIC, sem depender da comissão; prazo legal de resposta: 20 dias.

- [x] **[G]** Examinar os Expedientes Únicos `002.302984.00.0`, `002.322284.00.5` e `002.322291.00.8` e consolidar as obrigações viárias documentadas. Ver [projetos documentados](relatorios/projetos-viarios-ja-aprovados.md).
- [x] **[G]** Redigir os **pedidos LAI** para as informações que só a Prefeitura tem: [pedidos-informacao-lai.md](relatorios/pedidos-informacao-lai.md).
- [ ] **[C/F]** **Protocolar os pedidos LAI 1–7** no e-SIC e registrar números/datas na tabela de acompanhamento (o 7 cobre dados de tráfego da EPTC: Waze for Cities, contagens, planos semafóricos).
- [ ] **[C]** *(LAI — pedido 1)* Obter cópia **identificada e legível dos desenhos vigentes** do Plano Funcional — inclusive Anexo 7, projeto geométrico reaprovado em 2013 e eventuais substituições — via EPTC/SMMU/SMAMUS.
- [ ] **[C/G]** *(LAI — pedido 2)* Solicitar quadro oficial de **execução por trecho/interseção**, reconciliando as estacas do Plano Funcional com o trecho provisoriamente recebido em 2013 e distinguindo recebimento provisório, definitivo e saldo pendente.
- [ ] **[G]** Atualizar o **checklist interno de status do Plano Funcional** (`interno/checklist-status-plano-funcional.md`) com os achados dos expedientes e completá-lo quando os desenhos identificados chegarem.
- [ ] **[G]** *(LAI — pedido 5)* Confirmar o **status atual do projeto da Av. Monte Cristo** com a EPTC (afeta P2).
- [ ] **[C/G]** *(LAI — pedido 3)* Obter o desenho da **conexão/interseção Três Meninas ↔ Costa Gama** (**P7**) e confirmar geometria, primeira etapa, solução definitiva e desapropriações. Não designar a solução como “alça” antes dessa conferência.
- [ ] **[G]** *(LAI — pedido 6)* **Zoneamento de Vila Nova no novo PDUS** (Anexo 5 / Plataforma do Regramento Construtivo) — há adensamento previsto no entorno?
- [ ] **[G]** **Subprefeitura/região de cada ponto** (a área cruza RP5 e RP6).
- [x] **[G]** **Grafia oficial** "Cristiano Kraemer" — confirmada pela comissão.

## B. Campo / evidência (versão leve)
- [ ] **[C]** Distribuir o **questionário** a moradores e entorno (crowdsourced). Tabulação automática pronta: [pipeline de respostas](consultas/respostas/README.md) (`make respostas`).
- [ ] **[F]** **Levantamento fotográfico/360°** dos pontos (em organização pelos moradores).
- [ ] **[F]** **Fotos/vídeos** nos picos + **pins de GPS** dos pontos das demandas (D1–D4/P9).
- [ ] **[F]** **Cronometrar** o retorno distante (P7/D2); **fotografar** a rota de chão batido (P6).
- [ ] **[F]** Mapear **pontos de alagamento/drenagem** (nova dimensão).
- [x] **[G]** **Sonda de tempos de viagem ATIVA desde 2026-07-04** (repositório privado `alpha-viario-sonda`, GitHub Actions nos picos): [travas de custo](campo/sonda-tempos-google.md) todas configuradas (cota 200/dia no Console, orçamento com alertas, chave restrita à Routes API, tetos do script). Rotas em [dados/rotas-sonda-tempos.csv](dados/rotas-sonda-tempos.csv). Meta: 2–4 semanas de série antes do protocolo.
- [ ] **[G/F]** **Capturas do trânsito típico** (Google Maps) por ponto/horário: [roteiro](campo/observacoes/transito-tipico/README.md).
- [ ] **[F]** **Validar em campo** os segmentos prioritários do P4 (**S06/S01/S04**).
- [ ] **[F]** Registrar cada evidência no [inventário](campo/observacoes/inventario-evidencias.csv) (rastreabilidade + classificação público/interno).

## C. Decisões da comissão
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
- [x] **[G]** **Georreferenciar preliminarmente P9/D1–D4/P7**: ver [georreferenciamento](dados/tratados/georreferenciamento_referencias_demandas.md). Pins de campo seguem necessários para referências de baixa confiança.
- [x] **[G]** Esboçar **matriz pública de status** do Plano Funcional: ver [matriz pública](relatorios/matriz-publica-status-plano-funcional.md).
- [x] **[G]** Incorporar à matriz as previsões textuais, o aditamento de 2013 e a evidência de execução parcial localizadas nos expedientes.
- [ ] **[G]** Incorporar à matriz os **desenhos identificados** do Plano Funcional e mapear suas estacas quando obtidos.
- [ ] **[G]** Manter a **versão enxuta da matriz** ([anexo](relatorios/anexo-matriz-pontos.md)) atualizada.
- [x] **[G]** Documentar o **plano de evidência leve** (substitui o plano de campo "pesado"): ver [plano de evidência leve](campo/plano-evidencia-leve.md).
- [x] **[G]** Gerar o **mapa dos pontos P1–P9** do cadastro canônico ([mapa](mapas/mapa-pontos.png), `make mapa`) e incluí-lo no anexo externo.
- [x] **[G]** Montar o **pipeline de tabulação das respostas** do questionário ([respostas](consultas/respostas/README.md), `make respostas`, com gate de volume).
- [x] **[G]** Consolidar o **roteiro operacional com caminho crítico e datas-alvo**: [ROTEIRO.md](ROTEIRO.md).

## E. Estratégia (alavancas — detalhe em `interno/`)
- Execução direta do Município; **contrapartidas urbanísticas** de novos empreendimentos (Zona Sul / novo PDUS); **conclusão dos projetos já aprovados** no eixo Três Meninas.

---
*Atualize este arquivo conforme os itens forem concluídos. Pendências sensíveis adicionais: ver `interno/`.*
