# Retorno de valores das funções (return)

> ## **Retorno de função**

Por padrão toda função retorna **None**, porém é possível alterar o retornar utilizando a palavra reservada `return`.

```python
var = print("Olá")

print(var) # None
```

```python
def soma(x, y):
  return x + y

print(soma(1, 2)) # 3
```

Todo o código inserido após o `return` não será executado:

```python
def soma(x, y):
  return x + y
  # print("Alguma coisa") Nunca é executado

print(soma(1, 2)) # 3
```