# Checklist de liberação — antes de protocolar

> Companheiro humano do `make release-check` (a verificação automática). Aqui ficam as
> **decisões e preenchimentos da comissão** que a automação não faz sozinha.
> **Decisões da reunião de 13/08/2026 incorporadas** (ata em `interno/ata-reuniao-2026-08-13.md`).
> Backlog completo do projeto: [PENDENCIAS.md](PENDENCIAS.md).

## 0. Verificação automática
- [ ] `make release-check` **verde** (modo estrito: links, vazamento de `interno/`/`revisoes/`,
      placeholders e consistência dos pontos). Executar novamente para cada versão enviada; ver §4.

## 1. Decisões da comissão (13/08/2026) — destravam o `release-check`
- [x] **Identidade e assinatura:** peças assinadas por **Eduardo de Oliveira Horta (representante)**
      pela **Comissão Viária Estrada das Três Meninas**; contato **comissao.viaria@outlook.com**.
      *(número e data do ofício ficam para o ato do protocolo.)*
      Peças atualizadas: [memorando](relatorios/memorando-externo.md) ·
      [ofício](relatorios/oficio-eptc-rascunho.md) · [anexo](relatorios/anexo-matriz-pontos.md).
- [x] **Canal de protocolo:** **SMAMUS (principal)**, com cópia à **EPTC/SMMU** e às
      **Subprefeituras Centro-Sul e Glória**. As peças pedem que a SMAMUS articule a EPTC para a
      parte de trânsito (vistoria, contagens, semáforos).
- [x] **Lista de pontos:** **P1–P8 + novo P9** (entroncamento Rua Santuário × Av. Oscar Pereira);
      o antigo P9 (rótula Cristiano Kraemer × Juca Batista) foi **retirado**.
- [x] **Demandas D2/D3:** **incluídas** nas peças em **versão genérica** (retorno seguro; avaliação
      de capacidade da Cristiano Kraemer), sem detalhe de condomínio.
- [x] **Questionário:** **em espera** (não é condição do protocolo).
- [x] **Sensibilidade (o que tornar público):** itens 1–5 **privados por ora** (peças em versão
      conservadora); material de contextualização **restrito aos membros**; **repositório público** (os membros
      acessam sem login no GitHub; o cuidado é com dados pessoais de terceiros e documentos não
      públicos, que ficam fora do Git, em `interno/` e `retornos-protocolos/`); sinistros: **dados
      abertos** (Dados Abertos POA e base da EPTC obtida por LAI), que podem ser publicados também por
      registro, por serem anônimos (sem identidade de vítimas).
- [x] **Termos sensíveis:** `interno/termos-sensiveis.txt` **criado**
      — 23 termos conferidos na inspeção de 25/09; atualizar a lista privada antes de cada envio.

## 2. Rechecagem institucional — posição de 09/11/2026
- [ ] **Ata:** a ata da reunião com a EPTC (22/09) foi recebida em 08/10/2026, em versão revisada ainda não final; fechar a versão (no P5, "Dr Vergara" vira "Estr. João Vedana") e cumprir os encaminhamentos (ver [PENDENCIAS.md](PENDENCIAS.md)).
- [ ] **Protocolo principal:** não realizado (confirmado pela comissão em 08/10/2026); a comissão articula reunião com a SMAMUS. Decidir se o ofício segue como protocolo ou como apoio à reunião; número e data só no ato do envio.
- [ ] **LAIs:** 30 pedidos protocolados. Acompanhar os vencidos 24, 27 e 30, em espera por decisão de 09/11 (24 e 27) e 10/11 (30); o 14 foi respondido em 10/11, só sobre o esgoto (certidão de 2013 do coletor tronco do loteamento; rede de água sem resposta; fechado sem reexame em 10/11) (o 18 foi respondido sem localização em 30/09 e remetido à SMAMUS, gerando o 24); o 20 em 15/10 (intermediária) e 26/10 (planta e planilha por e-mail); o 21 foi respondido em 16/09, o 19 em 14/10, em parte (reexame do item "d" apresentado no mesmo dia e indeferido em 27/10: documentos preparatórios); o 23 em 19/10, em parte (TAC do MP não localizado; arquivado sem reexame); o 25 em 05/11, pela PGM (projeto de drenagem não elaborado, adiado até a conclusão das desapropriações; reexame sobre o responsável apresentado em 09/11, prazo final 19/11); o 26 em 05/11 (Parecer 985/1997, Informação 4084/2022 e situação dos quatro processos, sem cronograma; fecha o 16); o 29 em 09/11, em parte (expedientes dos P8 e P5, sem contrapartida confirmada; reexame do item 1 apresentado no mesmo dia, prazo final 19/11); e o 28 em 09/11, em parte (demolição designada para 28/10 e executada, segundo a comissão; sem notificação ao empreendedor; reexame apresentado no mesmo dia, prazo final 19/11). Consultar os prazos na [tabela atual](relatorios/pedidos-informacao-lai.md#acompanhamento).
- [ ] **LOA 2027:** envio do projeto até 15/out (data já passada; conferir o envio) e votação até 5/dez, conforme [fonte municipal](https://prefeitura.poa.br/smpg/lei-orcamentaria-anual-loa). Confirmar viabilidade orçamentária do pleito; o calendário não garante recursos.
- [ ] **PDUS/LUOS:** conferir textos finais, vetos, publicação, transição e parâmetros aplicáveis; a resposta do Pedido 6 inclui referências a minutas.
- [ ] **P2:** acompanhar a manifestação da EPTC sobre o nó da Monte Cristo. A SMMU informou (Pedido 5) que o projeto *implantado* no nó é da GPTC-EPTC; a ata de 22/09 registra que o trevo "não possui nenhum projeto atualmente" (compatível: sem projeto de melhoria). O Pedido 30 (EPTC, 018518-26-45, prazo 09/11) pergunta se há estudo ou proposta.
- [ ] **Desenhos e execução:** manter distinta a aprovação histórica, a validade atual, a situação fundiária e a implantação física.
- [ ] **Canais:** confirmar setor de protocolo, encaminhamento das cópias e enquadramento territorial do novo P9.

## 3. Base de evidência e enquadramento técnico
- [x] **Sonda local:** 8.582 medições, 14 rotas, 04/07–01/09/2026; [resumo](dados/tratados/sonda_tempos_resumo.md). R05/R06 medem assimetria direcional, sem isolar o efeito da alça. Coleta pausada em 01/11/2026; a série até essa data só precisa ser reagregada se a comissão quiser usá-la.
- [x] **Sinistros:** base EPTC principal, auxiliar sem filtro de vítimas e [reconciliação por ID na janela comum](dados/tratados/sinistros_reconciliacao.md).
- [x] **Novo P9:** Rua Santuário × Av. Oscar Pereira, pin de 14/08; 55 sinistros EPTC e 17 auxiliares.
- [ ] **LAIs:** incorporar respostas futuras e manter pendências datadas.
- [ ] **Pedido institucional:** preservar o caráter indicativo, a solicitação de vistoria e a validação pela autoridade competente.

## 4. Residuais para o ato do protocolo
- Confirmar número/data do ofício (atualmente nº 01/2026, setembro de 2026; a data já passou e deve ser ajustada no ato).
- Gerar `make pacote` e executar `make release-check`; verificar visualmente o PDF. O gate automático não certifica o conteúdo jurídico nem substitui essa inspeção.
- Conferir a lista privada de termos sensíveis e os anexos que efetivamente serão enviados.

Coleta física comunitária e questionário não são gates deste ciclo.
