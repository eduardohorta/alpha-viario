# Checklist de liberação — antes de protocolar

> Companheiro humano do `make release-check` (a verificação automática). Aqui ficam as
> **decisões e preenchimentos da comissão** que a automação não faz sozinha.
> Backlog completo do projeto: [PENDENCIAS.md](PENDENCIAS.md).

## 0. Verificação automática
- [ ] `make release-check` **verde** (modo estrito: links, vazamento de `interno/`/`revisoes/`,
      placeholders e consistência dos pontos).

## 1. A preencher pela comissão (destrava o `release-check`)
- [ ] **Peças externas** — nome, contato e **quem assina**:
      [memorando](relatorios/memorando-externo.md) ·
      [ofício](relatorios/oficio-eptc-rascunho.md) ·
      [anexo](relatorios/anexo-matriz-pontos.md).
- [ ] **Canal de protocolo**: EPTC – Solicitações de Trânsito / Subprefeitura Centro-Sul.
- [ ] **Termos sensíveis**: criar `interno/termos-sensiveis.txt` (nomes reais, um por linha)
      para ligar a checagem de vazamento — arquivo privado, não versionado.

> O [aviso de privacidade](consultas/moradores/aviso-privacidade.md) e o questionário só
> precisam ser preenchidos se a comissão decidir retomá-los. Não são condição para este
> protocolo.

## 2. Rechecagem institucional datada (imediatamente antes de protocolar)
Confirmar, com data, antes de enviar — detalhe e responsáveis em [PENDENCIAS §A](PENDENCIAS.md):
- [ ] **PDUS/LUOS** — sanção/publicação e transição.
- [ ] **Projeto da Av. Monte Cristo** — status atual (EPTC); afeta P2.
- [ ] **Plano Funcional** — desenhos vigentes, reconciliação de estacas e status de implantação (P1/P2/P3/P6/P7); os termos históricos e a execução parcial já estão documentados.
- [ ] **Canais institucionais** da EPTC / Subprefeitura.

## 3. Base de evidência e enquadramento técnico
- [ ] **Sonda de tempos:** consolidar agregados da série de 2–4 semanas (janela, rotas,
      atraso versus fluxo livre e limitações) sem publicar dados brutos da Google Routes API.
- [ ] **LAIs:** incorporar as respostas recebidas ou registrar, na matriz e no protocolo,
      quais pedidos seguem em prazo/prorrogação.
- [ ] **Pedido à EPTC:** manter explícito que o dossiê é indicativo e solicita vistoria
      técnica, contagens, planos semafóricos e demais validações da EPTC/SMMU.

Coleta física comunitária e questionário não são gates deste ciclo; os instrumentos ficam
em espera como referência para eventual vistoria técnica ou mobilização futura.
