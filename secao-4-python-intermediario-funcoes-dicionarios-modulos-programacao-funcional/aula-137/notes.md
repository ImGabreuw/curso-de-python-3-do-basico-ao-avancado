# Mapeamento de dados em list comprehension (map)

O mapeamento de dados em _list comprehension_ em Python refere-se à aplicação de uma função a cada elemento de uma lista (ou qualquer outro iterável) para criar uma nova lista com os resultados. Em outras palavras, ele permite mapear uma função em cada elemento de uma lista, transformando-os de acordo com a lógica definida na função.

A sintaxe para o mapeamento de dados em _list comprehension_ é a seguinte:

```python
nova_lista = [funcao(elemento) for elemento in iteravel]
```

Isso aplica a função `funcao()` a cada elemento no iterável e cria uma nova lista chamada `nova_lista` com os resultados.

Aqui está um exemplo para ilustrar o mapeamento de dados em _list comprehension_:

```python
produtos = [
  {"nome": "p1", "preco": 20},
  {"nome": "p2", "preco": 10},
  {"nome": "p3", "preco": 30},
]

novos_produtos = [
  {**produto, "preco": produto["preco"] * 1.05}
  for produto in produtos
]

print(*novos_produtos, sep="\n")
```

Saída do exemplo acima:

```
{'nome': 'p1', 'preco': 21.0}
{'nome': 'p2', 'preco': 10.5}
{'nome': 'p3', 'preco': 31.5}
```

Nesse exemplo, queremos criar uma nova lista chamada `novos_produtos` que contenha o preço do produto acrescido de 5% para cada produto na lista `produtos`. Utilizamos a _list comprehension_ para iterar sobre cada elemento `produto` em `produtos` e aplicar a função `{**produto, "preco": produto["preco"] * 1.05}` a cada elemento. O resultado é uma nova lista com o preço do produto reajustado.

O mapeamento de dados em _list comprehension_ pode ser combinado com a presença de uma cláusula `if` para filtrar elementos antes de aplicar a função. Por exemplo:

```python
produtos = [
  {"nome": "p1", "preco": 20},
  {"nome": "p2", "preco": 10},
  {"nome": "p3", "preco": 30},
]

novos_produtos = [
  {**produto, "preco": produto["preco"] * 1.05}
  if produto["preco"] > 20 else {**produto}
  for produto in produtos
]

print(*novos_produtos, sep="\n")
```

Saída do exemplo acima:

```
{'nome': 'p1', 'preco': 20}
{'nome': 'p2', 'preco': 10}
{'nome': 'p3', 'preco': 31.5}
```

Neste exemplo, além de reajusta o preço do produto em 5%, utilizamos a cláusula `if produto["preco"] > 20` para filtrar apenas os produtos com preço superior a 20 reais da lista `produtos`. Dessa forma, a função `{**produto, "preco": produto["preco"] * 1.05}` é aplicada somente aos produtos com preço maior do que 20 reais, resultando em uma nova lista chamada `novos_produtos`.

O mapeamento de dados em _list comprehension_ é uma forma concisa e eficiente de aplicar uma função a cada elemento de uma lista e criar uma nova lista com os resultados. Ele facilita a transformação dos dados de forma rápida e legível.
