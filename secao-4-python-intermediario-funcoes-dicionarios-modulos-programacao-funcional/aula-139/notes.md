# List comprehension com mais de um for

_List comprehension_ com mais de um `for` em Python permite criar listas a partir de múltiplas iterações aninhadas. Isso permite combinar valores de diferentes iteráveis em uma única linha, resultando em uma lista composta (matrizes ou tensores).

A sintaxe básica de _list comprehension_ com mais de um `for` é a seguinte:

```python
nova_lista = [expressão for variável1 in iterável1 for variável2 in iterável2]
```

Isso cria uma nova lista chamada `nova_lista`, onde a expressão é aplicada para cada combinação de valores das variáveis das iterações. A ordem das variáveis e iteráveis aninhados é determinada pela ordem em que aparecem na _list comprehension_ (a partir da direita do primeiro `for`).

Aqui está um exemplo para ilustrar o uso de _list comprehension_ com mais de um `for`:

```python
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']

combinacoes = [
  (x, y) 
  for x in numeros 
  for y in letras
]

print(combinacoes)  
# Saída: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]
```

Nesse exemplo, temos duas listas, `numeros` e `letras`. Utilizamos a _list comprehension_ com dois `for` para criar uma lista chamada `combinacoes` que contém todas as combinações possíveis entre os elementos das duas listas. A expressão `(x, y)` cria uma tupla com o elemento `x` de `numeros` e o elemento `y` de `letras`. Assim, a lista resultante `combinacoes` contém todas as combinações de números e letras.

É importante lembrar que a ordem dos `for` na _list comprehension_ determina a ordem das iterações aninhadas. No exemplo acima, primeiro ocorre a iteração sobre `numeros` e, em seguida, a iteração sobre `letras`. Portanto, as combinações são geradas seguindo essa ordem.

A _list comprehension_ com mais de um `for` é uma técnica poderosa para criar listas a partir de múltiplas iterações aninhadas. Ela oferece uma maneira concisa e legível de combinar valores de diferentes iteráveis em uma única lista.