# Introdução à função lambda + list.sort e sorted

> ## **Método: `sort()`**

Em Python, os métodos `sort()` e `sorted()` são usados para classificar uma lista em ordem crescente ou decrescente. Ambos os métodos são aplicados a objetos do tipo lista, mas têm comportamentos ligeiramente diferentes.

O método `sort()` é um método in-place, o que significa que ele classifica a lista original diretamente, sem criar uma nova lista. Ele modifica a lista existente. A sintaxe básica do método `sort()` é a seguinte:

```python
lista.sort()
```

Aqui está um exemplo simples que usa o método `sort()`:

```python
numeros = [4, 2, 1, 3]
numeros.sort()
print(numeros)  # Saída: [1, 2, 3, 4]
```

Observe que a lista `numeros` foi modificada diretamente e agora está classificada em ordem crescente.

Por outro lado, a função `sorted()` cria uma nova lista contendo os elementos da lista original em ordem classificada, preservando a lista original intacta. A sintaxe básica da função `sorted()` é a seguinte:

```python
nova_lista = sorted(lista)
```

Aqui está um exemplo de uso da função `sorted()`:

```python
numeros = [4, 2, 1, 3]
nova_lista = sorted(numeros)
print(nova_lista)  # Saída: [1, 2, 3, 4]
print(numeros)  # Saída: [4, 2, 1, 3]
```

Nesse exemplo, a função `sorted()` retorna uma nova lista `nova_lista` com os números classificados em ordem crescente, enquanto a lista original `numeros` permanece inalterada.

> **OBS**: a função _sorted()_ realiza o _shallow copy_ para retornar a nova lista.

Em resumo, o método `sort()` classifica a lista original, modificando-a diretamente, enquanto a função `sorted()` cria uma nova lista classificada, deixando a lista original inalterada. A escolha entre os dois métodos depende das necessidades específicas do seu programa.

> ## **Expressão lambda**

Em Python, a palavra-chave `lambda` é usada para criar funções anônimas, também conhecidas como funções lambda. Uma função lambda é uma função sem nome que pode ser usada quando você precisa de uma função simples e de curta duração.

A sintaxe básica de uma função lambda é a seguinte:

```python
lambda argumentos: expressão
```

Uma das aplicações de lambda é na ordenação personalizada usando `sorted()`:

```python
nomes = ['João', 'Maria', 'Ana', 'Pedro']
nomes_ordenados = sorted(nomes, key=lambda x: len(x))
print(nomes_ordenados)  # Saída: ['Ana', 'João', 'Maria', 'Pedro']
```

Neste exemplo, usamos a função `sorted()` para ordenar a lista `nomes` com base no comprimento de cada elemento. A função lambda `lambda x: len(x)` é usada como argumento `key` para indicar que queremos usar o comprimento de cada nome como critério de ordenação.

As funções lambda são úteis em situações em que você precisa de uma função simples e concisa, como em expressões lambda, funções de ordem superior (higher-order functions) e operações de filtragem. No entanto, é importante notar que o uso excessivo de funções lambda pode prejudicar a legibilidade do seu código, especialmente quando as expressões lambda se tornam muito complexas.