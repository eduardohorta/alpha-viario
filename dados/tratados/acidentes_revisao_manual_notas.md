# Notas de revisão manual preliminar - sinistros próximos

Data: 2026-06-04.

Base: `dados/tratados/acidentes_revisao_manual_proximos.csv`, até 20 registros mais próximos por ponto.

## Observações gerais

- A associação por distância é melhor que a bounding box original, mas ainda exige revisão manual dos logradouros.
- Muitos registros têm apenas um logradouro (`log2` vazio), o que impede afirmar o movimento ou a conversão.
- Alguns registros têm coordenada muito próxima do ponto, mas logradouros que sugerem possível geocodificação genérica ou ruído de cadastro.

## Por ponto

### P1

Os registros mais próximos são majoritariamente `ESTR CRISTIANO KRAEMER`, `ESTR TRES MENINAS` ou o par `ESTR CRISTIANO KRAEMER` x `ESTR TRES MENINAS`, coerentes com o ponto. Há, contudo, pelo menos um registro próximo com `ESTR TRES MENINAS` x `ESTR COSTA GAMA`, que sugere erro/ruído de geocodificação ou logradouro secundário inconsistente.

### P2

Há registros coerentes com `ESTR CRISTIANO KRAEMER`, `AV BELEM VELHO` e `AV MONTE CRISTO`, mas também aparecem pares como `AV MONTE CRISTO` x `AV EDUARDO PRADO` entre os mais próximos. Esses casos precisam ser revisados antes de afirmar que pertencem ao nó P2.

### P3

Os registros próximos incluem `AV VICENTE MONTEGGIA`, `ESTR JOAO SALOMONI` e `AV RODRIGUES DA FONSECA`, coerentes com o ponto. Também aparecem registros com `R ATILIO SUPERTTI`, que podem representar o entorno do acesso, mas precisam de validação visual.

### P4

Os registros próximos ao corredor são majoritariamente `AV VICENTE MONTEGGIA`, coerentes com a associação por malha. Como P4 é corredor, os números devem ser segmentados por trecho antes de qualquer proposta.

### P5

Os 20 registros mais próximos são quase todos `AV CAVALHADA`, com apenas dois explicitando `AV CAVALHADA` x `ESTR JOAO SALOMONI`. Portanto, os números de P5 por distância indicam sinistralidade no entorno da conversão, mas ainda não provam que a conversão João Salomoni -> Cavalhada seja o fator causal.

### P6

Os registros mais próximos da geometria Florestan/Kanazawa incluem muitos casos em `ESTR TRES MENINAS`, provavelmente por proximidade à conexão da rota. A evidência de sinistro na rota alternativa em si ainda é fraca; P6 deve seguir fundamentado por precariedade física, drenagem, calçada e potencial de rede, não por sinistralidade.

### P7

Os registros mais próximos são coerentes com `ESTR COSTA GAMA` e `ESTR TRES MENINAS`, inclusive pares explícitos entre as duas vias.

### P8

Os registros mais próximos são majoritariamente `ESTR COSTA GAMA`, `ESTR AFONSO LOURENCO MARIANTE` ou o par entre ambas. Há poucos registros com vias secundárias próximas, que devem ser revisados manualmente.

## Implicação para o memorando

- P4 pode ser mencionado como corredor com indício robusto de gravidade por proximidade à malha.
- P5 deve ser reformulado: há sinistros no entorno da conversão, mas a fatalidade da triagem inicial aparece apenas no contexto ampliado e não deve ser atribuída diretamente à conversão sem validação manual.
- P6 não deve usar sinistros como argumento principal.
