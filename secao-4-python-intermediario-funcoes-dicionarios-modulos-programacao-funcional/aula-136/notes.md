# Introdução à List comprehension em Python

_List comprehension_ é uma forma rápida para criar listas a partir de iteráveis.

List comprehension em Python é uma maneira concisa de criar listas a partir de outras listas ou iteráveis. Ele permite combinar um loop `for` e uma expressão condicional em uma única linha, facilitando a criação e transformação de listas de forma eficiente.

A sintaxe básica da _list comprehension_ é a seguinte:

```python
nova_lista = [expressão for elemento in iterável]
```

Isso cria uma nova lista chamada `nova_lista` aplicando a expressão a cada elemento no iterável.

Aqui está um exemplo para ilustrar o uso de _list comprehension_:

```python
numeros = [1, 2, 3, 4, 5]

quadrados = [x ** 2 for x in numeros]
print(quadrados)  # Saída: [1, 4, 9, 16, 25]
```

