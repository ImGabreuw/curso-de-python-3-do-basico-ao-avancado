# enumerate para enumerar valores de iteráveis (pegar índices)

> ## **Definição**

O tipo `enumerate` é uma lista enumerada, ou seja, cada elemento nela é uma tupla contendo o índice e o valor desse elemento na lista.

```python
lista = ["Maria", "Helena", "Luiz"]
lista_enumerada = list(enumerate(lista))

print(lista_enumerada)
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz')]
```

Esse recurso é muito utilizado no `for` juntamente com o desempacotamento dos elementos dentro do `enumerate`:

```python
lista = ["Maria", "Helena", "Luiz"]

for indice, valor in enumerate(lista):
  print(indice, valor)

# 0 Maria
# 1 Helena
# 2 Luiz
```
