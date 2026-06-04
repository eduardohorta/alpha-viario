# Projeto Viário — Alphaville Porto Alegre (Vila Nova / Zona Sul)

Projeto comunitário para propor melhorias viárias no entorno do Alphaville Porto Alegre (Estr. das Três Meninas, bairro **Vila Nova**), com qualidade técnica para apresentação à **Prefeitura de Porto Alegre (EPTC/SMMU)**. **Todas as vias são municipais.**

## Status atual — 2026-06-04
**Fase 0 madura.** Concluídos: revisão documental (Etapa 1), base de sinistros (com P4 segmentado), matriz dos pontos, avaliação das soluções, peças externas e instrumentos de coleta. **3 rodadas de revisão CODEX** incorporadas. **Gatekeeper para ir à EPTC: coleta de campo.**

**Pendências abertas:** ver [PENDENCIAS.md](PENDENCIAS.md).

## Fluxo de trabalho
**CLAUDE conduz** (estrutura, pesquisa, redação técnica, decisões). **CODEX revisa e complementa** quando acionado. Rodadas em [`revisoes/`](revisoes/) — briefing → resposta. Ver §8 do [plano-de-trabalho.md](plano-de-trabalho.md).

## Os pontos de estrangulamento (8 + P9 preliminar)
1. **P1** — Rótula Estr. Três Meninas × Estr. Cristiano Kraemer
2. **P2** — Trevo Cristiano Kraemer × Av. Belém Velho × Av. Monte Cristo *(sinergia com projeto PSVS da Monte Cristo)*
3. **P3** — Acesso à Av. Vicente Monteggia (Rodrigues da Fonseca / João Salomoni)
4. **P4** — Fluxo na Av. Vicente Monteggia *(prioridade de segurança — corredor)*
5. **P5** — Conversão João Salomoni → Av. da Cavalhada *(investigar)*
6. **P6** — Acesso à Av. Dr. Vergara (rota de chão batido Florestan/Kanazawa)
7. **P7** — Acesso à Estr. Costa Gama, sem conversão à esquerda
8. **P8** — Semáforo Estr. Costa Gama × Estr. Afonso Lourenço Mariante
9. **P9** *(preliminar)* — Rótula da Vila Nova (Estr. Cristiano Kraemer), da demanda D4

## Índice de documentos

**Insumos brutos**
- [sugs.md](sugs.md) — relato original (8 pontos + 3 propostas)
- [starting-point.md](starting-point.md) — pedido inicial
- [consultas/contribuicoes-comunitarias-publico.md](consultas/contribuicoes-comunitarias-publico.md) — contribuições da comunidade (versão neutra). *Inbox bruto mantido em `interno/`.*

**Plano e propostas**
- [plano-de-trabalho.md](plano-de-trabalho.md) — espinha dorsal (etapas 0–9)
- [propostas/problemas-priorizados.md](propostas/problemas-priorizados.md) — **matriz dos 8 pontos (v3)**
- [propostas/avaliacao-solucoes-iniciais.md](propostas/avaliacao-solucoes-iniciais.md) — avaliação das 3 soluções + escada de intervenção

**Relatórios e peças**
- [relatorios/revisao-documental.md](relatorios/revisao-documental.md) — enquadramento legal/institucional
- [relatorios/memorando-1pagina.md](relatorios/memorando-1pagina.md) — memorando (uso interno, rastreável)
- [relatorios/memorando-externo.md](relatorios/memorando-externo.md) — **versão institucional limpa**
- [relatorios/oficio-eptc-rascunho.md](relatorios/oficio-eptc-rascunho.md) — **rascunho de ofício à EPTC**
- [relatorios/anexo-matriz-pontos.md](relatorios/anexo-matriz-pontos.md) — **anexo externo (1 linha por ponto)**
- [relatorios/guia-validacao-comissao.md](relatorios/guia-validacao-comissao.md) — **pauta de validação + kickoff de campo**
- [relatorios/projetos-viarios-ja-aprovados.md](relatorios/projetos-viarios-ja-aprovados.md) — **projetos já aprovados no eixo Três Meninas (Plano Funcional)**

**Campo e consulta**
- [campo/plano-coleta-campo.md](campo/plano-coleta-campo.md) — **plano de coleta (clusters/horários)**
- [campo/observacoes/roteiro-vistoria.md](campo/observacoes/roteiro-vistoria.md) — o que medir por ponto
- [campo/observacoes/modelo-observacao-campo.csv](campo/observacoes/modelo-observacao-campo.csv) — planilha de campo
- [consultas/moradores/questionario-base.md](consultas/moradores/questionario-base.md) — questionário
- [consultas/registro-demandas-comunitarias.md](consultas/registro-demandas-comunitarias.md) — demandas estruturadas

**Dados (sinistros)**
- [dados/tratados/acidentes_resumo_distancia_pontos.csv](dados/tratados/acidentes_resumo_distancia_pontos.csv) — **resumo refinado por ponto**
- [dados/tratados/acidentes_metodologia.md](dados/tratados/acidentes_metodologia.md) · [revisão manual](dados/tratados/acidentes_revisao_manual_notas.md)
- [scripts/processar_sinistros_distancia.py](scripts/processar_sinistros_distancia.py)
- [Segmentação do P4](dados/tratados/acidentes_p4_segmentos.csv) · [hot spots](dados/tratados/acidentes_p4_hotspots_250m.csv) · [script](scripts/segmentar_p4_monteggia.py)

**Revisões técnicas (CODEX)**
- Mantidas fora deste repositório público (bastidores de revisão interna).

## Notas importantes
- **Dados de sinistros = associação preliminar por distância, não prova causal.** Exigem validação de campo.
- **Grafia:** "Estr. Cristiano **Kraemer**" (confirmar na base SMAMUS).
- **Marco urbanístico:** PDUS/LUOS **aprovados pela Câmara em 2026**; sanção/publicação e transição **a confirmar**.
- A obra asfáltica da Cristiano Kraemer é **SMSUrb (pavimento)**, ≠ projeto PSVS da Monte Cristo.
- **Privacidade:** nomes de moradores anonimizados (Morador A/B). Revisões internas (CODEX) e a base bruta de sinistros (~15 MB) não são versionadas.
- **Escopo (contribuição comunitária):** além de circulação/segurança, investigar **drenagem/alagamento**; os impactos alcançam também o Terraville e demais usuários da região.

## Próximos passos
1. **Validar o pacote com a comissão** ([guia](relatorios/guia-validacao-comissao.md)) e **iniciar a coleta de campo** ([plano](campo/plano-coleta-campo.md)) — destrava a ida à EPTC. *(decisão atual: validação interna + campo antes de protocolar)*
2. **Validar em campo os segmentos P4-S06/S01/S04** (hot spots do corredor).
3. **Pendências de gabinete:** zoneamento de Vila Nova no PDUS (Anexo 5 / Regramento Construtivo); status atual do projeto da Monte Cristo.
