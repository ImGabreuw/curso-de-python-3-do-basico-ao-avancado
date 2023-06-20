# Introdução às funções Python - def define uma função

> ## **Definição**

As funções servem para replicar uma determinada ação ao longo do código.

No Python, é possível criar funções a partir da palavra reservada `def`:

```python
def [nome da função]([parâmetros]) -> [retorno]:
  # Código
```

> O padrão de nomenclatura de função segue o mesmo das variáveis.

Para você chamar um função é preciso colocar os `()` após o nome da dela:

```python
minhaFuncao([argumentos])
```

Os argumentos são valores passados na chamada da função. Eles são obrigatórios caso na assinatura da função tenha parâmetros.

> **OBS**: é possível criar parâmetros opcionais quando é definido um valor padrão

> ## **Exemplo**

```python
def imprimir(a, b, c):
  print(a)
  print(b)
  print(c)

imprimir("olá", "tudo bem", "com você?")
# olá
# tudo bem
# com você?
```