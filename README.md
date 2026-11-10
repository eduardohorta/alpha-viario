# Projeto Viário — Alphaville Porto Alegre (Vila Nova / Zona Sul)

Projeto comunitário para propor melhorias viárias no entorno do Alphaville Porto Alegre (Estr. das Três Meninas, bairro **Vila Nova**), com qualidade técnica para apresentação à **Prefeitura de Porto Alegre (EPTC/SMMU)**. **Todas as vias são municipais.**

## Status atual — 09/11/2026
A base oficial do dossiê é a **EPTC**, obtida pelo Pedido 17 (01/01/2010–09/09/2026); Dados Abertos POA (01/01/2020–31/08/2025) permanece como auxiliar. **Ambas contêm registros com e sem vítimas registradas.** A [reconciliação por ID na janela comum](dados/tratados/sinistros_reconciliacao.md) distingue diferenças de cobertura e coordenadas. Não interpretar a comparação dos totais como tendência de segurança.

A trilha LAI soma **30 pedidos protocolados**. A situação atual está no [acompanhamento](relatorios/pedidos-informacao-lai.md#acompanhamento): Pedido 14 respondido em 10/11, 63 dias após o prazo, só sobre o esgoto (certidão de 2013 do coletor tronco do loteamento; rede de água sem resposta), enquanto o 27, que o refez, segue sem resposta; 16 com peças faltantes (reexame não apresentado), pedidas no 26 e recebidas em 05/11; 18 respondido em 30/09 sem localização do depósito (remetido à SMAMUS); 24, 27 e 30 vencidos sem resposta, em espera por decisão da comissão; o 20 foi respondido pela SMF (intermediária em 15/10; planta e planilha das desapropriações por e-mail, registradas em 26/10: 7 lotes da Cristiano Kraemer com negociação suspensa desde 2014). Os 21 (16/09), 22 (06/10), 19 (14/10, parcial: três pareceres, sem o quarto processo; reexame apresentado no mesmo dia e indeferido em 27/10, por serem documentos preparatórios) e 23 (19/10, parcial: TAC do MP não localizado, com indício de averbações nas matrículas; arquivado sem reexame) foram respondidos; o 25 (drenagem, feito à CTAAPS após a resposta do DMAE) foi respondido pela PGM em 05/11: projeto não elaborado, adiado até a conclusão das desapropriações, com reexame sobre o responsável apresentado em 09/11; o 26 (PGM) trouxe em 05/11 o Parecer 985/1997 e a Informação 4084/2022 e declarou que não há cronograma das desapropriações; o 29 (SMAMUS, 09/11, parcial) informou os expedientes ligados ao P8 (suspenso por ordem judicial) e ao P5 (em análise), sem Termo de Compromisso nem contrapartida confirmada, com reexame do item 1 apresentado no mesmo dia; o 28 (PGM, 09/11, parcial) informou demolição designada para 28/10 (executada, segundo a comissão, sem confirmação oficial), sem registro de notificação ao empreendedor e sem processo de desapropriação na Rodrigues da Fonseca, com reexame apresentado no mesmo dia. A documentação de 24–25/09 reconcilia as parcelas fundiárias do P7; a faixa da Três Meninas 1085 fica junto à Florestan Fernandes (P6), não ao P1.

**Reunião:** a ata da reunião com a Diretoria da EPTC (22/09) foi recebida em 08/10/2026, em versão revisada ainda não final; os encaminhamentos estão em [PENDENCIAS.md](PENDENCIAS.md). As decisões documentadas de 13/08 permanecem como referência. **O protocolo principal (ofício à SMAMUS) não foi realizado; a comissão articula uma reunião com a SMAMUS.**

Os agregados da sonda têm **8.582 medições em 14 rotas**, de 04/07 a 01/09; são estimativas descritivas, e a comparação R05/R06 mede assimetria entre sentidos, não o efeito isolado da alça. A **coleta foi pausada em 01/11/2026** (série de 04/07 a 01/11, ainda não reagregada); ver [detalhe](campo/sonda-tempos-google.md). Coleta física e questionário seguem em espera e não bloqueiam o protocolo.

**Ordem e datas:** [ROTEIRO.md](ROTEIRO.md) — caminho crítico, trilhas paralelas e janelas de calendário (LOA 2027, PDUS). **Pendências abertas:** [PENDENCIAS.md](PENDENCIAS.md). **Antes de circular/protocolar:** [LIBERACAO.md](LIBERACAO.md) (+ `make release-check`). **Inspeção nova? Comece pela** [ARQUITETURA.md](ARQUITETURA.md) — como as peças (dois repositórios, fluxos de dado, governança) se encaixam.

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
9. **P9** *(preliminar)* — Entroncamento Rua Santuário × Av. Oscar Pereira (decisão de 13/08; pin de 14/08). A antiga referência da rótula permanece apenas no histórico de D4

## Índice de documentos

**Orientação**
- [ARQUITETURA.md](ARQUITETURA.md) — **comece aqui**: dois repositórios, fluxos de dado e governança
- [ROTEIRO.md](ROTEIRO.md) · [LIBERACAO.md](LIBERACAO.md) · [PENDENCIAS.md](PENDENCIAS.md) — estado, gate e backlog

**Insumos brutos**
- [sugs.md](sugs.md) — relato original (8 pontos + 3 propostas)
- [starting-point.md](starting-point.md) — pedido inicial
- [consultas/contribuicoes-comunitarias-publico.md](consultas/contribuicoes-comunitarias-publico.md) — contribuições da comunidade (versão neutra). *Inbox bruto mantido em `interno/`.*

**Plano e propostas**
- [ROTEIRO.md](ROTEIRO.md) — **caminho crítico, trilhas paralelas e datas-alvo (jul–out 2026)**
- [plano-de-trabalho.md](plano-de-trabalho.md) — plano fundador (histórico; etapas 0–9)
- [propostas/problemas-priorizados.md](propostas/problemas-priorizados.md) — **matriz dos pontos — 8 + P9 preliminar (v7)**
- [propostas/avaliacao-solucoes-iniciais.md](propostas/avaliacao-solucoes-iniciais.md) — avaliação das 3 soluções + escada de intervenção

**Relatórios e peças**
- [relatorios/revisao-documental.md](relatorios/revisao-documental.md) — enquadramento legal/institucional
- [relatorios/memorando-1pagina.md](relatorios/memorando-1pagina.md) — memorando (uso interno, rastreável)
- [relatorios/memorando-externo.md](relatorios/memorando-externo.md) — **versão institucional limpa**
- [relatorios/oficio-eptc-rascunho.md](relatorios/oficio-eptc-rascunho.md) — **rascunho de ofício (canal principal SMAMUS, cópia à EPTC/SMMU; não protocolado)**
- [relatorios/anexo-matriz-pontos.md](relatorios/anexo-matriz-pontos.md) — **anexo externo (1 linha por ponto)**
- [relatorios/guia-validacao-comissao.md](relatorios/guia-validacao-comissao.md) — **pauta de validação e encaminhamento do protocolo**
- [relatorios/linha-do-tempo-documental.md](relatorios/linha-do-tempo-documental.md) — **cronologia 2009→2026 em uma página** (o que a cidade pactuou, projetou e declarou, e o que parou); [versão HTML para projetar](relatorios/linha-do-tempo-documental.html)
- [relatorios/projetos-viarios-ja-aprovados.md](relatorios/projetos-viarios-ja-aprovados.md) — **evidência administrativa, obrigações e execução parcial no eixo Três Meninas**
- [relatorios/matriz-publica-status-plano-funcional.md](relatorios/matriz-publica-status-plano-funcional.md) — **matriz de previsão documental × execução × verificação atual**
- [relatorios/pedidos-informacao-lai.md](relatorios/pedidos-informacao-lai.md) — **pedidos LAI prontos para protocolo (trilha independente do pleito)**

**Sonda e instrumentos de referência**
- [campo/plano-evidencia-leve.md](campo/plano-evidencia-leve.md) — referência de contingência para mobilização futura ou vistoria técnica · [plano técnico completo](campo/plano-coleta-campo.md)
- [campo/sonda-tempos-google.md](campo/sonda-tempos-google.md) — **sonda de tempos de viagem** (Routes API no Google Cloud, travas de custo) · [rotas](dados/rotas-sonda-tempos.csv) · agregação para o dossiê: `make sonda-agg` → [resumo](dados/tratados/sonda_tempos_resumo.md) · [agregado](dados/tratados/sonda_tempos_agregado.csv)
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
- [dados/tratados/acidentes_resumo_distancia_pontos.csv](dados/tratados/acidentes_resumo_distancia_pontos.csv) — **resumo auxiliar por ponto**; [resumo oficial EPTC](dados/tratados/eptc_acidentes_resumo_distancia_pontos.csv) e [reconciliação](dados/tratados/sinistros_reconciliacao.md)
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
- **Marco urbanístico:** PDUS/LUOS **aprovados pela Câmara em 2026** e **sancionados em 14/07/2026**; textos finais, vetos e transição **a conferir**.
- A obra asfáltica da Cristiano Kraemer é **SMSUrb (pavimento)**, ≠ projeto PSVS da Monte Cristo.
- **Privacidade:** nomes de moradores anonimizados (Morador A/B). Revisões internas, expedientes administrativos brutos (com dados pessoais/registrais) e a base bruta de sinistros (~15 MB) não são versionados.
- **Escopo (contribuição comunitária):** além de circulação/segurança, investigar **drenagem/alagamento**; os impactos alcançam também o Terraville e demais usuários da região.

## Próximos passos
1. Fechar a versão final da ata da reunião com a EPTC e cumprir seus encaminhamentos.
2. Acompanhar as pendências LAI no [registro atualizado](relatorios/pedidos-informacao-lai.md#acompanhamento), sem repetir pedidos já respondidos.
3. Protocolo principal não realizado: acompanhar a articulação da reunião com a SMAMUS e decidir o uso do ofício e do pacote; usar [LIBERACAO.md](LIBERACAO.md) antes de qualquer envio.
4. Validar os pontos em base municipal/vistoria e conferir o enquadramento territorial do novo P9; a consulta de julho usava o antigo ponto.
5. Manter os agregados e as sínteses documentais atualizados, com janela e limites explícitos.

## Licença
Licenciamento duplo — **código** (`scripts/`, `tests/`, `Makefile`, `.github/`) sob **MIT**; **conteúdo** (textos, questionários, dados próprios) sob **CC BY 4.0**. Dados de terceiros mantêm suas licenças. Ver [LICENSE](LICENSE).
