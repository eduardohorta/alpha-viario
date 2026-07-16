# Projeto Viário — Alphaville Porto Alegre (Vila Nova / Zona Sul)

Projeto comunitário para propor melhorias viárias no entorno do Alphaville Porto Alegre (Estr. das Três Meninas, bairro **Vila Nova**), com qualidade técnica para apresentação à **Prefeitura de Porto Alegre (EPTC/SMMU)**. **Todas as vias são municipais.**

## Status atual — 2026-07-16
**Fase 0 madura.** Concluídos: revisão documental (Etapa 1), leitura dos expedientes administrativos do Alphaville, base de sinistros (com P4 segmentado), matriz dos pontos, avaliação das soluções, peças externas e instrumentos de coleta. Os expedientes confirmam o Plano Funcional, obrigações para o eixo Três Meninas e execução parcial; **desenhos vigentes e status atual ainda dependem de confirmação municipal**. Os pedidos LAI 1–7 foram protocolados em 10/07/2026 e aguardam resposta. A [sonda de tempos](campo/sonda-tempos-google.md) é executada por serviços Google Cloud e encaminha seus registros ao repositório privado `alpha-viario-sonda`; ela forma, com os sinistros e as LAIs, a evidência prévia deste ciclo. **Não há mobilização para coleta física ou questionário; ambos ficam em espera e não bloqueiam o protocolo.** O pedido à EPTC é justamente de dados e vistoria técnica. **Governança automatizada:** cadastro canônico de pontos, `public-check`, build do pacote e manifesto de dados (ver [Cadastro e governança](#cadastro-e-governança)).

**Ordem e datas:** [ROTEIRO.md](ROTEIRO.md) — caminho crítico, trilhas paralelas e janelas de calendário (LOA 2027, PDUS). **Pendências abertas:** [PENDENCIAS.md](PENDENCIAS.md). **Antes de circular/protocolar:** [LIBERACAO.md](LIBERACAO.md) (+ `make release-check`).

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
- [ROTEIRO.md](ROTEIRO.md) — **caminho crítico, trilhas paralelas e datas-alvo (jul–out 2026)**
- [plano-de-trabalho.md](plano-de-trabalho.md) — plano fundador (histórico; etapas 0–9)
- [propostas/problemas-priorizados.md](propostas/problemas-priorizados.md) — **matriz dos pontos — 8 + P9 preliminar (v4)**
- [propostas/avaliacao-solucoes-iniciais.md](propostas/avaliacao-solucoes-iniciais.md) — avaliação das 3 soluções + escada de intervenção

**Relatórios e peças**
- [relatorios/revisao-documental.md](relatorios/revisao-documental.md) — enquadramento legal/institucional
- [relatorios/memorando-1pagina.md](relatorios/memorando-1pagina.md) — memorando (uso interno, rastreável)
- [relatorios/memorando-externo.md](relatorios/memorando-externo.md) — **versão institucional limpa**
- [relatorios/oficio-eptc-rascunho.md](relatorios/oficio-eptc-rascunho.md) — **rascunho de ofício à EPTC**
- [relatorios/anexo-matriz-pontos.md](relatorios/anexo-matriz-pontos.md) — **anexo externo (1 linha por ponto)**
- [relatorios/guia-validacao-comissao.md](relatorios/guia-validacao-comissao.md) — **pauta de validação e encaminhamento do protocolo**
- [relatorios/projetos-viarios-ja-aprovados.md](relatorios/projetos-viarios-ja-aprovados.md) — **evidência administrativa, obrigações e execução parcial no eixo Três Meninas**
- [relatorios/matriz-publica-status-plano-funcional.md](relatorios/matriz-publica-status-plano-funcional.md) — **matriz de previsão documental × execução × verificação atual**
- [relatorios/pedidos-informacao-lai.md](relatorios/pedidos-informacao-lai.md) — **pedidos LAI prontos para protocolo (trilha independente do pleito)**

**Sonda e instrumentos de referência**
- [campo/plano-evidencia-leve.md](campo/plano-evidencia-leve.md) — referência de contingência para mobilização futura ou vistoria técnica · [plano técnico completo](campo/plano-coleta-campo.md)
- [campo/sonda-tempos-google.md](campo/sonda-tempos-google.md) — **sonda de tempos de viagem** (Routes API, travas de custo; `make sonda`) · [rotas](dados/rotas-sonda-tempos.csv)
- [campo/observacoes/transito-tipico/README.md](campo/observacoes/transito-tipico/README.md) — **roteiro de capturas do trânsito típico** (Google Maps)
- [campo/observacoes/roteiro-vistoria.md](campo/observacoes/roteiro-vistoria.md) — o que medir por ponto
- [campo/observacoes/modelo-observacao-campo.csv](campo/observacoes/modelo-observacao-campo.csv) — planilha de campo
- [campo/observacoes/inventario-evidencias.csv](campo/observacoes/inventario-evidencias.csv) — **inventário central de evidências** (rastreabilidade + público/interno)
- [campo/observacoes/ficha-drenagem.csv](campo/observacoes/ficha-drenagem.csv) — ficha de alagamento/drenagem
- [consultas/moradores/questionario-curto.md](consultas/moradores/questionario-curto.md) — **questionário curto (~2 min, porta de entrada)** · [completo](consultas/moradores/questionario-base.md)
- [consultas/moradores/aviso-privacidade.md](consultas/moradores/aviso-privacidade.md) — **aviso de privacidade (LGPD)** — preencher responsável/retenção antes de circular
- [consultas/registro-demandas-comunitarias.md](consultas/registro-demandas-comunitarias.md) — demandas estruturadas
- [consultas/respostas/README.md](consultas/respostas/README.md) — **pipeline de tabulação das respostas** (`make respostas`)

**Dados (sinistros)**
- [dados/tratados/acidentes_resumo_distancia_pontos.csv](dados/tratados/acidentes_resumo_distancia_pontos.csv) — **resumo refinado por ponto**
- [dados/tratados/acidentes_metodologia.md](dados/tratados/acidentes_metodologia.md) · [revisão manual](dados/tratados/acidentes_revisao_manual_notas.md)
- [scripts/processar_sinistros_distancia.py](scripts/processar_sinistros_distancia.py)
- [Segmentação do P4](dados/tratados/acidentes_p4_segmentos.csv) · [hot spots](dados/tratados/acidentes_p4_hotspots_250m.csv) · [script](scripts/segmentar_p4_monteggia.py)
- [Georreferenciamento de referências](dados/tratados/georreferenciamento_referencias_demandas.md) (P9/D1–D4/P7 — preliminar, a validar por bases oficiais, imagem aérea ou vistoria técnica)

**Cadastro e governança**
- [dados/pontos.csv](dados/pontos.csv) — **cadastro canônico dos pontos** (fonte única: ID, nome, status, coordenadas, confiança, aliases). As listas dos questionários são geradas dele (`make` / `scripts/pontos.py sync`).
- [dados/tratados/pontos.geojson](dados/tratados/pontos.geojson) — geometrias dos pontos (geradas do cadastro)
- [mapas/mapa-pontos.png](mapas/mapa-pontos.png) — **mapa dos pontos P1–P9** (`make mapa`; incluído no anexo externo)
- [dados/brutos/manifest.json](dados/brutos/manifest.json) — **manifesto dos insumos** (URL, SHA-256, licença, janela temporal). Reprodução: `make data`.
- [scripts/public_check.py](scripts/public_check.py) — **porteiro de publicação** (`make check`): links quebrados, vazamento de áreas privadas, placeholders, pontos inconsistentes.
- [scripts/build_pacote.py](scripts/build_pacote.py) — **gera o pacote de reunião** a partir das fontes (`make pacote`).
- [pacote-reuniao.md](pacote-reuniao.md) — **pacote de reunião (gerado)** · [PDF](pacote-reuniao.pdf)
- [Makefile](Makefile) — `make all` · `make check` · `make test` · `make data`

**Revisões técnicas (CODEX)**
- Mantidas fora deste repositório público (bastidores de revisão interna).

## Notas importantes
- **Dados de sinistros = associação preliminar por distância, não prova causal.** Exigem validação técnica; a vistoria solicitada à EPTC é a via principal para isso.
- **Grafia:** "Estr. Cristiano **Kraemer**" (confirmada pela comissão).
- **Marco urbanístico:** PDUS/LUOS **aprovados pela Câmara em 2026**; sanção/publicação e transição **a confirmar**.
- A obra asfáltica da Cristiano Kraemer é **SMSUrb (pavimento)**, ≠ projeto PSVS da Monte Cristo.
- **Privacidade:** nomes de moradores anonimizados (Morador A/B). Revisões internas, expedientes administrativos brutos (com dados pessoais/registrais) e a base bruta de sinistros (~15 MB) não são versionados.
- **Escopo (contribuição comunitária):** além de circulação/segurança, investigar **drenagem/alagamento**; os impactos alcançam também o Terraville e demais usuários da região.

## Próximos passos
Detalhe, dependências e datas-alvo: [ROTEIRO.md](ROTEIRO.md). Em síntese (trilhas paralelas):
1. **Acompanhar os [pedidos LAI](relatorios/pedidos-informacao-lai.md)**, com prazo ordinário em 03/08, e incorporar respostas ou prorrogações à matriz.
2. **Manter e consolidar a sonda** após 2–4 semanas: agregados por rota, horário, atraso e assimetria, com metodologia e limitações declaradas.
3. **Validar o pacote com a comissão em 13/8** ([guia](relatorios/guia-validacao-comissao.md)) e obter assinatura/canal ([LIBERACAO.md](LIBERACAO.md)).
4. **Protocolar na EPTC** dentro da janela da LOA 2027 (meta: até 20/ago), solicitando os dados e a vistoria técnica que complementam a evidência já disponível.

## Licença
Licenciamento duplo — **código** (`scripts/`, `tests/`, `Makefile`, `.github/`) sob **MIT**; **conteúdo** (textos, questionários, dados próprios) sob **CC BY 4.0**. Dados de terceiros mantêm suas licenças. Ver [LICENSE](LICENSE).
