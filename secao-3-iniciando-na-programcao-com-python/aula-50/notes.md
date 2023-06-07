# Variáveis, constantes e complexidade de código

> ## **Constantes**

Não existe o conceito de variáveis constantes no Python, mas por convensão é adotado como constante toda variáveis com **todas as letras maíusculas**.

```python
URL = "https://www.python.org/"
```

> ## **Legibilidade**

Não é recomendado `if`s com muitas condições, pois isso aumenta a complexidade do código. Além disso, pode tornar a expressão ambigua e trazendo comportamentos inesperados ao programa:

```python
if condicao1 or condicao2 and condicao3:
  ...
```

Evitar alinhamento de blocos de códigos, seja com estruturas de repetição, condicionais, etc:

```python
if condicao1:
  if condicao2:
    if condicao3:
      ...
    else:
      ...
  else:
    ...
else:
  ...
```

