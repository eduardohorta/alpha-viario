# Avaliação preliminar das soluções propostas

> **Status:** versão 2 (condução: CLAUDE; incorpora a revisão CODEX Rodada 01 — [revisoes/codex-01-resposta.md](../revisoes/codex-01-resposta.md)).
> As três soluções do [sugs.md](../sugs.md) são **hipóteses**, não pontos de partida. Princípio endurecido pela revisão: **cada intervenção precisa provar que resolve um problema público identificado, melhora a segurança e não apenas desloca o congestionamento.**

## Reenquadramento à luz dos dados

Os sinistros (refinados por **associação à distância** na Rodada 02) reforçam o eixo de **segurança viária (PSVS/Visão Zero)**, com a fluidez como benefício secundário. **Motociclistas têm envolvimento relevante, sobretudo em P4, P2, P3 e P8.** A gravidade mais robusta está no **corredor da Av. Vicente Monteggia (P4)** — inclusive com fatais (a segmentar por trecho). Em **P5** há sinistralidade no entorno, mas a fatalidade aparece só no contexto ampliado e **não é atribuível à conversão** sem validação de campo. *(Associação por distância ≠ prova causal — ver [resumo refinado](../dados/tratados/acidentes_resumo_distancia_pontos.csv).)*

## Escada de intervenção (revisada)

Do mais leve/barato ao mais complexo/caro. A pavimentação deixou de ser "sempre o mais simples":

| Nível | Categoria | Custo | Desapropriação |
|------|-----------|-------|----------------|
| **—** | **Sem obra imediata:** diagnóstico / monitoramento / **fiscalização** / manutenção | mínimo | nenhuma |
| **0A** | Sinalização / manutenção / fiscalização | muito baixo | nenhuma |
| **0B** | Ajuste semafórico (ciclo/split/coordenação) e canalização leve | baixo | nenhuma |
| **1** | Pequenas obras localizadas (baia, refúgio, raio de giro) | baixo | baixa |
| **2** | Pavimentação / **qualificação de rota alternativa** | médio-baixo | baixa |
| **3** | Redesenho de interseção / rótula | médio-alto | média |
| **4** | Corredor / faixa reversível (**condicionada**) | alto | média (alargar ~50%) |

**Liderar pelos níveis "—" a 0B** gera credibilidade e vitórias rápidas, conversa com a restrição "Prefeitura sem recursos" e é o terreno natural da EPTC.

> **"Sem obra imediata" é uma resposta legítima** (revisão CODEX): em P1, P2, P4 e P8 a melhor primeira providência pode ser diagnóstico/fiscalização/manutenção — a comissão formula um **problema público**, não "procura obra".

## Proposta 1 — Faixa central reversível (corredor) → **hipótese condicionada**
- **Precedente local:** Av. Oscar Pereira, Av. Coronel Marcos (POA já opera reversíveis).
- **Rebaixamento (revisão):** deixa de ser candidata automática do P4. A Av. Vicente Monteggia é **segmentada** (1–3 faixas, vários sentidos únicos) e tem **alta sinistralidade de motos** — tratá-la como solução de corredor antes de medir é arriscado.
- **Critérios mínimos para manter a hipótese:**
  1. assimetria direcional forte em ao menos dois picos;
  2. seção viária contínua e compatível;
  3. plano de controle de faixa + semáforos + sinalização aérea + fiscalização;
  4. tratamento explícito de pedestres, ciclistas e transporte coletivo;
  5. análise de conversões suprimidas e retornos substitutos.
- **Efeito colateral esperado (a avaliar):** risco de colisão frontal; supressão de conversões à esquerda; concentração de retornos; piora de travessias; custo operacional diário.
- **Onde se aplica:** P4 — **apenas** se os 5 critérios forem atendidos.

## Proposta 2 — Redesenho de interseção (rótula como **uma** alternativa)
- **Reformulação (revisão):** trocar "rótula maior" por **"estudo de redesenho da interseção, incluindo rótula compacta/moderna, canalização, semaforização ou microintervenções"**. Rótula moderna ≠ maior diâmetro.
- **Base técnica:** rótulas modernas reduzem pontos de conflito e velocidade (bom para segurança), mas **saturam** em volumes altos/desbalanceados e **pioram travessias** se mal desenhadas; "maior diâmetro" implica desapropriação na Zona Sul.
- **Família a considerar:** rótula compacta, mini-rótula, turbo-rótula (menos área), além de canalização/semáforo.
- **Cuidados:** travessias recuadas e acessíveis (NBR 9050); geometria para ônibus/caminhão.
- **Efeito colateral esperado (a avaliar):** desapropriação; oposição comunitária; incompatibilidade com ramo dominante, ônibus ou pedestres.
- **Onde se aplica:** P1, P2 (articulado com a requalificação da Monte Cristo/PSVS), P3; possivelmente P8 **apenas após** o diagnóstico semafórico.

## Proposta 3 — Qualificação de rota alternativa (não "apenas pavimentar")
- **Reformulação (revisão):** P6 deixa de ser "pavimentação" e passa a **"rota alternativa com pacote mínimo de segurança"**: pavimento + drenagem + seção segura + velocidade baixa + pedestres + controle de tráfego de passagem.
- **Vantagem:** menor custo e boa relação custo-benefício; usa a redundância da malha.
- **Cuidados (revisão + OSM):** Estr. Kanazawa é `dirt`; R. Florestan Fernandes tem `smoothness=very_bad` e `sidewalk=no` → pavimentar sem calçada/drenagem **induz tráfego de passagem** em via residencial despreparada; possível restrição ambiental/fundiária.
- **Efeito colateral esperado (a avaliar):** tráfego de passagem em rua local; impacto em moradias lindeiras; drenagem; indução de demanda.
- **Onde se aplica:** P6 (principal); P7 (alternativa).

## "Efeito colateral esperado" — campo obrigatório
Toda solução candidata, antes de virar proposta, deve preencher: congestionamento deslocado para onde · conversões suprimidas · impacto em pedestres · impacto em ônibus · impacto em vias locais · risco de aumento de velocidade · necessidade de fiscalização · necessidade de manutenção.

## Matriz pontos × resposta (revisada)

| Ponto | Sem obra / monitorar | Operacional (0A/0B) | Qualif. rota (2) | Redesenho/rótula (3) | Faixa reversível (4) |
|-------|:--:|:--:|:--:|:--:|:--:|
| P1 — Rótula 3 Meninas × C. Kraemer | ◐ | | | ★ | |
| P2 — Trevo C. Kraemer × Belém Velho × Monte Cristo | ◐ | | | ★ * | |
| P3 — Acesso Vicente Monteggia | | ○ | | ★ | |
| P4 — Fluxo Av. Vicente Monteggia ⚠️ | ◐ | ○ | | | ⚠ cond. |
| P5 — Conversão João Salomoni → Cavalhada ⚠️ | | ★ | | | |
| P6 — Rota Florestan/Kanazawa → Dr. Vergara | | | ★ | | |
| P7 — Acesso Costa Gama (sem conversão à esquerda) | | ★ | ○ | | |
| P8 — Semáforo Costa Gama × A. L. Mariante | ◐ | ★ | | ○ | |

★ principal · ○ alternativa · ◐ resposta inicial possível (diagnóstico/fiscalização/manutenção) · ⚠ hipótese condicionada · \* articular com a requalificação PSVS da Av. Monte Cristo · ⚠️ prioridade de segurança (P4, P5).

## Benefício público além do condomínio
Para cada proposta, registrar o ganho para **toda a cidade** (não só o Alphaville): segurança em via municipal, redução de sinistros com motos, melhoria do transporte coletivo, acesso para moradores do entorno, drenagem/manutenção, travessias mais seguras. É o que torna a demanda defensável perante a EPTC/SMAMUS.

## Ressalva
Mapeamento preliminar, baseado em relato (sugs.md), triagem de sinistros e checagem OSM. **Geometria real ainda não confirmada.** Validar com imagem aérea/base SMAMUS, vistoria e contagens antes de virar proposta.

## Rodada 01 — encerrada
Revisão CODEX incorporada (separação problema/causa/solução; rebaixamento da faixa reversível; reformulação de P6/P7/P8; modos vulneráveis obrigatórios; "sem obra" como alternativa; efeito colateral obrigatório; uso da triagem de sinistros como orientação).
