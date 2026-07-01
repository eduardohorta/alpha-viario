# Checklist de liberação — antes de circular ou protocolar

> Companheiro humano do `make release-check` (a verificação automática). Aqui ficam as
> **decisões e preenchimentos da comissão** que a automação não faz sozinha.
> Backlog completo do projeto: [PENDENCIAS.md](PENDENCIAS.md).

## 0. Verificação automática
- [ ] `make release-check` **verde** (modo estrito: links, vazamento de `interno/`/`revisoes/`,
      placeholders e consistência dos pontos).

## 1. A preencher pela comissão (destrava o `release-check`)
- [ ] **Aviso de privacidade** ([arquivo](consultas/moradores/aviso-privacidade.md)):
      **responsável** (nome + e-mail/telefone) e **prazo de retenção**.
- [ ] **Peças externas** — nome, contato e **quem assina**:
      [memorando](relatorios/memorando-externo.md) ·
      [ofício](relatorios/oficio-eptc-rascunho.md) ·
      [anexo](relatorios/anexo-matriz-pontos.md).
- [ ] **Canal de protocolo**: EPTC – Solicitações de Trânsito / Subprefeitura Centro-Sul.
- [ ] **Gate de campo** ([guia §4](relatorios/guia-validacao-comissao.md)):
      definir o **volume mínimo de respostas** do questionário.
- [ ] **Termos sensíveis**: criar `interno/termos-sensiveis.txt` (nomes reais, um por linha)
      para ligar a checagem de vazamento — arquivo privado, não versionado.

## 2. Rechecagem institucional datada (imediatamente antes de protocolar)
Confirmar, com data, antes de enviar — detalhe e responsáveis em [PENDENCIAS §A](PENDENCIAS.md):
- [ ] **PDUS/LUOS** — sanção/publicação e transição.
- [ ] **Projeto da Av. Monte Cristo** — status atual (EPTC); afeta P2.
- [ ] **Plano Funcional** — desenhos vigentes, reconciliação de estacas e status de implantação (P1/P2/P3/P6/P7); os termos históricos e a execução parcial já estão documentados.
- [ ] **Canais institucionais** da EPTC / Subprefeitura.

## 3. Evidência de campo
Mínimo suficiente para protocolar: [guia §4](relatorios/guia-validacao-comissao.md).
Registrar tudo no [inventário de evidências](campo/observacoes/inventario-evidencias.csv).
