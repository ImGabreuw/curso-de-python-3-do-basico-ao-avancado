# (Parte 1) *args para quantidade de argumentos não nomeados variáveis

> ## **Definição**

É possível definir uma quantidade variável de argumentos não nomeados a partir do parâmetro `*args` (convenção). 

Ao utilizar o operador `*`, o Python empacotará todos os argumentos em uma tupla:

```python
def funcao(*args): 
  print(args, type(args))


funcao(1, 2, 3, 4) # (1, 2, 3, 4) <class 'tuple'>
```
> ## **Exemplo**

```python
def soma(*args):
  resultado = 0

  for numero in args:
    resultado += numero

  return resultado

print(soma(1, 2, 3, 4, 5, 6)) # 21
```