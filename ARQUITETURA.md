# Arquitetura e mapa do projeto

> **Comece por aqui** se você está inspecionando o projeto pela primeira vez.
> Este documento é **estável** (a arquitetura muda pouco). Para o **estado atual e as
> datas**, veja o topo do [README](README.md) e o [ROTEIRO](ROTEIRO.md); para o **gate
> antes de protocolar**, o [LIBERACAO](LIBERACAO.md); para o **backlog por responsável**,
> o [PENDENCIAS](PENDENCIAS.md).

## O que é
Projeto comunitário que propõe melhorias viárias em **9 pontos (P1–P9)** à EPTC/Prefeitura
de Porto Alegre. O produto é um **dossiê técnico** protocolado na EPTC pedindo dados e
vistoria. Fase atual: montar a **evidência prévia** (sinistros + tempos de viagem +
documentos oficiais via LAI); coleta física comunitária e questionário ficam **em espera**
e não bloqueiam o protocolo.

## Dois repositórios
| Repositório | Visibilidade | Papel |
|-------------|--------------|-------|
| `alpha-viario` (este) | público | dossiê, cadastro dos pontos, governança, **agregados** |
| `alpha-viario-sonda` | privado | coletor da sonda (Google Cloud) + **dados brutos** de tempos |

Só **agregados** cruzam do privado para o público. O bruto (Google) e os dados
pessoais/registrais ficam no privado ou em `interno/` (gitignored).

## Como o dado vira dossiê (4 fluxos)

### 1. Sinistros (segurança)
Dados Abertos POA (CC-BY; bruto ~15 MB **gitignored**) → `scripts/processar_sinistros_distancia.py`
+ `scripts/segmentar_p4_monteggia.py` → `dados/tratados/acidentes_*` → anexo/matriz.
Reprodução: `make data` (confere o SHA-256 do bruto contra `dados/brutos/manifest.json`).

### 2. Sonda de tempos (fluidez)
O coletor roda em **Google Cloud (Cloud Function + Scheduler)** nos picos e **commita a
série no repo privado** `alpha-viario-sonda` — **não** é GitHub Actions (o workflow que
existe lá é só variante documentada; não confundir "workflow active" com "coletando"). O
sinal de que está viva é o **commit diário de dados**. Para o dossiê, `make sonda-agg`
baixa a série (via `gh`) e roda `scripts/agregar_sonda.py`, gerando
`dados/tratados/sonda_tempos_{agregado.csv,resumo.md}` — **só agregados** entram no dossiê.
A chave da API nunca entra em nenhum repositório. Detalhe e travas de custo:
[campo/sonda-tempos-google.md](campo/sonda-tempos-google.md).

### 3. Trânsito típico e evidência de campo
Capturas do Google Maps (e, se acionada, coleta física) → registradas em
`campo/observacoes/inventario-evidencias.csv` com classificação **público/interno**.

### 4. Documentos oficiais (LAI) e questionário
Os [pedidos LAI](relatorios/pedidos-informacao-lai.md) (8 protocolados — o Pedido 8, à PGM,
desdobrado das respostas 2 e 3) buscam o que só a Prefeitura tem. **As respostas brutas ficam em
`retornos-protocolos/` (gitignored)**; só os **fatos institucionais** são transcritos para o
[documento de projetos aprovados](relatorios/projetos-viarios-ja-aprovados.md) e a
[matriz de status](relatorios/matriz-publica-status-plano-funcional.md) — mesmo padrão dos
expedientes-únicos. As duas primeiras respostas (jul/2026) confirmaram e caducaram o projeto
do P7. O questionário e seu pipeline (`make respostas`) estão **prontos, em espera** — só
circulam se a comissão decidir (aí o [aviso de privacidade](consultas/moradores/aviso-privacidade.md)
volta a ser exigido).

## Cadastro canônico + governança
- `dados/pontos.csv` é a **fonte única** dos pontos → gera o GeoJSON, o mapa e as listas
  dos questionários (`scripts/pontos.py`, via regiões marcadas nos documentos).
- **Porteiros:** `make check` (public-check — links quebrados, vazamento de áreas privadas,
  placeholders, consistência dos pontos) e `make release-check` (estrito, antes de
  protocolar). O CI roda os dois + testes a cada push.
- Pacote de reunião **gerado** das fontes (`make pacote`, exige Pandoc); testes em `tests/`.
- Licença dupla: **MIT** (código) / **CC BY 4.0** (conteúdo). Ver [LICENSE](LICENSE).

## Fronteira público × privado — o que NUNCA vai ao repo público
- Bruto de sinistros (~15 MB) e bruto da sonda (Google) — gitignored / repo privado.
- **Chave da Routes API** — só no ambiente da Google Cloud.
- Nomes reais de moradores (anonimizados como Morador A/B); `interno/termos-sensiveis.txt`
  (privado) liga a checagem que bloqueia vazamento.
- Expedientes administrativos brutos e **retornos de protocolos LAI** (`retornos-protocolos/`),
  revisões internas (CODEX) e estratégia jurídica — `interno/`.

## Comandos-chave
`make check` · `make release-check` · `make test` · `make data` · `make sonda-agg` ·
`make pacote` · `make mapa` · `make respostas`. Lista completa: `make help`.
