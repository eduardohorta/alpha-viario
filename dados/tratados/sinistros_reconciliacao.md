# Reconciliação das bases de sinistros

> Gerado por `scripts/reconciliar_sinistros.py`. Janela comum: **01/01/2020–31/08/2025**. Associação principal com os mesmos pontos, geometrias e limiares. Os totais oficiais de 2010–2026 não foram alterados.

O cruzamento é por ID, procurando a contraparte nos **brutos completos**, inclusive quando ela não tem coordenada válida. As categorias explicam a inclusão no recorte, não por que a administração alterou ou omitiu o registro. Ausência de um ID não prova ausência do evento, pois não foi feito pareamento probabilístico entre IDs diferentes.

| Ponto | Auxiliar | EPTC | IDs comuns | Só auxiliar | Só EPTC |
|---|---:|---:|---:|---:|---:|
| P1 | 29 | 30 | 24 | 5 | 6 |
| P2 | 58 | 65 | 51 | 7 | 14 |
| P3 | 44 | 53 | 37 | 7 | 16 |
| P4 | 409 | 448 | 393 | 16 | 55 |
| P5 | 71 | 89 | 66 | 5 | 23 |
| P6 | 8 | 8 | 6 | 2 | 2 |
| P7 | 18 | 36 | 18 | 0 | 18 |
| P8 | 36 | 39 | 27 | 9 | 12 |
| P9 | 17 | 20 | 16 | 1 | 4 |

## Decomposição das diferenças

| Presente apenas no recorte | Razão observada na outra base | Associações ID/ponto |
|---|---|---:|
| auxiliar | `coordenada_fora_do_limiar` | 17 |
| auxiliar | `id_ausente_no_bruto` | 35 |
| eptc | `coordenada_fora_do_limiar` | 43 |
| eptc | `coordenada_invalida` | 82 |
| eptc | `id_ausente_no_bruto` | 25 |

São **202 associações divergentes**, correspondentes a **193 IDs**. As linhas por ponto não são somáveis como número de eventos únicos. Não houve divergência de data, feridos, graves, fatais ou motos nas associações comuns.

No P7, os 18 IDs auxiliares também estão no recorte EPTC. Dos 18 adicionais da EPTC, 6 têm coordenada inválida no auxiliar, 11 têm coordenada fora dos 100 m e 1 não consta no bruto auxiliar. Isso não pode ser explicado simplesmente por inclusão de danos materiais.

**Ambas as bases contêm registros sem vítimas registradas.** O auxiliar tem 75.176 linhas; 46437 têm `cont_vit = 0`. Nenhum dos dois processadores aplica filtro de vítimas.

## Rastreabilidade e limites

- [Resumo CSV](sinistros_reconciliacao_resumo.csv), [divergências por ID/ponto](sinistros_reconciliacao_divergencias.csv) e [metadados com hashes](sinistros_reconciliacao_metadata.json). O detalhe contém apenas IDs, datas e distâncias; os brutos permanecem privados.
- Reprodução: `make reconcile-data`, com os dois brutos locais. Não baixa dados nem chama serviços externos.
- Coordenadas diferentes não permitem escolher qual é correta sem boletins/base oficial e validação espacial. Não foram fundidas as bases nem imputadas localizações.
- O ID 804757 aparece duas vezes no contexto ampliado de P1 e de P2 na EPTC, fora desta janela (02/09/2026). Não altera os recortes principais. Mantido como recebido, sem deduplicação silenciosa; totais globais devem distinguir linhas, IDs e pares ID/ponto.
