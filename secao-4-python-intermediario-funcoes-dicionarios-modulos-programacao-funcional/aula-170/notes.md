# Solução do Exercício + zip e zip_longest do itertools

A biblioteca `itertools` em Python oferece várias funções úteis para manipulação de iteráveis. Duas dessas funções são `zip()` e `zip_longest()`, que são usadas para combinar elementos de múltiplos iteráveis em pares ordenados.

A função `zip()` combina os elementos de iteráveis correspondentes até que o menor iterável seja esgotado. Ela retorna um objeto `zip` que contém tuplas emparelhadas dos elementos correspondentes dos iteráveis.

Aqui está um exemplo que ilustra o uso da função `zip()`:

```python
frutas = ['maçã', 'banana', 'laranja']
cores = ['vermelho', 'amarelo', 'laranja']

for fruta, cor in zip(frutas, cores):
    print(fruta, '-', cor)
```

Neste exemplo, temos duas listas, `frutas` e `cores`, com elementos correspondentes. Ao usar `zip(frutas, cores)`, obtemos um objeto `zip` que combina os elementos correspondentes das duas listas. No loop `for`, desempacotamos as tuplas emparelhadas em `fruta` e `cor` e imprimimos cada par.

A saída será:

```
maçã - vermelho
banana - amarelo
laranja - laranja
```

A função `zip_longest()` também combina elementos de múltiplos iteráveis, mas continua até que o iterável mais longo seja esgotado. Os elementos emparelhados são preenchidos com um valor padrão quando um iterável é mais curto que os outros.

Aqui está um exemplo que ilustra o uso da função `zip_longest()`:

```python
from itertools import zip_longest

frutas = ['maçã', 'banana', 'laranja']
cores = ['vermelho', 'amarelo']

for fruta, cor in zip_longest(frutas, cores, fillvalue='desconhecido'):
    print(fruta, '-', cor)
```

Neste exemplo, temos duas listas, `frutas` e `cores`. No entanto, a lista `cores` é mais curta que a lista `frutas`. Ao usar `zip_longest(frutas, cores, fillvalue='desconhecido')`, definimos `fillvalue` como `'desconhecido'`, que será usado para preencher os elementos da lista `cores` que são esgotados.

A saída será:

```
maçã - vermelho
banana - amarelo
laranja - desconhecido
```

Observe que o elemento `'laranja'` da lista `frutas` foi combinado com o valor padrão `'desconhecido'` da lista `cores`.

Em resumo, a função `zip()` combina elementos correspondentes de iteráveis até que o menor seja esgotado, enquanto `zip_longest()` continua até que o iterável mais longo seja esgotado, preenchendo os elementos emparelhados com um valor padrão.