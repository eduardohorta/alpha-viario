# Matriz de problemas — pontos de estrangulamento

> **Status:** versão 6 (Fase 0 — incorpora a leitura dos expedientes administrativos do Alphaville). **P4 segmentado por trecho**; **P9 (preliminar)** adicionado a partir da demanda D4 e, na Rodada 05, **identificado (Cristiano Kraemer × Juca Batista) e incorporado à associação por distância**.
> Fonte primária: [sugs.md](../sugs.md). Sinistros: [dados/tratados/acidentes_resumo_distancia_pontos.csv](../dados/tratados/acidentes_resumo_distancia_pontos.csv).
> **Jurisdição: municipal — Porto Alegre (EPTC/SMMU).**
>
> **Princípio:** separar **problema → hipótese causal → solução**. As "soluções candidatas" são **hipóteses**.
> **Grafia:** "Estrada Cristiano **Kraemer**" (corrigido de "Cremer"; confirmada pela comissão).
> **Projetos documentados:** os expedientes administrativos confirmam **Plano Funcional aprovado na SMT/EPTC**, obrigações específicas para P1/P2, estudos nos acessos de P6 e conexão em etapas para P7. P3 e P9 mantêm relação parcial/indireta; P4/P5/P8 permanecem fora da cobertura identificada. Ver [projetos-viarios-ja-aprovados.md](../relatorios/projetos-viarios-ja-aprovados.md). **A execução integral e o status atual continuam a confirmar.**
>
> **Nota metodológica (sinistros):** a Rodada 01 usou *triagem* por bounding box; a Rodada 02 refez por **associação à distância real** da malha OSM (limiar **≤100 m** para interseções e **≤50 m** para corredores/rotas). Os números abaixo são os **refinados (R02)**, com o **P9 incorporado na Rodada 05** pelo mesmo critério de interseção. **Associação por distância ≠ prova causal** — exige geocodificação fina, base municipal e vistoria.

## Quadro-resumo

| Nº | Local | Sinistros (refinado R02)¹ | Tipo | Resposta candidata (hipótese) |
|----|-------|---------------------------|------|-------------------------------|
| P1 | Rótula Estr. Três Meninas × Estr. Cristiano Kraemer | 29 (4 graves, 6 motos) | Interseção (rótula) | Estudo de redesenho da interseção |
| P2 | Trevo Cristiano Kraemer × Av. Belém Velho × Av. Monte Cristo | 58 (7 graves, 23 motos) | Interseção multi-ramo | Redesenho **em sinergia com o projeto PSVS da Monte Cristo** |
| P3 | Acesso à Av. Vicente Monteggia (Rodrigues da Fonseca / João Salomoni) | 44 (4 graves, 20 motos) | Interseção/acesso | Redesenho de interseção (canalização/rótula compacta/semáforo) |
| P4 | Fluxo na Av. Vicente Monteggia | **409 no corredor de ≈2,9 km (36 graves, 2 fatais, 186 motos)** ² | Corredor | **Diagnóstico de segurança primeiro** (segmentar por trecho); faixa reversível = hipótese condicionada |
| P5 | Conversão à direita Av. João Salomoni → Av. da Cavalhada | 71 (3 graves, 14 motos) ³ | Movimento de conversão | Operacional/geométrico de baixo custo, com pedestres e ônibus |
| P6 | Acesso à Av. Dr. Vergara (chão batido: Florestan Fernandes + Kanazawa) | 8 ² (evidência fraca — ver nota) | Conexão/rota | **Qualificação de rota alternativa** (sustentar por precariedade física, **não** por sinistros) |
| P7 | Acesso à Estr. Costa Gama (bairro→centro), sem conversão à esquerda | 18 (1 grave) | Acesso/conversão | Comparar retorno atual × conversão; alternativas múltiplas |
| P8 | Semáforo Estr. Costa Gama × Estr. Afonso Lourenço Mariante | 36 (4 graves, 17 motos) | Interseção semaforizada | **Diagnóstico semafórico-operacional primeiro** |
| P9 | Rótula Estr. Cristiano Kraemer × Av. Juca Batista ("rótula da Vila Nova") — *preliminar (demanda D4)* | 33 (1 grave, 8 motos) ⁴ | Interseção (rótula) | Refinamento geométrico (divisória; revisão de quebra-mola) — **a verificar** |

¹ associação por distância à malha (não causal). ² P4 e P6 são polilinha (corredor/rota), limiar ≤50 m; demais são ponto, limiar ≤100 m — **números de corredor somam a extensão inteira e não são comparáveis aos de interseção**; em peças externas, apresentar P4 por segmento (ver detalhamento). ³ em P5, o contexto ampliado (≤200 m) inclui 1 fatal na Av. Cavalhada (~128 m), **a validar** — não atribuível à conversão. ⁴ P9 entrou na associação por distância na Rodada 05, com o mesmo limiar das demais interseções (≤100 m). Dos 33, **11 citam explicitamente o par Juca Batista × Cristiano Kraemer** e 10 destes estão a menos de 25 m da rótula; os 21 que citam só a Juca Batista se dispersam com a distância (3/4/10/4 por faixa de 25 m), padrão de **corredor**, não de nó. Ou seja: parte do total pertence ao fluxo da Juca Batista e não à rótula. O número é mantido no mesmo critério dos demais pontos para preservar a comparabilidade da tabela — os quais, pelo mesmo motivo, também incorporam entorno.

## Prioridades de segurança
**P4** é a prioridade de segurança mais robusta — a segmentação (R03) aponta os trechos **S06 (João Vedana→João Passuelo: 9 graves, 1 fatal, 41 motos)**, **S01 (ponta Cavalhada/Nonoai)** e **S04 (Aracaju→Amapá: 1 fatal)** como prioridades de vistoria técnica. **P5** segue como prioridade de **investigação** (sinistralidade no entorno), mas **a relação com a conversão é hipótese a confirmar com dados e vistoria técnica**, não dado. Regra: **não propor aumento de capacidade sem mitigação de risco.**

---

## Detalhamento por ponto

> Camada obrigatória de modos vulneráveis em todos os pontos: travessia · calçada/acostamento · acessibilidade · paradas de ônibus · motos · bicicleta · conflito com pedestre/ciclista · velocidade. Marcados *a levantar*.

### P1 — Rótula Estr. Três Meninas × Estr. Cristiano Kraemer
- **Sinistros (R02, ≤100 m):** 29 ocorr. · 4 graves · 0 fatais · 6 motos.
- **Problema operacional:** estrangulamento na rótula (relato).
- **Problema de segurança:** graves e motos sugerem conflito/velocidade na rótula.
- **Hipótese causal (a testar):** geometria/deflexão inadequada e/ou desbalanceamento de volume; possível velocidade de entrada alta.
- **Movimento dominante:** a medir.
- **Modos vulneráveis:** *a levantar*.
- **Evidência mínima a coletar:** contagem direcional por movimento + fila por aproximação + conflitos.
- **Benefício público:** redução de risco em interseção municipal, sobretudo a motociclistas.
- **Solução candidata (hipótese):** estudo de redesenho da interseção — rótula compacta/moderna, canalização, semaforização ou microintervenções. *Não assumir "rótula maior".*

### P2 — Trevo Cristiano Kraemer × Av. Belém Velho × Av. Monte Cristo
- **Sinistros (R02, ≤100 m):** 58 ocorr. · 7 graves · 0 fatais · 23 motos · 3 ônibus.
- **Problema operacional:** confluência de três vias com conflito de circulação.
- **Problema de segurança:** sinistralidade relevante, com presença importante de motos.
- **Hipótese causal:** múltiplos pontos de conflito numa confluência sem canalização clara; velocidade.
- **Movimento dominante:** a medir.
- **Modos vulneráveis:** *a levantar*.
- **Evidência mínima a coletar:** contagem direcional + fila por aproximação + conflitos.
- **Gancho institucional:** o **projeto PSVS de qualificação da Av. Monte Cristo termina na Estr. Cristiano Kraemer (este nó)** — **sinergia direta** com o P2.
- **Benefício público:** segurança numa confluência crítica; sinergia com projeto municipal existente.
- **Solução candidata (hipótese):** estudo de redesenho da confluência **em sinergia com o projeto da Av. Monte Cristo**; rótula moderna como **uma** das alternativas.

### P3 — Acesso à Av. Vicente Monteggia (Rodrigues da Fonseca / João Salomoni)
- **Sinistros (R02, ≤100 m):** 44 ocorr. · 4 graves · 0 fatais · 20 motos.
- **Problema operacional:** dificuldade de acesso/entrada na Monteggia.
- **Problema de segurança:** presença relevante de motos.
- **Hipótese causal:** conflito de junção sem prioridade clara; brechas (*gaps*) insuficientes.
- **Movimento dominante:** a medir.
- **Modos vulneráveis:** *a levantar*.
- **Evidência mínima a coletar:** contagem direcional por movimento + fila por aproximação + conflitos.
- **Benefício público:** organização de acesso e redução de conflito em via municipal.
- **Solução candidata (hipótese):** estudo de redesenho da interseção (canalização, rótula compacta ou semaforização) + medidas operacionais.

### P4 — Fluxo na Av. Vicente Monteggia  ⚠️ prioridade de segurança
- **Sinistros (R02, ≤50 m da malha):** **409 ocorr. · 36 graves · 2 fatais · 186 motos · 6 ônibus** (corredor inteiro).
- **Segmentação (R03):** trechos prioritários — **S06** João Vedana→João Passuelo (67 ocorr., 9 graves, 1 fatal, 41 motos); **S01** ponta Cavalhada/Nonoai (104 ocorr., 11 graves — *revisar ruído de geocodificação*); **S04** Aracaju→Amapá (1 fatal). Ver [segmentos](../dados/tratados/acidentes_p4_segmentos.csv).
- **Problema operacional:** congestionamento/fluxo do corredor.
- **Problema de segurança:** corredor de alta sinistralidade, com fatais e forte presença de motos.
- **Hipótese causal:** corredor **segmentado** (1–3 faixas, vários sentidos únicos — OSM); congestionamento pode ser sintoma de geometria/semáforos e conflitos, não só capacidade.
- **Movimento dominante:** a medir (origem-destino e assimetria por trecho/hora).
- **Modos vulneráveis:** *a levantar* — obrigatório (paradas de ônibus, travessias, motos).
- **Evidência mínima a coletar:** contagem direcional por trecho/hora + velocidades + acidentes por **segmento** + paradas de ônibus.
- **Benefício público:** redução de mortes e feridos graves em corredor municipal.
- **Solução candidata (hipótese):** **diagnóstico de segurança do corredor primeiro**, segmentando por trecho. **Faixa reversível = hipótese condicionada** (ver [avaliacao-solucoes-iniciais.md](avaliacao-solucoes-iniciais.md)). *Não aumentar capacidade sem mitigar risco.*

### P5 — Conversão à direita Av. João Salomoni → Av. da Cavalhada  ⚠️ investigar
- **Sinistros (R02, ≤100 m):** 71 ocorr. · 3 graves · 0 fatais · 14 motos · 1 ônibus. **Contexto ≤200 m:** 102 ocorr. e **1 fatal na Av. Cavalhada (~128 m), a validar — não atribuível à conversão.**
- **Problema operacional:** conversão à direita problemática (relato).
- **Problema de segurança:** sinistralidade no **entorno** (quase toda em `AV CAVALHADA`); a relação com a conversão João Salomoni → Cavalhada **não está provada** pelos dados.
- **Hipótese causal (a comprovar em campo):** conflito da conversão com travessia e com o fluxo da Cavalhada; raio/visibilidade; interação com ônibus.
- **Movimento dominante:** volume da conversão (a medir).
- **Modos vulneráveis:** *a levantar* — crítico aqui (pedestres na esquina, ônibus).
- **Evidência mínima a coletar:** volume da conversão + conflitos observados + fase semafórica + travessia + ônibus/paradas + raio de giro.
- **Benefício público:** segurança de pedestres e usuários de ônibus em via arterial.
- **Solução candidata (hipótese):** operacional/geométrico de baixo custo (baia/raio, canalização, fase semafórica), **com tratamento explícito de pedestres e ônibus** — **após** confirmar o problema em campo.

### P6 — Acesso à Av. Dr. Vergara (chão batido)
- **Sinistros (R02, ≤50 m):** 8 ocorr. (vários dos mais próximos estão na Estr. Três Meninas, perto da conexão) — **evidência de sinistro fraca; não usar como argumento central**.
- **Problema operacional:** acesso por chão batido (R. Florestan Fernandes + Estr. Kanazawa); rota precária.
- **Achado documental:** o segundo aditamento de 2013 exigiu novos estudos das interseções da Estr. das Três Meninas com **Kanazawa** e **Florestan Fernandes**, seguidos de projetos de pavimento. Não foi localizada comprovação de aprovação/execução desses projetos, e a obrigação não cobre necessariamente toda a rota até a Av. Dr. Vergara.
- **Checagem OSM:** Estr. Kanazawa `unpaved/dirt`; R. Florestan Fernandes asfalto porém `smoothness=very_bad`, `sidewalk=no`.
- **Problema (eixo do argumento):** **precariedade física** — pavimento, drenagem, calçada, iluminação, seção; risco de tráfego de passagem em via residencial.
- **Hipótese causal:** ausência de rota pavimentada adequada força desvios; via despreparada.
- **Modos vulneráveis:** *a levantar* — moradias lindeiras, pedestres, drenagem.
- **Evidência mínima a coletar:** largura, superfície, drenagem, calçadas, inclinação, iluminação, moradias lindeiras e origem-destino provável; **restrição ambiental/APP e situação fundiária**.
- **Benefício público:** rota mais segura e drenada para moradores do entorno.
- **Solução candidata (hipótese):** **qualificação de rota alternativa** = pavimento + drenagem + seção segura + velocidade baixa + pedestres + controle de tráfego de passagem.

### P7 — Acesso à Estr. Costa Gama bairro→centro (sem conversão à esquerda)
- **Sinistros (R02, ≤100 m):** 18 ocorr. · 1 grave.
- **Problema operacional:** não é possível converter à esquerda; exige retorno em rótula distante.
- **Achado documental:** o expediente-mãe confirma projeto geométrico aprovado para a conexão Três Meninas–Costa Gama, dividido em **primeira etapa sem desapropriação** e **solução definitiva após desapropriações**. Correspondência de 2013 informa que a nova ligação estava aprovada na CTAAPS. A geometria específica de uma **“alça à esquerda” não foi confirmada** nas peças identificadas.
- **Problema de segurança:** abrir conversão à esquerda pode **criar** conflito pior que o desvio atual.
- **Hipótese causal:** o problema real pode ser a **distância/tempo do retorno**, não a proibição.
- **Evidência mínima a coletar:** distância e tempo do retorno atual + volume do movimento desejado + velocidade na Costa Gama + fila/armazenagem para baia + visibilidade + acidentes no entorno.
- **Modos vulneráveis:** *a levantar*.
- **Benefício público:** redução de quilometragem/tempo improdutivo e de risco no retorno.
- **Solução candidata (hipótese — manter alternativas):** verificar e, se tecnicamente atual, **concluir a conexão/interseção projetada** · alça, somente se confirmada pelo desenho · retorno protegido · conversão semaforizada · rota alternativa · **ou** manter a restrição melhorando o retorno existente.

### P8 — Semáforo Estr. Costa Gama × Estr. Afonso Lourenço Mariante (bairro→centro)
- **Sinistros (R02, ≤100 m):** 36 ocorr. · 4 graves · 0 fatais · 17 motos. Nó OSM ~`-30.1152, -51.1771`.
- **Problema operacional:** longos engarrafamentos no pico.
- **Problema de segurança:** presença relevante de motos.
- **Hipótese causal:** tempos semafóricos/coordenação inadequados; capacidade × demanda no pico.
- **Evidência mínima a coletar:** ciclo + split por aproximação + defasagem com semáforos vizinhos + fila residual após verde + volume por aproximação + ônibus + pedestres.
- **Modos vulneráveis:** *a levantar*.
- **Benefício público:** redução de fila e de risco em interseção semaforizada municipal.
- **Solução candidata (hipótese):** **diagnóstico semafórico-operacional primeiro**. Redesenho/rótula só depois, se a capacidade for de fato o gargalo.

### P9 — Rótula Estr. Cristiano Kraemer × Av. Juca Batista ("rótula da Vila Nova") — *preliminar*
- **Origem:** demanda **D4** ([registro](../consultas/registro-demandas-comunitarias.md)); **nó distinto do P1** (rótula 3 Meninas × Cristiano Kraemer). Também é a âncora sul do corredor descrito na **D3** ("da rótula da Vila Nova até as Três Meninas"), o que o mantém dentro do recorte do eixo Cristiano Kraemer apesar da distância (~3,2 km ao sul do P1).
- **Relato:** divisória (canteiro) na chegada/saída da Cristiano Kraemer à rótula e revisão do quebra-mola (manter na chegada, retirar na saída).
- **Localização:** -30.1476851, -51.2045098 (centroide dos segmentos OSM `junction=circular`; transversal confirmada visualmente em 20/07/2026). Rótula pequena, ~29 × 33 m — compatível com refinamento geométrico, não com redesenho.
- **Sinistros:** **33** pelo limiar de 100 m (11 feridos, 1 grave, 0 fatais, 8 motos); 57 no contexto de 200 m; distância mínima 3,8 m. **Ler com a ressalva ⁴ do quadro-resumo:** apenas 11 registros citam o cruzamento explicitamente, e a dispersão dos demais indica contribuição do corredor da Av. Juca Batista. Detalhamento em [metodologia, Rodada 05](../dados/tratados/acidentes_metodologia.md).
- **Hipótese causal:** a definir após vistoria.
- **Modos vulneráveis:** 8 motos entre os 33 registros; pedestres *a levantar* em campo.
- **Evidência mínima a coletar:** geometria atual da rótula, velocidade na saída, conflitos, pedestres, posição dos quebra-molas (chegada/saída).
- **Benefício público:** *a confirmar* — fluidez na saída mantendo segurança na chegada.
- **Solução candidata (hipótese):** refinamento geométrico (divisória/canteiro) + revisão da moderação de velocidade — **após** vistoriar. A remoção do quebra-mola da saída exige justificar que a segurança se mantém; os 33 registros do entorno **não** sustentam essa remoção por si sós.

---

## Dimensões adicionais a investigar (contribuição comunitária)
- **Drenagem / alagamento:** dimensão ainda **não mapeada** nos P1–P9 (que são circulação/segurança). Levantar **pontos de alagamento** no entorno da Estr. das Três Meninas e acessos.
- **Escopo regional:** os problemas afetam também o **Terraville** e demais usuários da Zona Sul — reforça o **benefício público além do condomínio**.

## Próximos preenchimentos necessários
- **Sonda:** consolidar os agregados por rota e janela horária, incluindo atraso versus fluxo livre, assimetria no P4 e custo do retorno no P7.
- **Sinistros:** **validar por aerofoto, bases oficiais e vistoria técnica da EPTC os segmentos P4-S06/S01/S04** e os registros mais próximos — ver [segmentos](../dados/tratados/acidentes_p4_segmentos.csv), [revisão manual](../dados/tratados/acidentes_revisao_manual_notas.md) e [metodologia](../dados/tratados/acidentes_metodologia.md).
- **Imagem aérea + base SMAMUS:** confirmar geometria real de cada ponto.
- **Planos oficiais:** zoneamento de Vila Nova no novo PDUS; escopo da requalificação da Av. Monte Cristo.
