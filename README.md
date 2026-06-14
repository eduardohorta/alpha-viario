# Projeto Viário — Alphaville Porto Alegre (Vila Nova / Zona Sul)

Projeto comunitário para propor melhorias viárias no entorno do Alphaville Porto Alegre (Estr. das Três Meninas, bairro **Vila Nova**), com qualidade técnica para apresentação à **Prefeitura de Porto Alegre (EPTC/SMMU)**. **Todas as vias são municipais.**

## Status atual — 2026-06-14
**Fase 0 madura.** Concluídos: revisão documental (Etapa 1), base de sinistros (com P4 segmentado), matriz dos pontos, avaliação das soluções, peças externas e instrumentos de coleta. **5 rodadas de revisão CODEX** incorporadas. **Governança automatizada:** cadastro canônico de pontos, `public-check`, build do pacote e manifesto de dados (ver [Cadastro e governança](#cadastro-e-governança)). **Gatekeeper para ir à EPTC: coleta de campo.**

**Pendências abertas:** ver [PENDENCIAS.md](PENDENCIAS.md).

## Fluxo de trabalho
**CLAUDE conduz** (estrutura, pesquisa, redação técnica, decisões). **CODEX revisa e complementa** quando acionado. As rodadas de revisão são mantidas **fora do repositório público** (revisões internas). Ver §8 do [plano-de-trabalho.md](plano-de-trabalho.md).

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
- [propostas/problemas-priorizados.md](propostas/problemas-priorizados.md) — **matriz dos pontos — 8 + P9 preliminar (v4)**
- [propostas/avaliacao-solucoes-iniciais.md](propostas/avaliacao-solucoes-iniciais.md) — avaliação das 3 soluções + escada de intervenção

**Relatórios e peças**
- [relatorios/revisao-documental.md](relatorios/revisao-documental.md) — enquadramento legal/institucional
- [relatorios/memorando-1pagina.md](relatorios/memorando-1pagina.md) — memorando (uso interno, rastreável)
- [relatorios/memorando-externo.md](relatorios/memorando-externo.md) — **versão institucional limpa**
- [relatorios/oficio-eptc-rascunho.md](relatorios/oficio-eptc-rascunho.md) — **rascunho de ofício à EPTC**
- [relatorios/anexo-matriz-pontos.md](relatorios/anexo-matriz-pontos.md) — **anexo externo (1 linha por ponto)**
- [relatorios/guia-validacao-comissao.md](relatorios/guia-validacao-comissao.md) — **pauta de validação + kickoff de campo**
- [relatorios/projetos-viarios-ja-aprovados.md](relatorios/projetos-viarios-ja-aprovados.md) — **projetos já aprovados no eixo Três Meninas (Plano Funcional)**
- [relatorios/matriz-publica-status-plano-funcional.md](relatorios/matriz-publica-status-plano-funcional.md) — **matriz de status (a preencher com os desenhos)**

**Campo e consulta**
- [campo/plano-evidencia-leve.md](campo/plano-evidencia-leve.md) — **plano de coleta comunitária (recomendado)** · [plano técnico completo](campo/plano-coleta-campo.md)
- [campo/observacoes/roteiro-vistoria.md](campo/observacoes/roteiro-vistoria.md) — o que medir por ponto
- [campo/observacoes/modelo-observacao-campo.csv](campo/observacoes/modelo-observacao-campo.csv) — planilha de campo
- [campo/observacoes/inventario-evidencias.csv](campo/observacoes/inventario-evidencias.csv) — **inventário central de evidências** (rastreabilidade + público/interno)
- [campo/observacoes/ficha-drenagem.csv](campo/observacoes/ficha-drenagem.csv) — ficha de alagamento/drenagem
- [consultas/moradores/questionario-curto.md](consultas/moradores/questionario-curto.md) — **questionário curto (~2 min, porta de entrada)** · [completo](consultas/moradores/questionario-base.md)
- [consultas/moradores/aviso-privacidade.md](consultas/moradores/aviso-privacidade.md) — **aviso de privacidade (LGPD)** — preencher responsável/retenção antes de circular
- [consultas/registro-demandas-comunitarias.md](consultas/registro-demandas-comunitarias.md) — demandas estruturadas

**Dados (sinistros)**
- [dados/tratados/acidentes_resumo_distancia_pontos.csv](dados/tratados/acidentes_resumo_distancia_pontos.csv) — **resumo refinado por ponto**
- [dados/tratados/acidentes_metodologia.md](dados/tratados/acidentes_metodologia.md) · [revisão manual](dados/tratados/acidentes_revisao_manual_notas.md)
- [scripts/processar_sinistros_distancia.py](scripts/processar_sinistros_distancia.py)
- [Segmentação do P4](dados/tratados/acidentes_p4_segmentos.csv) · [hot spots](dados/tratados/acidentes_p4_hotspots_250m.csv) · [script](scripts/segmentar_p4_monteggia.py)
- [Georreferenciamento de referências](dados/tratados/georreferenciamento_referencias_demandas.md) (P9/D1–D4/P7 — preliminar, a validar em campo)

**Cadastro e governança**
- [dados/pontos.csv](dados/pontos.csv) — **cadastro canônico dos pontos** (fonte única: ID, nome, status, coordenadas, confiança, aliases). As listas dos questionários são geradas dele (`make` / `scripts/pontos.py sync`).
- [dados/tratados/pontos.geojson](dados/tratados/pontos.geojson) — **mapa dos pontos** (gerado do cadastro)
- [dados/brutos/manifest.json](dados/brutos/manifest.json) — **manifesto dos insumos** (URL, SHA-256, licença, janela temporal). Reprodução: `make data`.
- [scripts/public_check.py](scripts/public_check.py) — **porteiro de publicação** (`make check`): links quebrados, vazamento de áreas privadas, placeholders, pontos inconsistentes.
- [scripts/build_pacote.py](scripts/build_pacote.py) — **gera o pacote de reunião** a partir das fontes (`make pacote`).
- [pacote-reuniao.md](pacote-reuniao.md) — **pacote de reunião (gerado)** · [PDF](pacote-reuniao.pdf)
- [Makefile](Makefile) — `make all` · `make check` · `make test` · `make data`

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

## Licença
Licenciamento duplo — **código** (`scripts/`, `tests/`, `Makefile`, `.github/`) sob **MIT**; **conteúdo** (textos, questionários, dados próprios) sob **CC BY 4.0**. Dados de terceiros mantêm suas licenças. Ver [LICENSE](LICENSE).
