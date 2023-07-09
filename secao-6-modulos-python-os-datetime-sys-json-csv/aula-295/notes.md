# random tem geradores de números pseudoaleatórios (randrange, randint, uniform)

O módulo `random` do Python fornece funções para gerar números pseudoaleatórios. Esses números são gerados por algoritmos determinísticos que parecem se comportar de maneira aleatória, mas podem ser reproduzidos se você conhecer a semente (ou seja, o valor inicial) usada.

**IMPORTANTE**: este módulo não deve ser utilizado para fins de segurança ou uso criptográfico, devido a natureza previsível do algoritmo utilizado pelo módulo.

### `randrange(start, stop, step)`

A função `randrange()` gera um número inteiro aleatório dentro de um intervalo especificado. Você pode fornecer um valor de início, um valor de parada (exclusivo) e um valor de passo opcional. Se nenhum valor de passo for fornecido, o padrão será 1. Aqui está um exemplo:

```python
import random

# Gerar um número aleatório par entre 0 e 11 (exclusivo)
numero = random.randrange(0, 11, 2)
print(numero)
```

### `randint(a, b)`

A função `randint()` gera um número inteiro aleatório dentro de um intervalo fechado, incluindo ambos os extremos. Você precisa fornecer os valores mínimo e máximo do intervalo. Aqui está um exemplo:

```python
import random

# Gerar um número aleatório entre 1 e 10 (inclusivo)
numero = random.randint(1, 10)
print(numero)
```

### `uniform(a, b)`

A função `uniform()` gera um número de ponto flutuante aleatório dentro de um intervalo especificado. Você precisa fornecer os valores mínimo e máximo do intervalo. Aqui está um exemplo:

```python
import random

# Gerar um número aleatório entre 0 e 1
numero = random.uniform(0, 1)
print(numero)
```

O segundo argumento (no caso `1`) pode ser inclusivo ou exclusivo dependendo do critério de arredondamento que o você adotar.
