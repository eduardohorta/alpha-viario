# Revisão informacional — 25/09/2026

## Correções aplicadas

- **Bases de sinistros:** removida a caracterização incorreta de Dados Abertos POA como base apenas com vítimas. Ambas as fontes incluem registros sem vítimas registradas. Preservados os totais oficiais e auxiliares; corrigidas a explicação das diferenças, as janelas e as unidades (motos são veículos).
- **Reconciliação:** incluído `make reconcile-data`, com cruzamento por ID na janela 01/01/2020–31/08/2025, procura das contrapartes nos brutos completos, conferência dos derivados e hashes dos insumos. [Relatório reproduzível](../dados/tratados/sinistros_reconciliacao.md).
- **P9:** sincronizadas as referências atuais para Rua Santuário × Av. Oscar Pereira. A rótula Cristiano Kraemer × Juca Batista permanece identificada como referência histórica de D4, retirada do cadastro P9 em agosto. A classificação territorial da nova localização ficou explicitamente pendente.
- **Estado operacional:** atualizados README, roteiro, pendências, checklist e guia; separados marcos históricos das pendências atuais dos 23 pedidos LAI. Registrada a informação recebida em 25/09 de que a comissão está preparando a ata; nenhuma deliberação foi antecipada.
- **Documentação administrativa:** reconciliadas as sínteses das parcelas do P7; retirada a associação residual da faixa Três Meninas 1085 ao P1; corrigido o prazo do Pedido 11. A data de caducidade do projeto P7 deixou de ser inferida como 2024; a confirmação documental é de julho/2026.
- **Ressalvas:** a Cláusula Nona ficou sem vencimento financeiro fechado enquanto não individualizados ato e publicação; a contrapartida do empreendimento vizinho não foi apresentada como financiamento assegurado da solução específica de P1. Atualizada a referência CONTRAN e corrigida a afirmação de fechamento absoluto da janela orçamentária em agosto. Publicação, vetos e transição do PDUS/LUOS continuam por conferir no texto final.
- **Sonda:** corrigidos os conceitos de duração estimada e `staticDuration`, a contagem de rotas e a conclusão causal sobre a alça. Incluída comparação em 145 timestamps de pico comuns às 14 rotas (14/08–01/09), mantendo também os agregados originais. Removida a garantia documental de custo zero; os limites locais e o consumo observado não comprovam a configuração/cobrança em produção.
- **Pacote:** substituída a tabela de textos extensos por fichas; compactadas as tabelas numéricas, com os nomes dos trechos em legenda; atualizadas capa, identidade e data. O pacote foi reconstruído e renderizado para inspeção.
- **Verificadores:** manifesto passou a incluir hash do mapa, do Markdown e do PDF de cada build completo; `--no-pdf` não certifica um PDF antigo. A proteção de links inclui as cinco pastas privadas. O manifesto dos insumos passou a registrar o DBF EPTC. A documentação distingue o CI em modo de desenvolvimento do gate estrito local.

## Resultado da reconciliação

São **202 associações ID/ponto divergentes, correspondentes a 193 IDs**, na janela comum:

| Presença apenas no recorte | Coordenada fora do limiar na outra base | Coordenada inválida na outra base | ID ausente no outro bruto |
|---|---:|---:|---:|
| Auxiliar | 17 | 0 | 35 |
| EPTC | 43 | 82 | 25 |

Todas foram classificadas; as datas e os campos de feridos, graves, fatais e motos coincidem nas associações comuns. No P7, os 18 IDs auxiliares estão entre os 36 da EPTC na mesma janela. Os 18 adicionais correspondem a 6 coordenadas inválidas, 11 coordenadas fora do limiar e 1 ID ausente no auxiliar.

Isso explica a seleção espacial e temporal observada, **não a causa administrativa das diferenças**. Não se escolheu uma coordenada como verdadeira nem se fundiram fontes. A duplicação do ID 804757 no contexto de P1/P2, fora da janela comum, foi documentada e preservada; não afeta os totais principais.

## Validação

- `make reconcile-data`, `make verify-data`, `make check`, `make release-check` e `make test` executados; **59 testes passaram**, incluindo casos de ausência de ID, coordenada inválida, mudança espacial e PDF ausente/alterado/build só Markdown.
- Os quatro insumos presentes no manifesto conferem, incluindo o DBF EPTC.
- Pacote final de **10 páginas** renderizado, todas as páginas inspecionadas e caixas de texto verificadas dentro dos limites físicos das páginas. O texto de P6/P7, antes cortado, aparece integralmente.
- Os arquivos brutos continuam fora do Git. Nenhum envio, protocolo, commit, push ou alteração em serviços de coleta foi realizado nesta revisão.

## O que permanece pendente

1. **Ata em preparação pela comissão**, a incorporar quando disponibilizada; data/comprovante do protocolo principal ainda sem confirmação neste repositório.
2. Respostas/documentos LAI pendentes no [acompanhamento](pedidos-informacao-lai.md#acompanhamento), validação territorial do novo P9 e verificação de implantação em campo.
3. Individualização financeira pela SMF, cobertura específica de P1 pelo TC/projeto e conferência dos textos legais finais do PDUS/LUOS.
4. Conferência da configuração de coleta/cotas e do faturamento no ambiente privado. O bruto local termina em 01/09; isso não comprova que o serviço tenha parado.

Os **12 arquivos não rastreados que já existiam antes desta revisão** foram preservados, incluindo os materiais locais de contextualização/slides e os diretórios `Claude outputs/` e `_to_delete/`. São versões anteriores que **não foram adotadas como peças atuais nem reexportadas**; podem conservar afirmações superadas. Para circulação atual, usar as fontes institucionais corrigidas e o [pacote reconstruído](../pacote-reuniao.md). O extrator inicial de P7 permanece como registro histórico; a reprodução corrente usa o processador completo e a reconciliação acima.
