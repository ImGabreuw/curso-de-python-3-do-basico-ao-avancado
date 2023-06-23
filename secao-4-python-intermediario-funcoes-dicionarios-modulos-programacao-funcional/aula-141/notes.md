# Dictionary Comprehension e Set Comprehension

> ## **Dictionary comprehension**

_Dictionary comprehension_ em Python é uma forma concisa de criar dicionários a partir de uma iteração ou de uma sequência de elementos. Assim como a _list comprehension_, ela permite criar dicionários em uma única linha de código, economizando tempo e tornando o código mais legível.

A sintaxe básica para _dictionary comprehension_ é a seguinte:

```python
novo_dicionario = {chave: valor for elemento in iterável}
```

Isso cria um novo dicionário chamado `novo_dicionario`, onde cada chave e valor são definidos pela expressão aplicada a cada elemento do iterável.

Aqui está um exemplo para ilustrar o uso de _dictionary comprehension_:

```python
numeros = [1, 2, 3, 4, 5]

quadrados = {x: x ** 2 for x in numeros}
print(quadrados)  # Saída: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Nesse exemplo, queremos criar um novo dicionário chamado `quadrados`, onde a chave é cada número da lista `numeros` e o valor é o quadrado correspondente desse número. Utilizamos _dictionary comprehension_ para iterar sobre cada elemento `x` em `numeros` e criar o par chave-valor `{x: x ** 2}` para cada elemento. O resultado é um novo dicionário contendo os quadrados dos números originais.

É possível adicionar uma condição à _dictionary comprehension_ para filtrar os elementos antes de criar os pares chave-valor. Por exemplo:

```python
numeros = [1, 2, 3, 4, 5]

quadrados_pares = {x: x ** 2 for x in numeros if x % 2 == 0}
print(quadrados_pares)  # Saída: {2: 4, 4: 16}
```

Neste exemplo, adicionamos a condição `if x % 2 == 0` à _dictionary comprehension_. Isso filtra apenas os números pares da lista `numeros` antes de criar os pares chave-valor. Portanto, o dicionário resultante `quadrados_pares` contém apenas os quadrados dos números pares.

Além disso, uma outra utilidade do _dictionary comprehension_ é a conversão de uma estrutura de dados parecido com um dicionário em um dicionário:

```python
pseudo_dict = [
  ("a", "valor a"),
  ("b", "valor b"),
  ("c", "valor c"),
]

dc = {
  chave: valor
  for chave, valor in pseudo_dict
}

print(dc)

# Saída: {'a': 'valor a', 'b': 'valor b', 'c': 'valor c'}
```

> **OBS**: a classe `dict()` possui o mesmo comportamento do exemplo acima.

O _dictionary comprehension_ é uma técnica poderosa em Python para criar dicionários de forma concisa e expressiva. Ele permite criar dicionários com base em iterações, aplicar transformações e filtrar elementos, tornando o código mais eficiente e legível.

> ## **Set Comprehension**

_Set comprehension_ em Python é uma forma concisa de criar conjuntos (sets) a partir de uma iteração ou de uma sequência de elementos. Assim como a _list comprehension_ e a _dictionary comprehension_, ela permite criar conjuntos em uma única linha de código, facilitando a criação de conjuntos de forma eficiente e legível.

A sintaxe básica para _set comprehension_ é a seguinte:

```python
novo_conjunto = {elemento for elemento in iterável}
```

Isso cria um novo conjunto chamado `novo_conjunto`, onde cada elemento é definido pela expressão aplicada a cada elemento do iterável. Como os conjuntos não permitem elementos duplicados, o _set comprehension_ é útil para criar conjuntos de elementos únicos.

Aqui está um exemplo para ilustrar o uso de _set comprehension_:

```python
numeros = [1, 2, 2, 3, 3, 4, 5]

conjunto_unico = {x for x in numeros}
print(conjunto_unico)  # Saída: {1, 2, 3, 4, 5}
```

Nesse exemplo, temos uma lista chamada `numeros` que contém alguns elementos duplicados. Utilizamos _set comprehension_ para criar um novo conjunto chamado `conjunto_unico` com todos os elementos únicos da lista. A expressão `{x for x in numeros}` é aplicada a cada elemento de `numeros`, e o conjunto resultante contém apenas os elementos únicos.

Da mesma forma que nas outras compreensões, também é possível adicionar uma condição ao _set comprehension_ para filtrar os elementos antes de criar o conjunto. Por exemplo:

```python
numeros = [1, 2, 3, 4, 5]

conjunto_pares = {x for x in numeros if x % 2 == 0}
print(conjunto_pares)  # Saída: {2, 4}
```

Neste exemplo, adicionamos a condição `if x % 2 == 0` ao _set comprehension_. Isso filtra apenas os números pares da lista `numeros` antes de criar o conjunto. Portanto, o conjunto resultante `conjunto_pares` contém apenas os números pares.

O _set comprehension_ é uma maneira eficiente e legível de criar conjuntos em Python. Ele permite criar conjuntos com base em iterações, filtrar elementos e eliminar duplicatas em uma única linha de código. É uma ótima opção quando você precisa trabalhar com coleções de elementos únicos.