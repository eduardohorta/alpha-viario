# Respostas do questionário — pipeline de tabulação

> Torna o crowdsourcing **acionável no dia em que a comissão liberar o questionário**:
> as respostas entram num CSV com esquema fixo e `make respostas` gera o resumo agregado
> (ranking de pontos, perfis, períodos, problemas, medidas) que alimenta a matriz.
>
> **Privacidade (LGPD):** o arquivo bruto `respostas.csv` **não é versionado** (a coluna
> `observacao` pode conter texto livre com dados pessoais). Só o **resumo agregado** pode
> circular — e o resumo gerado também fica fora do versionamento até a comissão decidir
> publicá-lo. Ver [aviso de privacidade](../moradores/aviso-privacidade.md).

## Fluxo

1. Montar o formulário online a partir do [questionário curto](../moradores/questionario-curto.md)
   (Google Forms ou equivalente), com o aviso de privacidade preenchido.
2. Exportar as respostas (CSV/Sheets) e convertê-las ao esquema abaixo —
   uma linha por respondente, colunas na ordem do [modelo](respostas-modelo.csv),
   salvando como `consultas/respostas/respostas.csv`.
3. Rodar `make respostas` (ou `python3 scripts/processar_respostas.py`).
   O resumo sai em `resumo-respostas.md`.
4. Para conferir o gate de volume mínimo do [guia §4](../../relatorios/guia-validacao-comissao.md):
   `python3 scripts/processar_respostas.py --gate 50 --gate-entorno 10`
   *(50/10 é a proposta do gabinete — usar o número que a comissão confirmar).*

## Esquema do CSV

Campos múltiplos usam `;` como separador. Códigos, não rótulos (mapa abaixo).

| Coluna | Conteúdo |
|--------|----------|
| `respondente_id` | `R-0001`, `R-0002`, … (atribuído na consolidação; não identifica a pessoa) |
| `data` | data da resposta, `AAAA-MM-DD` |
| `origem` | `curto` ou `base` (qual questionário) |
| `perfil` | `alphaville` · `entorno` · `trabalha` · `usuario` · `outro` |
| `ponto_mais_critico` | `P1`…`P9` ou `outro` |
| `ponto_outro_texto` | texto livre se `outro` (senão vazio) |
| `periodo_critico` | `pico_manha` · `meio_dia` · `pico_tarde` · `fim_de_semana` · `varia` |
| `problemas` | até 2 de: `congestionamento` · `semaforo` · `conversao` · `velocidade` · `pedestre_ciclista` · `pavimento` · `drenagem` · `acidente` |
| `medidas_apoiadas` | 0+ de: `reducao_velocidade` · `restricao_conversao` · `ajuste_semaforo` · `pavimentar_rota` · `rotula_redesenho` |
| `observacao` | texto livre (campo 6) — **tratar como dado sensível** |

**Mapa rótulo → código** (perguntas do questionário curto):

- P1 *"Você é"*: Morador(a) do Alphaville → `alphaville` · Morador(a) do entorno → `entorno` ·
  Trabalha/presta serviço → `trabalha` · Usa as vias com frequência → `usuario`.
- P3 *"Quando é mais grave"*: Pico da manhã → `pico_manha` · Meio do dia → `meio_dia` ·
  Pico da tarde/noite → `pico_tarde` · Fins de semana → `fim_de_semana` · Varia muito → `varia`.
- P4 *"Principal problema"*: Congestionamento/fila → `congestionamento` · Espera no semáforo →
  `semaforo` · Conversão perigosa → `conversao` · Excesso de velocidade → `velocidade` ·
  Risco para pedestre/ciclista → `pedestre_ciclista` · Pavimento ruim/sem asfalto → `pavimento` ·
  Drenagem/alagamento → `drenagem` · Já vi acidente/quase-acidente → `acidente`.
- P5 *"Medidas que apoiaria"*: Redução de velocidade → `reducao_velocidade` · Restrição de
  conversão → `restricao_conversao` · Ajuste de semáforo → `ajuste_semaforo` · Pavimentar
  vias secundárias → `pavimentar_rota` · Rótula/redesenho → `rotula_redesenho`.

O script valida os códigos e o conjunto de pontos contra o cadastro canônico
(`dados/pontos.csv`) e lista avisos de consistência no fim do resumo.
