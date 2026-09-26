# Matriz de problemas — pontos de estrangulamento

> **Status:** versão 7 (Fase 0). **P4 segmentado por trecho**; **P9 (preliminar)** foi **redefinido na reunião de 13/08/2026** como o **entroncamento Rua Santuário × Av. Oscar Pereira**, **georreferenciado por pin em 14/08/2026** (55 sinistros por proximidade na base EPTC; 17 na R02); o ponto anterior (rótula Cristiano Kraemer × Juca Batista) foi **retirado**.
> Fonte primária: [sugs.md](../sugs.md). Sinistros (**base oficial, EPTC**): [eptc_acidentes_resumo_distancia_pontos.csv](../dados/tratados/eptc_acidentes_resumo_distancia_pontos.csv); auxiliar (Dados Abertos POA, R02): [acidentes_resumo_distancia_pontos.csv](../dados/tratados/acidentes_resumo_distancia_pontos.csv).
> **Jurisdição: municipal — Porto Alegre (EPTC/SMMU).**
>
> **Princípio:** separar **problema → hipótese causal → solução**. As "soluções candidatas" são **hipóteses**.
> **Grafia:** "Estrada Cristiano **Kraemer**" (corrigido de "Cremer"; confirmada pela comissão).
> **Projetos documentados:** os expedientes administrativos confirmam **Plano Funcional aprovado na SMT/EPTC**, obrigações específicas para P1/P2, estudos nos acessos de P6 e conexão em etapas para P7. P3 mantém relação parcial; P4/P5/P8 e o P9 atual permanecem fora da cobertura específica identificada. Ver [projetos-viarios-ja-aprovados.md](../relatorios/projetos-viarios-ja-aprovados.md). **A execução integral e o status atual continuam a confirmar.**
>
> **Nota metodológica (sinistros):** a Rodada 01 usou *triagem* por bounding box; a Rodada 02 refez por **associação à distância real** da malha OSM (limiar **≤100 m** para interseções e **≤50 m** para corredores/rotas). **Decisão de 24/09/2026:** a base oficial de sinistros passa a ser a da **EPTC** (Rodada 04, obtida pelo Pedido 17: 264.567 registros, 2010–2026, todas as ocorrências, inclusive danos materiais); os números abaixo são os da EPTC, pelo mesmo critério de distância. Os da **R02** (Dados Abertos POA, 2020–2025, sem filtro de vítimas, com o P9 atual incorporado em agosto) ficam como **evidência auxiliar**, indicados como *R02*. As bases têm janelas, cobertura e coordenadas diferentes; **ambas incluem registros sem vítimas**. A diferença de totais não demonstra tendência de segurança — ver [metodologia](../dados/tratados/acidentes_metodologia.md#rodada-04-base-oficial-eptc-via-pedido-17-22092026). **Associação por distância ≠ prova causal** — exige geocodificação fina, base municipal e vistoria.

## Quadro-resumo

| Nº | Local | Sinistros (base EPTC 2010–2026; entre parênteses, R02)¹ | Tipo | Resposta candidata (hipótese) |
|----|-------|---------------------------|------|-------------------------------|
| P1 | Rótula Estr. Três Meninas × Estr. Cristiano Kraemer | **58** (3 graves, 18 motos; R02: 29) | Interseção (rótula) | Estudo de redesenho da interseção |
| P2 | Trevo Cristiano Kraemer × Av. Belém Velho × Av. Monte Cristo | **150** (14 graves, 50 motos; R02: 58) | Interseção multi-ramo | Redesenho **em sinergia com o projeto PSVS da Monte Cristo** |
| P3 | Acesso à Av. Vicente Monteggia (Rodrigues da Fonseca / João Salomoni) | **136** (12 graves, 57 motos; R02: 44) | Interseção/acesso | Redesenho de interseção (canalização/rótula compacta/semáforo) |
| P4 | Fluxo na Av. Vicente Monteggia | **1.648 no corredor de ≈2,9 km (94 graves, 8 fatais, 640 motos; R02: 409)** ² | Corredor | **Diagnóstico de segurança primeiro** (segmentar por trecho); faixa reversível = hipótese condicionada |
| P5 | Conversão à direita Av. João Salomoni → Av. da Cavalhada | **311** (6 graves, 57 motos; R02: 71) ³ | Movimento de conversão | Operacional/geométrico de baixo custo, com pedestres e ônibus |
| P6 | Acesso à Av. Dr. Vergara (chão batido: Florestan Fernandes + Kanazawa) | **36** (2 graves, 15 motos; R02: 8) ² (evidência fraca — ver nota) | Conexão/rota | **Qualificação de rota alternativa** (sustentar por precariedade física, **não** por sinistros) |
| P7 | Acesso à Estr. Costa Gama (bairro→centro), sem conversão à esquerda | **67** (6 graves, 1 fatal, 17 motos; R02: 18) | Acesso/conversão | Comparar retorno atual × conversão; alternativas múltiplas |
| P8 | Semáforo Estr. Costa Gama × Estr. Afonso Lourenço Mariante | **124** (11 graves, 44 motos; R02: 36) | Interseção semaforizada | **Diagnóstico semafórico-operacional primeiro** |
| P9 | Entroncamento Rua Santuário × Av. Oscar Pereira — *preliminar (reunião 13/08/2026)* | **55** (6 graves, 1 fatal, 26 motos; R02: 17) ⁴ | Interseção (conversão à esquerda) | Fila para conversão à esquerda no pico; volume, geometria e travessia — **a verificar** |

¹ associação por distância à malha (não causal). ² P4 e P6 são polilinha (corredor/rota), limiar ≤50 m; demais são ponto, limiar ≤100 m — **números de corredor somam a extensão inteira e não são comparáveis aos de interseção**; em peças externas, apresentar P4 por segmento (ver detalhamento). ³ em P5, o contexto ampliado (≤200 m) inclui 1 fatal na Av. Cavalhada (~128 m), **a validar** — não atribuível à conversão. ⁴ P9 foi **redefinido na reunião de 13/08/2026** como o entroncamento Rua Santuário × Av. Oscar Pereira e **georreferenciado por pin em 14/08/2026** (-30.096763, -51.178065). Os 55 registros da base EPTC (17 na R02) são a associação por proximidade (≤100 m) desse novo ponto; a associação do ponto anterior (rótula Juca Batista) foi **retirada**.

## Prioridades de segurança
**P4** é a prioridade de segurança mais robusta — a segmentação na base EPTC aponta os trechos **S06 (João Vedana→João Passuelo: 25 graves, 2 fatais, 116 motos)**, **S03 (Otto Niemeyer→Aracaju: 3 fatais)** e **S01 (ponta Cavalhada/Nonoai: 494 ocorrências)** como prioridades de vistoria técnica (a R03, auxiliar, apontava S06, S01 e S04). **P5** segue como prioridade de **investigação** (sinistralidade no entorno), mas **a relação com a conversão é hipótese a confirmar com dados e vistoria técnica**, não dado. Regra: **não propor aumento de capacidade sem mitigação de risco.**

---

## Detalhamento por ponto

> Camada obrigatória de modos vulneráveis em todos os pontos: travessia · calçada/acostamento · acessibilidade · paradas de ônibus · motos · bicicleta · conflito com pedestre/ciclista · velocidade. Marcados *a levantar*.

### P1 — Rótula Estr. Três Meninas × Estr. Cristiano Kraemer
- **Sinistros (base EPTC 2010–2026, ≤100 m):** 58 ocorr. · 3 graves · 0 fatais · 18 motos. *Auxiliar (R02, 2020–2025, sem filtro de vítimas): 29 ocorr. · 4 graves · 6 motos.*
- **Problema operacional:** estrangulamento na rótula (relato).
- **Problema de segurança:** graves e motos sugerem conflito/velocidade na rótula.
- **Hipótese causal (a testar):** geometria/deflexão inadequada e/ou desbalanceamento de volume; possível velocidade de entrada alta.
- **Movimento dominante:** a medir.
- **Modos vulneráveis:** *a levantar*.
- **Evidência mínima a coletar:** contagem direcional por movimento + fila por aproximação + conflitos.
- **Benefício público:** redução de risco em interseção municipal, sobretudo a motociclistas.
- **Solução candidata (hipótese):** estudo de redesenho da interseção — rótula compacta/moderna, canalização, semaforização ou microintervenções. *Não assumir "rótula maior".*

### P2 — Trevo Cristiano Kraemer × Av. Belém Velho × Av. Monte Cristo
- **Sinistros (base EPTC 2010–2026, ≤100 m):** 150 ocorr. · 14 graves · 0 fatais · 50 motos · 13 ônibus. *Auxiliar (R02): 58 ocorr. · 7 graves · 23 motos · 3 ônibus.*
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
- **Sinistros (base EPTC 2010–2026, ≤100 m):** 136 ocorr. · 12 graves · 0 fatais · 57 motos · 5 ônibus; 1 fatal só no contexto ≤200 m (2010, Estr. João Salomoni). *Auxiliar (R02): 44 ocorr. · 4 graves · 20 motos.*
- **Problema operacional:** dificuldade de acesso/entrada na Monteggia.
- **Problema de segurança:** presença relevante de motos.
- **Hipótese causal:** conflito de junção sem prioridade clara; brechas (*gaps*) insuficientes.
- **Movimento dominante:** a medir.
- **Modos vulneráveis:** *a levantar*.
- **Evidência mínima a coletar:** contagem direcional por movimento + fila por aproximação + conflitos.
- **Benefício público:** organização de acesso e redução de conflito em via municipal.
- **Solução candidata (hipótese):** estudo de redesenho da interseção (canalização, rótula compacta ou semaforização) + medidas operacionais.

### P4 — Fluxo na Av. Vicente Monteggia  ⚠️ prioridade de segurança
- **Sinistros (base EPTC 2010–2026, ≤50 m da malha):** **1.648 ocorr. · 94 graves · 8 fatais · 640 motos · 46 ônibus** (corredor inteiro). *Auxiliar (R02): 409 ocorr. · 36 graves · 2 fatais · 186 motos · 6 ônibus.*
- **Segmentação na base EPTC:** **S06** João Vedana→João Passuelo (248 ocorr., **25 graves**, 2 fatais, 116 motos — o trecho com mais graves); **S03** Otto Niemeyer→Aracaju (320 ocorr., 8 graves, **3 fatais** — o trecho com mais fatais); **S01** ponta Cavalhada/Nonoai (**494 ocorr.**, 1.823/km, 16 graves, 0 fatais — dominado pelo entroncamento com a Av. Cavalhada/Nonoai, *revisar*); S05 Amapá→João Vedana (2 fatais) e S04 Aracaju→Amapá (1 fatal). Ver [segmentos](../dados/tratados/eptc_acidentes_p4_segmentos.csv). *Auxiliar (R03, Dados Abertos POA): S06 67 ocorr., 9 graves, 1 fatal; S01 104; S04 1 fatal — [segmentos](../dados/tratados/acidentes_p4_segmentos.csv).*
- **Problema operacional:** congestionamento/fluxo do corredor.
- **Problema de segurança:** corredor de alta sinistralidade, com fatais e forte presença de motos.
- **Hipótese causal:** corredor **segmentado** (1–3 faixas, vários sentidos únicos — OSM); congestionamento pode ser sintoma de geometria/semáforos e conflitos, não só capacidade.
- **Movimento dominante:** a medir (origem-destino e assimetria por trecho/hora).
- **Modos vulneráveis:** *a levantar* — obrigatório (paradas de ônibus, travessias, motos).
- **Evidência mínima a coletar:** contagem direcional por trecho/hora + velocidades + acidentes por **segmento** + paradas de ônibus.
- **Benefício público:** redução de mortes e feridos graves em corredor municipal.
- **Solução candidata (hipótese):** **diagnóstico de segurança do corredor primeiro**, segmentando por trecho. **Faixa reversível = hipótese condicionada** (ver [avaliacao-solucoes-iniciais.md](avaliacao-solucoes-iniciais.md)). *Não aumentar capacidade sem mitigar risco.*

### P5 — Conversão à direita Av. João Salomoni → Av. da Cavalhada  ⚠️ investigar
- **Sinistros (base EPTC 2010–2026, ≤100 m):** 311 ocorr. · 6 graves · 0 fatais · 57 motos · 22 ônibus. **Contexto ≤200 m:** 418 ocorr. e **1 fatal na Av. Cavalhada (~128 m, 17/04/2025), a validar — não atribuível à conversão.** *Auxiliar (R02): 71 ocorr. · 3 graves · 14 motos · 1 ônibus; contexto 102.*
- **Problema operacional:** conversão à direita problemática (relato).
- **Problema de segurança:** sinistralidade no **entorno** (quase toda em `AV CAVALHADA`); a relação com a conversão João Salomoni → Cavalhada **não está provada** pelos dados.
- **Hipótese causal (a comprovar em campo):** conflito da conversão com travessia e com o fluxo da Cavalhada; raio/visibilidade; interação com ônibus.
- **Movimento dominante:** volume da conversão (a medir).
- **Modos vulneráveis:** *a levantar* — crítico aqui (pedestres na esquina, ônibus).
- **Evidência mínima a coletar:** volume da conversão + conflitos observados + fase semafórica + travessia + ônibus/paradas + raio de giro.
- **Benefício público:** segurança de pedestres e usuários de ônibus em via arterial.
- **Solução candidata (hipótese):** operacional/geométrico de baixo custo (baia/raio, canalização, fase semafórica), **com tratamento explícito de pedestres e ônibus** — **após** confirmar o problema em campo.

### P6 — Acesso à Av. Dr. Vergara (chão batido)
- **Sinistros (base EPTC 2010–2026, ≤50 m):** 36 ocorr. · 2 graves · 0 fatais · 15 motos (vários dos mais próximos estão na Estr. Três Meninas, perto da conexão) — **evidência de sinistro fraca, mesmo na base maior; não usar como argumento central**. *Auxiliar (R02): 8 ocorr.*
- **Problema operacional:** acesso por chão batido (R. Florestan Fernandes + Estr. Kanazawa); rota precária.
- **Achado documental:** o segundo aditamento de 2013 exigiu novos estudos das interseções da Estr. das Três Meninas com **Kanazawa** e **Florestan Fernandes**, seguidos de projetos de pavimento. O Parecer CTAAPS 093/2020 registra projetos aprovados e nenhuma implantação. A obrigação não cobre necessariamente toda a rota até a Av. Dr. Vergara.
- **Checagem OSM:** Estr. Kanazawa `unpaved/dirt`; R. Florestan Fernandes asfalto porém `smoothness=very_bad`, `sidewalk=no`.
- **Problema (eixo do argumento):** **precariedade física** — pavimento, drenagem, calçada, iluminação, seção; risco de tráfego de passagem em via residencial.
- **Hipótese causal:** ausência de rota pavimentada adequada força desvios; via despreparada.
- **Modos vulneráveis:** *a levantar* — moradias lindeiras, pedestres, drenagem.
- **Evidência mínima a coletar:** largura, superfície, drenagem, calçadas, inclinação, iluminação, moradias lindeiras e origem-destino provável; **restrição ambiental/APP e situação fundiária**.
- **Benefício público:** rota mais segura e drenada para moradores do entorno.
- **Solução candidata (hipótese):** **qualificação de rota alternativa** = pavimento + drenagem + seção segura + velocidade baixa + pedestres + controle de tráfego de passagem.

### P7 — Acesso à Estr. Costa Gama bairro→centro (sem conversão à esquerda)
- **Sinistros (base EPTC 2010–2026, ≤100 m):** 67 ocorr. · 6 graves · **1 fatal** (2014, ~89 m; óbito posterior ao acidente) · 17 motos. *Auxiliar (R02): 18 ocorr. · 1 grave.*
- **Problema operacional:** não é possível converter à esquerda; exige retorno em rótula distante.
- **Achado documental:** o expediente-mãe confirma projeto geométrico aprovado para a conexão Três Meninas–Costa Gama, dividido em **primeira etapa sem desapropriação** e **solução definitiva após desapropriações**. Correspondência de 2013 informa que a nova ligação estava aprovada na CTAAPS. O desenho obtido em julho/2026 identifica conector a oeste; o Decreto 20.860/2020 nomeia a **alça de ligação**. A atualização do projeto e sua execução permanecem pendentes.
- **Problema de segurança:** abrir conversão à esquerda pode **criar** conflito pior que o desvio atual.
- **Hipótese causal:** o problema real pode ser a **distância/tempo do retorno**, não a proibição.
- **Evidência mínima a coletar:** distância e tempo do retorno atual + volume do movimento desejado + velocidade na Costa Gama + fila/armazenagem para baia + visibilidade + acidentes no entorno.
- **Modos vulneráveis:** *a levantar*.
- **Benefício público:** redução de quilometragem/tempo improdutivo e de risco no retorno.
- **Solução candidata (hipótese — manter alternativas):** verificar e, se tecnicamente atual, **concluir a conexão/interseção projetada** · alça, somente se confirmada pelo desenho · retorno protegido · conversão semaforizada · rota alternativa · **ou** manter a restrição melhorando o retorno existente.

### P8 — Semáforo Estr. Costa Gama × Estr. Afonso Lourenço Mariante (bairro→centro)
- **Sinistros (base EPTC 2010–2026, ≤100 m):** 124 ocorr. · 11 graves · 0 fatais no limiar (2 fatais só no contexto ≤200 m, em 2018) · 44 motos. Nó OSM ~`-30.1152, -51.1771`. *Auxiliar (R02): 36 ocorr. · 4 graves · 17 motos.*
- **Problema operacional:** longos engarrafamentos no pico.
- **Problema de segurança:** presença relevante de motos.
- **Hipótese causal:** tempos semafóricos/coordenação inadequados; capacidade × demanda no pico.
- **Evidência mínima a coletar:** ciclo + split por aproximação + defasagem com semáforos vizinhos + fila residual após verde + volume por aproximação + ônibus + pedestres.
- **Modos vulneráveis:** *a levantar*.
- **Benefício público:** redução de fila e de risco em interseção semaforizada municipal.
- **Solução candidata (hipótese):** **diagnóstico semafórico-operacional primeiro**. Redesenho/rótula só depois, se a capacidade for de fato o gargalo.

### P9 — Entroncamento Rua Santuário × Av. Oscar Pereira — *preliminar*
- **Origem:** definido na **reunião da comissão de 13/08/2026**, em substituição ao ponto preliminar anterior (rótula Cristiano Kraemer × Juca Batista), **retirado**.
- **Relato:** em dias de maior fluxo, forma-se **fila na Rua Santuário para a conversão à esquerda na Av. Oscar Pereira**.
- **Localização:** -30.096763, -51.178065 (**pin fornecido em 14/08/2026**), entroncamento da Rua Santuário com a Av. Oscar Pereira, em Vila Nova.
- **Sinistros (base EPTC 2010–2026):** **55** pelo limiar de 100 m (6 graves, **1 fatal** em 2014, ~79 m, 26 motos); 67 no contexto de 200 m. Associação por distância — não implica causalidade. *Auxiliar (R02): 17 pelo limiar de 100 m (10 feridos, 2 graves, 0 fatais, 6 motos); 25 no contexto de 200 m; distância mínima 11 m.*
- **Modos vulneráveis:** 26 motos entre os 55 registros da base EPTC (6 entre os 17 da R02); pedestres *a levantar* em campo.
- **Hipótese causal:** capacidade/brechas insuficientes para a conversão à esquerda no pico; prioridade e geometria da aproximação — a definir após vistoria.
- **Evidência mínima a coletar:** volume da conversão à esquerda e da via principal no pico, brechas disponíveis, geometria da aproximação, travessia de pedestres.
- **Benefício público:** *a confirmar* — redução de fila e de manobras de risco em conversão sobre via municipal.
- **Solução candidata (hipótese):** diagnóstico operacional primeiro (prioridade/sinalização/faixa de acumulação); intervenção geométrica só se a vistoria confirmar.

---

## Dimensões adicionais a investigar (contribuição comunitária)
- **Drenagem / alagamento:** dimensão ainda **não mapeada** nos P1–P9 (que são circulação/segurança). Levantar **pontos de alagamento** no entorno da Estr. das Três Meninas e acessos.
- **Escopo regional:** os problemas afetam também o **Terraville** e demais usuários da Zona Sul — reforça o **benefício público além do condomínio**.

## Próximos preenchimentos necessários
- **Sonda:** consolidar os agregados por rota e janela horária, incluindo o índice de estimativas com/sem considerar tráfego e assimetrias entre sentidos no P4/P7, sem isolar o efeito causal de uma intervenção.
- **Sinistros:** **validar por aerofoto e vistoria técnica da EPTC os segmentos P4-S06/S03/S01** e os registros mais próximos — ver [segmentos (EPTC)](../dados/tratados/eptc_acidentes_p4_segmentos.csv), [segmentos (R03, auxiliar)](../dados/tratados/acidentes_p4_segmentos.csv), [revisão manual](../dados/tratados/acidentes_revisao_manual_notas.md) e [metodologia](../dados/tratados/acidentes_metodologia.md).
- **Imagem aérea + base SMAMUS:** confirmar geometria real de cada ponto.
- **Planos oficiais:** zoneamento de Vila Nova no novo PDUS; escopo da requalificação da Av. Monte Cristo.
