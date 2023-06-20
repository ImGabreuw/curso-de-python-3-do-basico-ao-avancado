# Argumentos nomeados e argumentos posicionais (não nomeados) em funções

> ## **Argumento nomeados**

Argumento nomeados são valores definidos de forma explicita para qual parâmetro ele deve ser atribuído.

```python
def soma(x, y):
  print(x + y)

soma(x=1, y=3) # x = 1 e y = 3
soma(y=1, x=3) # x = 1 e y = 3
```

> ## **Argumento não nomeados**

Argumentos não nomeados são chamados de argumentos posicionais, ou seja, o valor atribuído a um parâmetro é baseado na ordem o qual foi inserido.

```python
def soma(x, y):
  print(x + y)

soma(1, 3) # x = 1 e y = 3
soma(3, 1) # x = 3 e y = 1
```