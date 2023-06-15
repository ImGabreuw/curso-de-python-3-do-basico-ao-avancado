# Cuidados com tipos de dados mutáveis - list e copy

No caso de estruturas de dados mutáveis como a `list`, o operador de atribuição altera o valor no endereço de memória aonde ele está alocado. Dessa forma, caso seja alterado irá refletir nas outras variáveis que apontam para esse endereço.

```python
lista_a = ["Luiz", "Maria"]
lista_b = lista_a

lista_a[0] = "João"

print(lista_b) # ["João", "Maria"]
```

Para resolver esse problema, usa-se o método `copy()` para copiar todos os valores de uma lista e armazená-las em outro endereço de memória.

```python
lista_a = ["Luiz", "Maria"]
lista_b = lista_a.copy()

lista_a[0] = "João"

print(lista_b) # ["Luiz", "Maria"]
```