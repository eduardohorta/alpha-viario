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

## 2. Rechecagem institucional — posição de 25/09/2026 (atualizada em 08/10/2026)
- [ ] **Ata:** a ata da reunião com a EPTC (22/09) foi recebida em 08/10/2026, em versão revisada ainda não final; fechar a versão e cumprir os encaminhamentos (ver [PENDENCIAS.md](PENDENCIAS.md)).
- [ ] **Protocolo principal:** não realizado (confirmado pela comissão em 08/10/2026); a comissão articula reunião com a SMAMUS. Decidir se o ofício segue como protocolo ou como apoio à reunião; número e data só no ato do envio.
- [ ] **LAIs:** 30 pedidos protocolados. Acompanhar 14, documentos restantes do 16 (Pedido 26), respostas 19/20/23/24/25/26/27/28/29/30 (o 18 foi respondido sem localização em 02/10 e remetido à SMAMUS, gerando o 24); o 21 foi respondido em 16/09. Consultar os prazos na [tabela atual](relatorios/pedidos-informacao-lai.md#acompanhamento).
- [ ] **LOA 2027:** envio do projeto até 15/out e votação até 5/dez, conforme [fonte municipal](https://prefeitura.poa.br/smpg/lei-orcamentaria-anual-loa). Confirmar viabilidade orçamentária do pleito; o calendário não garante recursos.
- [ ] **PDUS/LUOS:** conferir textos finais, vetos, publicação, transição e parâmetros aplicáveis; a resposta do Pedido 6 inclui referências a minutas.
- [ ] **P2:** acompanhar a manifestação da EPTC sobre o nó da Monte Cristo. A SMMU informou (Pedido 5) que o projeto *implantado* no nó é da GPTC-EPTC; a ata de 22/09 registra que o trevo "não possui nenhum projeto atualmente" (compatível: sem projeto de melhoria). O Pedido 30 (EPTC, 018518-26-45, prazo 28/10) pergunta se há estudo ou proposta.
- [ ] **Desenhos e execução:** manter distinta a aprovação histórica, a validade atual, a situação fundiária e a implantação física.
- [ ] **Canais:** confirmar setor de protocolo, encaminhamento das cópias e enquadramento territorial do novo P9.

## 3. Base de evidência e enquadramento técnico
- [x] **Sonda local:** 8.582 medições, 14 rotas, 04/07–01/09/2026; [resumo](dados/tratados/sonda_tempos_resumo.md). R05/R06 medem assimetria direcional, sem isolar o efeito da alça. Conferir série posterior em produção quando necessário.
- [x] **Sinistros:** base EPTC principal, auxiliar sem filtro de vítimas e [reconciliação por ID na janela comum](dados/tratados/sinistros_reconciliacao.md).
- [x] **Novo P9:** Rua Santuário × Av. Oscar Pereira, pin de 14/08; 55 sinistros EPTC e 17 auxiliares.
- [ ] **LAIs:** incorporar respostas futuras e manter pendências datadas.
- [ ] **Pedido institucional:** preservar o caráter indicativo, a solicitação de vistoria e a validação pela autoridade competente.

## 4. Residuais para o ato do protocolo
- Confirmar número/data do ofício (atualmente nº 01/2026, setembro de 2026).
- Gerar `make pacote` e executar `make release-check`; verificar visualmente o PDF. O gate automático não certifica o conteúdo jurídico nem substitui essa inspeção.
- Conferir a lista privada de termos sensíveis e os anexos que efetivamente serão enviados.

Coleta física comunitária e questionário não são gates deste ciclo.
