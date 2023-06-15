# Introdução ao empacotamento e desempacotamento

> ## **Desempacotamento**

O conceito de desempacotamento é conhecido em outras linguagens, por exemplo no JavaScript, como _destructuring_. 

Esse recurso consiste em armazenar cada elemento de uma lista, por exemplo, em uma variável utilizando apenas 1 linha.

```python
nome1, nome2, nome3 = ["Maria", "Helena", "Luiz"]

print(nome1) # Maria
print(nome2) # Helena
print(nome3) # Luiz
```

> **IMPORTANTE**: o número de variáveis deve ser o mesmo número de elementos dentro da lista a ser desempacotado. Caso contrário, será lançado um erro `ValueError`

> ## **Empacotamento**

Há casos em que não é necessário desempacotar todos os elementos de uma lista, apenas o 1º. Então para isso usa-se o operador `*` (_rest_) para empacotar os elementos restantes.Por exemplo:

```python
nome1, *resto = ["Maria", "Helena", "Luiz"]

print(nome1) # Maria
print(resto) # ["Helena", "Luiz"]
```

Entretanto, o `resto` pode não ter utilizado no programa, então por convenção é atribuído o nome `_` (_underline_) para variáveis que não são utilizadas.

```python
nome1, *_ = ["Maria", "Helena", "Luiz"]

print(nome1) # Maria
print(_) # ["Helena", "Luiz"]
```