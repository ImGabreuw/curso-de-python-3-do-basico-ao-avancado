# Introdução ao try e except para capturar erros (exceptions)

> ## **Definição**

A estrutura `try-except` serve para prevenir um código de ter sua execução interrompida por causa do lançamento de um erro, geralmente esperado.

Essa estrutura é dividida em 2 blocos:

1. Bloco `try`: tenta executar um código

2. Bloco `except`: captura um erro laçado no bloco `try`

É uma boa prática especificar o erro esperado no bloco `except`:

- Não é recomendado:

  ```python
  try:
    ...
  except:
    ...

  # OU

  try:
    ...
  except Exception:
    ...
  ```

- Recomendado:

  ```python
  try:
    ...
  except ValueError:
    ...
  ```

> Não utilizar erros genéricos como `BaseException`, `Exception`

Além disso, é possível obter os dados do erro lançado no bloco `except` atribuindo um rótulo ao erro com `as`:

```python
try:
  num = int("a")

  print(num)
except ValueError as e:
  print(e) # invalid literal for int() with base 10: 'a'
```

> ## **Exemplo**

```python
num = int("a")

print(num)

# Traceback (most recent call last):
#   File "/home/gabriel/Projects/curso-de-python-3-do-basico-ao-avancado/secao-3-iniciando-na-programcao-com-python/aula-49/example-2.py", line 1, in <module>
#     num = int("a")
# ValueError: invalid literal for int() with base 10: 'a'
```

Como foi possível ver no código acima, era esperado que `num = int("a")` lançaria um erro, uma vez que não é possível converter uma letra em um número inteiro. Dessa forma, o erro `ValueError` já era esperado.

Então para resolver esse possível cenário, basta utilizar a estrutura `try-except`:

```python
try:
  num = int("a")

  print(num)
except ValueError:
  print("Número inválido")
```
