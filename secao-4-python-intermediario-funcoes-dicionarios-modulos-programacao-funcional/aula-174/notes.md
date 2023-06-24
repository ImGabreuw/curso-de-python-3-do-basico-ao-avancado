# Combinations, Permutations e Product - Itertools

A biblioteca `itertools` em Python oferece várias funções úteis para manipulação de iteráveis. Três dessas funções são `combinations()`, `permutations()` e `product()`, que geram combinações, permutações e produtos cartesianos de elementos de iteráveis.

A função `combinations()` retorna todas as combinações possíveis de um determinado tamanho a partir de um iterável de entrada, sem repetição.

Aqui está um exemplo que ilustra o uso da função `combinations()`:

```python
from itertools import combinations

letras = ['A', 'B', 'C', 'D']

for combinacao in combinations(letras, 2):
    print(combinacao)
```

Neste exemplo, temos uma lista `letras` com os elementos `'A'`, `'B'`, `'C'` e `'D'`. Ao usar `combinations(letras, 2)`, geramos todas as combinações possíveis de tamanho 2 a partir dos elementos da lista `letras`. No loop `for`, iteramos sobre as combinações geradas e as imprimimos.

A saída será:

```
('A', 'B')
('A', 'C')
('A', 'D')
('B', 'C')
('B', 'D')
('C', 'D')
```

A função `permutations()` retorna todas as permutações possíveis de um determinado tamanho a partir de um iterável de entrada, sem repetição.

Aqui está um exemplo que ilustra o uso da função `permutations()`:

```python
from itertools import permutations

letras = ['A', 'B', 'C']

for permutacao in permutations(letras, 2):
    print(permutacao)
```

Neste exemplo, temos uma lista `letras` com os elementos `'A'`, `'B'` e `'C'`. Ao usar `permutations(letras, 2)`, geramos todas as permutações possíveis de tamanho 2 a partir dos elementos da lista `letras`. No loop `for`, iteramos sobre as permutações geradas e as imprimimos.

A saída será:

```
('A', 'B')
('A', 'C')
('B', 'A')
('B', 'C')
('C', 'A')
('C', 'B')
```

A função `product()` retorna o produto cartesiano de dois ou mais iteráveis, que é uma combinação de todos os elementos dos iteráveis de entrada.

Aqui está um exemplo que ilustra o uso da função `product()`:

```python
from itertools import product

numeros = [1, 2]
letras = ['A', 'B']

for produto in product(numeros, letras):
    print(produto)
```

Neste exemplo, temos uma lista `numeros` com os elementos `1` e `2`, e uma lista `letras` com os elementos `'A'` e `'B'`. Ao usar `product(numeros, letras)`, geramos o produto cartesiano entre os dois iteráveis. No loop `for`, iteramos sobre os produtos gerados e os imprimimos.

A saída será:

```
(1, 'A')
(1, 'B')
(2, 'A')
(2, 'B')
```

Em resumo, as funções `combinations()`, `permutations()` e `product()` da biblioteca `itertools` permitem gerar combinações, permutações e produtos cartesianos de elementos de iteráveis, respectivamente. Essas funções são úteis para realizar operações combinatórias em Python.