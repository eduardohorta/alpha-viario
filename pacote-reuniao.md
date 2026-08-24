---
title: "Projeto Viário — Vila Nova / Zona Sul"
subtitle: "Pacote de reunião — Comissão de Mobilidade"
author: "Comissão de Mobilidade — Moradores do Alphaville Porto Alegre"
date: "Julho de 2026"
lang: pt-BR
geometry: margin=2.2cm
fontsize: 11pt
---

<!-- GERADO por scripts/build_pacote.py — NÃO editar à mão. Fontes: relatorios/guia-validacao-comissao.md, relatorios/memorando-externo.md, relatorios/anexo-matriz-pontos.md -->

```{=latex}
\newpage
```

# Guia de validação com a comissão + encaminhamento à EPTC

> **Caminho escolhido:** protocolar com a evidência já disponível — sinistros, série da
> sonda e documentação oficial — e solicitar à EPTC os dados e a vistoria técnica que a
> comunidade não tem condições de produzir. Coleta física e questionário permanecem em
> espera por falta de mobilização e **não são condições do protocolo**.

## 1. O que está pronto para revisão
- **Peças externas:** [memorando institucional](relatorios/memorando-externo.md) · [rascunho de ofício](relatorios/oficio-eptc-rascunho.md) · [anexo de pontos](relatorios/anexo-matriz-pontos.md).
- **Para abrir a reunião:** [linha do tempo documental](relatorios/linha-do-tempo-documental.md) — uma página que mostra o que a cidade já pactuou, projetou e declarou no eixo da Três Meninas, e o que ficou parado. Boa forma de nivelar a comissão antes das decisões.
- **Técnico:** [mapa dos pontos](mapas/mapa-pontos.png) · [matriz dos pontos (8 + P9)](propostas/problemas-priorizados.md) · [avaliação das soluções](propostas/avaliacao-solucoes-iniciais.md) · [base de sinistros](dados/tratados/acidentes_resumo_distancia_pontos.csv).
- **Evidência em consolidação:** [sonda de tempos](campo/sonda-tempos-google.md) (12 rotas, dados brutos privados; agregar antes de circular) · [capturas do trânsito típico](campo/observacoes/transito-tipico/README.md) · [acompanhamento das LAIs](relatorios/pedidos-informacao-lai.md#acompanhamento).
- **Referências para a vistoria técnica:** [plano de coleta](campo/plano-coleta-campo.md) · [roteiro](campo/observacoes/roteiro-vistoria.md) · [ficha CSV](campo/observacoes/modelo-observacao-campo.csv).

## 2. Decisões da comissão (checklist)
- [x] **Lista de pontos** decidida (13/08): **P1–P8 + novo P9** (entroncamento Rua Santuário × Av. Oscar Pereira); o antigo P9 (rótula Cristiano Kraemer × Juca Batista) foi retirado.
- [x] **Grafia** "Estr. Cristiano **Kraemer**" — confirmada pela comissão.
- [x] **Peças aprovadas** (13/08): assina **Eduardo de Oliveira Horta (representante)** pela **Comissão Viária Estrada das Três Meninas**; contato **comissao.viaria@outlook.com**.
- [x] **D2 (retorno) e D3 (capacidade da Cristiano Kraemer):** **incluídas** nas peças em versão genérica (decisão 13/08).
- [ ] **P9 (Rótula da Vila Nova):** confirmar como ponto rastreado.
- [x] **Protocola:** Eduardo. **Canal:** SMAMUS (principal), com cópia à EPTC/SMMU e às Subprefeituras Centro-Sul e Glória.
- [ ] **Confirmar o encaminhamento:** protocolo baseado em sonda, sinistros e LAIs, com pedido explícito de dados e vistoria técnica da EPTC; coleta comunitária e questionário ficam em espera.

## 3. Consolidação antes da reunião de 13/8

- **Sonda:** verificar continuidade e gerar agregados por rota e horário: atraso versus
  fluxo livre, assimetria direcional no P4 e custo do retorno no P7. Declarar a janela de
  coleta e as limitações; não anexar nem publicar dados brutos da Google Routes API.
- **LAIs:** os cinco pedidos prorrogados em 22/07 (1, 4, 5, 6, 7) **estão todos respondidos**.
  **6** (13/08, zoneamento PDUS e mapa de contrapartidas viárias), **4** (14/08, quadro de
  expedientes complementares), **1** (17/08, EPTC sem sinalização aprovada para a nova
  interseção Costa Gama — processo migrado à SMMU, novo Pedido 15) e **5** (24/08, SMMU:
  sinalização da Av. Monte Cristo concluída em projeto mas implantação parcial — SMSURB parado
  desde set/2024; nó do P2 encaminhado à EPTC, manifestação pendente). **O pedido 7 já respondeu
  (10/08)**: confirma Waze desde 2019, aponta o portal ObservaMOB e traz os planos semafóricos
  oficiais de P5 e P8 — já no [anexo](relatorios/anexo-matriz-pontos.md). O **Pedido 8** (PGM) também
  respondeu (21/08) e originou os Pedidos 16 e 17.
- **Documentação da administração do Alphaville (recebida em 07/08):** já incorporada ao dossiê
  — TC integral, aditivos, **Parecer CTAAPS nº 093/2020** e **três decretos de desapropriação de
  23/12/2020**. Mudou o enquadramento: o pleito passa a ser **concluir o que a cidade pactuou,
  projetou e declarou**, não pedir obra nova. **Decisão para a comissão:** protocolar os
  **Pedidos 9 (prioritário — prazo legal das desapropriações venceu em 23/12/2025) e 10**.
- **Peças:** atualizar o memorando e o anexo somente com fatos documentados e agregados,
  mantendo o pedido de validação técnica da EPTC.

## 4. Mínimo suficiente para protocolar na EPTC
> Protocolar quando os requisitos formais abaixo estiverem cumpridos. A ausência de coleta
> física ou questionário não impede o pedido, que busca justamente a vistoria e os dados da
> autoridade competente.

- [ ] **Base indicativa consolidada:** sinistros, agregados metodologicamente descritos da sonda e respostas LAI — ou situação datada dos pedidos ainda pendentes.
- [ ] **Peças externas sem placeholders** — `make release-check` verde (memorando, ofício e anexo preenchidos).
- [x] **Quem assina/protocola** definido (Eduardo) e **canal** escolhido: **SMAMUS (principal)** + EPTC/SMMU e Subprefeituras Centro-Sul/Glória.

## 5. Depois do protocolo
1. Acompanhar a designação de canal técnico e a resposta de cada pedido LAI.
2. Compartilhar os agregados da sonda e os documentos que chegarem, quando solicitados.
3. Organizar vistoria técnica conjunta se a EPTC/SMMU a aceitar; os roteiros de campo
   servem de referência para essa etapa.

```{=latex}
\newpage
```

**COMISSÃO VIÁRIA ESTRADA DAS TRÊS MENINAS**

# Melhorias viárias no entorno de Vila Nova — síntese para diálogo com o poder público

*Documento-síntese · versão institucional · 2026*

## Apresentação
Somos uma comissão de moradores constituída para contribuir, de forma técnica e colaborativa, com a qualificação viária do entorno de Vila Nova (Zona Sul de Porto Alegre). Este documento sintetiza um diagnóstico preliminar e propõe um diálogo com a SMAMUS e a EPTC/SMMU. **Todas as vias tratadas são de jurisdição municipal.**

## O que identificamos
Em um diagnóstico preliminar, identificamos **oito pontos de atenção (estrangulamento)** de segurança e fluidez que afetam tanto os moradores quanto a comunidade do entorno (Belém Velho, Costa Gama, Cavalhada, Camaquã):

1. Rótula da Estr. das Três Meninas × Estr. Cristiano Kraemer
2. Confluência Cristiano Kraemer × Av. Belém Velho × Av. Monte Cristo
3. Acesso à Av. Vicente Monteggia (a partir de Rodrigues da Fonseca / João Salomoni)
4. Corredor da Av. Vicente Monteggia
5. Conversão da Av. João Salomoni para a Av. da Cavalhada
6. Acesso à Av. Dr. Vergara (hoje por via não pavimentada)
7. Acesso à Estr. Costa Gama no sentido bairro–centro
8. Cruzamento semaforizado Estr. Costa Gama × Estr. Afonso Lourenço Mariante

Acompanhamos ainda um **nono ponto preliminar** — o entroncamento da Rua Santuário com a Av. Oscar Pereira, onde se formam filas para a conversão à esquerda em dias de maior fluxo — e **duas demandas adicionais de continuidade viária**: um **retorno seguro** no eixo da Estr. das Três Meninas e a **avaliação de capacidade** da Estr. Cristiano Kraemer. Ambas são apresentadas no anexo, como pontos a validar em vistoria.

## Por que importa para a cidade
- **Segurança viária.** A análise preliminar dos sinistros (Dados Abertos POA, associação por proximidade) aponta **gravidade relevante**, com destaque para o **corredor da Av. Vicente Monteggia** — que registra feridos graves e vítimas fatais — e **envolvimento recorrente de motociclistas**. *(Indicadores preliminares, a validar em vistoria conjunta.)*
- **Fluidez.** Uma sonda própria de tempos de viagem (Google Routes API, série iniciada em jul/2026) indica, no pico, **atraso de ~1,3–1,4× no corredor da Av. Vicente Monteggia** e um custo de **≈2,0× no tempo do acesso legal à Estr. Costa Gama (P7)** frente ao movimento direto. *(Indicadores próprios, indicativos; a validar com contagens da EPTC.)*
- **Alinhamento com as políticas municipais.** As demandas convergem com o **Plano de Segurança Viária Sustentável (PSVS)** e a meta da Visão Zero, e com a diretriz de **redução do tempo de deslocamento** do novo marco urbanístico (PDUS/LUOS, sancionado em 14/07/2026, com vigência 180 dias após a publicação).

## Uma oportunidade de sinergia
O ponto 2 conversa diretamente com o **projeto da Prefeitura para a Av. Monte Cristo** (qualificação viária do PSVS, cujo trecho se encerra na Estr. Cristiano Kraemer). Acreditamos que parte das melhorias pode ser **integrada a iniciativas já em curso** no mesmo eixo, com ganho de eficiência **e sem prejuízo da segurança e dos modos vulneráveis**.

Além disso, a documentação oficial do licenciamento do empreendimento no eixo da Estr. das Três Meninas — reunida em jul–ago/2026 a partir de respostas aos nossos pedidos de acesso à informação e de documentos disponibilizados pela administração do empreendimento — mostra que **boa parte do que aqui se pede já foi pactuada, projetada e aprovada pelo próprio Município, sem conclusão**:

- há um **Plano Funcional aprovado** para a Estr. das Três Meninas e um **Termo de Compromisso sem prazo de validade** (a cláusula que o limitava a 30 meses foi suprimida por aditivo em 2012);
- o **Parecer CTAAPS nº 093/2020**, elaborado pelo Município, registra que **não foram implantadas** as segundas fases das interseções da Estr. das Três Meninas com a **Estr. Cristiano Kraemer (ponto 1)**, com a **Estr. Kanazawa e a R. Florestan Fernandes (ponto 6)** e com a **Estr. Costa Gama (ponto 7)**;
- **três decretos de 23/12/2020** declararam de utilidade pública as áreas necessárias ao alargamento, inclusive a da **alça de ligação com a Estr. Costa Gama** (Decreto nº 20.860/2020);
- o **projeto geométrico** dessa conexão, aprovado na CTAAPS em 2013, **perdeu a validade** (Decreto nº 20.659/2020) — e a própria **EPTC já recomendava, em 2020, revisar os projetos** em razão do tempo decorrido.

Ou seja: para vários pontos é possível **partir de soluções que a própria cidade já projetou e cujas áreas já declarou de utilidade pública** — a serem revalidadas, atualizadas às condições atuais e concluídas, não estudadas do zero. O saldo das obrigações e a situação atual das intervenções e desapropriações estão sob apuração junto à **Procuradoria-Geral do Município**.

## Como pretendemos colaborar
Adotamos o princípio de **diagnóstico antes da solução** e priorizamos **medidas faseadas, começando pelas de menor custo** (sinalização, ajuste de tempos semafóricos, qualificação de rotas). Nossa intenção é **somar à atuação técnica da SMAMUS e da EPTC/SMMU**, não substituí-la.

## O que solicitamos
1. **Vistoria técnica conjunta** dos oito pontos (e do ponto preliminar);
2. **Disponibilização dos dados disponíveis** (tempos semafóricos, sinistros georreferenciados, contagens), conforme as possibilidades da EPTC;
3. **Acesso aos desenhos vigentes e ao status de implantação** do Plano Funcional da Estr. das Três Meninas, inclusive a conexão com a Costa Gama e os projetos complementares, com **avaliação de revalidação/atualização** das soluções já projetadas;
4. **Abertura de um canal de diálogo** com a SMAMUS e a EPTC/SMMU (com apoio das Subprefeituras Centro-Sul e Glória);
5. **Implantação de medidas rápidas de baixo custo** nos pontos em que a vistoria e os dados confirmarem evidência suficiente.

---
*Anexos: matriz dos pontos críticos e diagnóstico detalhado.*

**Comissão Viária Estrada das Três Meninas** — comissao.viaria@outlook.com

```{=latex}
\newpage
```

# Anexo — Pontos de atenção mapeados (síntese para vistoria)

> Anexo ao [ofício à SMAMUS (c/c EPTC/SMMU)](relatorios/oficio-eptc-rascunho.md) e ao [memorando](relatorios/memorando-externo.md). **Diagnóstico preliminar da comissão**, para orientar **vistoria técnica conjunta** — não é laudo. Os dados de sinistros são **associação preliminar por proximidade** (Dados Abertos POA), **não prova de causa**. Solicita-se, para cada ponto, **vistoria e validação técnica da SMAMUS/EPTC/SMMU**.

![Mapa dos pontos P1–P9 (localização aproximada, a validar tecnicamente)](mapas/mapa-pontos.png)

| Ponto | Localização | Problema relatado (a verificar) | Indício preliminar | A vistoriar / coletar |
|-------|-------------|----------------------------------|--------------------|------------------------|
| **P1** | Rótula Estr. Três Meninas × Estr. Cristiano Kraemer | Estrangulamento e conflito na rótula | ~29 sinistros (4 graves) + adequação prevista no Plano Funcional; **Parecer CTAAPS 093/2020: implantada só em 1ª etapa, projeto da 2ª fase não aprovado e falta o projeto de drenagem da adequação** | Aprovação do projeto da 2ª fase e da drenagem; geometria executada, velocidade e contagem direcional |
| **P2** | Confluência Cristiano Kraemer × Av. Belém Velho × Av. Monte Cristo | Conflito na confluência de três vias | ~58 sinistros (7 graves; motos); **projeto de sinalização da Av. Monte Cristo concluído, implantação apenas parcial** — baias de ônibus paradas desde set/2024 (DCVU-SMSURB); **o nó específico do P2 tem projeto próprio, elaborado pela GPTC-EPTC**, com manifestação da EPTC ainda pendente (resposta ao Pedido 5, 24/08/2026) | Movimentos direcionais; **acompanhar a manifestação da EPTC sobre o projeto do nó** (Pedido 5) |
| **P3** | Acesso à Av. Vicente Monteggia (Rodrigues da Fonseca / João Salomoni) | Dificuldade/conflito de acesso | ~44 sinistros (4 graves; motos) | Brechas de entrada, prioridade, contagem |
| **P4** | Corredor da Av. Vicente Monteggia (≈2,9 km) | Sobrecarga e gravidade no corredor | Sinistros graves e **2 fatais** no corredor; trecho mais crítico entre Estr. João Vedana e Estr. João Passuelo (~67 sinistros, 9 graves, 1 fatal); **tempos de viagem (sonda): o corredor mais lento, atraso ~1,3–1,4× no pico (p85 até ~1,9×)** | Contagem por trecho; velocidades; **vistoriar trechos prioritários** |
| **P5** | Conversão Av. João Salomoni → Av. da Cavalhada | Conversão problemática | Sinistralidade no entorno da Cavalhada; **plano semafórico obtido via LAI: 13 planos por horário, ciclos de 55 a 130 s, 2 estágios** (Informação Técnica EPTC nº 40664080) | Volume da conversão, travessia, ônibus; **confirmar se o movimento relatado tem fase dedicada** |
| **P6** | Acesso à Av. Dr. Vergara (via Florestan Fernandes / Estr. Kanazawa) | Rota precária (trecho não pavimentado) | Precariedade física + estudos dos dois acessos exigidos em 2013; **Parecer CTAAPS 093/2020: projetos de Kanazawa e Florestan Fernandes aprovados e "nenhuma foi implantada"**; **Decreto nº 20.859/2020 declarou a desapropriação** na esquina com a Kanazawa (1.806,73 m²) | Efetivação da desapropriação e implantação dos projetos aprovados; largura, drenagem, calçadas e função de rede |
| **P7** | Acesso à Estr. Costa Gama, sentido bairro–centro | Sem conversão à esquerda; retorno distante | ~18 sinistros; **projeto geométrico aprovado na CTAAPS/2013 obtido via LAI — 1ª etapa + solução definitiva com conector a oeste — hoje caducado** (Dec. 20.659/2020); **a "alça de ligação" está nomeada no Decreto nº 20.860/2020, que declarou a desapropriação da área (1.334,07 m²)**; **2ª fase nunca implantada** (Parecer CTAAPS 093/2020); **sinalização viária nunca aprovada** para a nova interseção — confirmado pela EPTC, que orientou novo pedido à SMMU (Pedido 1→15); **sonda: a rota legal (com o retorno) custa ≈2,0× o tempo e 1,6× a distância do movimento direto** | Revalidar/atualizar o projeto (agora na **SMMU**); **confirmar o status da desapropriação** (prazo legal de 5 anos a partir de 23/12/2020); tempo do retorno e volume |
| **P8** | Cruzamento semaforizado Estr. Costa Gama × Estr. Afonso Lourenço Mariante | Filas no pico | ~36 sinistros (4 graves; motos); **sonda: atraso ~1,3× no pico (sentido Mariante→Costa Gama)**; **plano semafórico obtido via LAI: 15 planos por horário, ciclos de 55 a 160 s, 3 estágios** (Informação Técnica EPTC nº 40691572) | Fila residual e volume por aproximação, agora com os tempos de verde oficiais como referência |
| **P9** *(preliminar)* | Entroncamento Rua Santuário × Av. Oscar Pereira | Fila para a conversão à esquerda na Av. Oscar Pereira em dias de maior fluxo | ~17 sinistros (2 graves; 6 motos) por proximidade (≤100 m); **novo ponto (reunião 13/08/2026), georreferenciado por pin** | Volume e brechas para a conversão à esquerda no pico; geometria, prioridade e travessia; contagem direcional |

*Observação: dados de sinistros referentes a recortes por proximidade da malha viária (≤100 m em interseções; corredor inteiro em P4 — escalas não comparáveis entre si, razão pela qual P4 é apresentado por trecho). Pontos sem número expressivo de sinistros (ex.: P6) sustentam-se por outras evidências (precariedade física, função de rede). Em interseções sobre vias de tráfego intenso, parte das ocorrências no raio de 100 m pode pertencer ao corredor e não ao nó — é uma das validações solicitadas à EPTC. Contato: Comissão Viária Estrada das Três Meninas — comissao.viaria@outlook.com.*

**Demandas adicionais de continuidade viária (preliminares, a validar).** Além dos pontos acima, a comissão registra duas demandas de continuidade, apresentadas para avaliação técnica:

- **D2 — Retorno seguro no eixo da Estr. das Três Meninas.** Avaliar a implantação de um retorno que reduza percursos e manobras de risco — em linha, inclusive, com os **retornos no canteiro central** já previstos, em tese, no projeto do corredor. A validar quanto a localização, volume e segurança.
- **D3 — Avaliação de capacidade da Estr. Cristiano Kraemer** (trecho entre a rótula da Vila Nova e a Estr. das Três Meninas). Verificar, com contagens da EPTC, se a seção atual comporta a demanda — inclusive a decorrente dos **empreendimentos em licenciamento no eixo** —, dimensionando eventual ampliação de capacidade.

**Evidência documental — obrigações pactuadas e projetos parados.** Documentação oficial obtida em jul–ago/2026 (respostas LAI e documentos repassados pela administração do empreendimento) mostra que boa parte do que se pede **já foi pactuada, projetada e aprovada** pelo Município, sem conclusão: o Termo de Compromisso do licenciamento **não tem prazo de validade** (a cláusula de 30 meses foi suprimida por aditivo em 2012); o **Parecer CTAAPS nº 093/2020** registra que as **2ªs fases das interseções com a Cristiano Kraemer (P1), a Kanazawa e a Florestan Fernandes (P6) e a Costa Gama (P7) não foram implantadas**; e **três decretos de 23/12/2020** declararam de utilidade pública as áreas necessárias — inclusive a da **"alça de ligação" do P7** (Decreto nº 20.860/2020). A própria **EPTC recomendou, em 2020, revisar os projetos** em razão do tempo decorrido. Cronologia resumida em [linha do tempo documental](relatorios/linha-do-tempo-documental.md); detalhamento e fontes em [projetos viários documentados](relatorios/projetos-viarios-ja-aprovados.md).

**Evidência de fluidez — sonda própria de tempos de viagem** (Google Routes API, série iniciada em 04/07/2026, medindo 12 rotas nos picos e fins de semana): confirma o **corredor da Av. Vicente Monteggia (P4)** como o mais lento e mede o **custo do retorno distante do P7** — a rota legalmente disponível custa ≈2,0× o tempo e 1,6× a distância do movimento direto permitido. São **indicadores próprios, indicativos** — não substituem contagens e medições da EPTC/SMMU. Agregados em [dados/tratados/sonda_tempos_resumo.md](dados/tratados/sonda_tempos_resumo.md).
