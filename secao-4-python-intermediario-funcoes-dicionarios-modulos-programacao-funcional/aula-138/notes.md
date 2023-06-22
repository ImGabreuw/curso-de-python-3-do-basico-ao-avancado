# Filtro de dados em list comprehension (filter)

> ## **Módulo: `pprint`**

O módulo `pprint` (pretty print) em Python é usado para exibir estruturas de dados de forma mais legível e organizada, especialmente para estruturas complexas, como dicionários e listas aninhadas. Ele fornece recursos adicionais de formatação que ajudam a melhorar a legibilidade do output.

Para utilizar o módulo `pprint`, você precisa importá-lo primeiro:

```python
import pprint
```

Em seguida, você pode usar a função `pprint()` para exibir a estrutura de dados formatada.

Aqui está um exemplo de uso do `pprint`:

```python
import pprint

dados = {
    'nome': 'João',
    'idade': 25,
    'cidade': 'São Paulo',
    'interesses': ['esportes', 'música', 'leitura'],
    'amigos': [
        {'nome': 'Maria', 'idade': 27},
        {'nome': 'Pedro', 'idade': 24},
        {'nome': 'Ana', 'idade': 26}
    ]
}

pprint.pprint(dados)
```

Nesse exemplo, temos um dicionário chamado `dados` com informações pessoais e uma lista de amigos. Ao utilizar `pprint.pprint(dados)`, o `pprint` formata a estrutura de dados de forma mais legível, exibindo os elementos do dicionário e da lista de amigos de forma organizada.

A saída seria:

```python
{'amigos': [{'idade': 27, 'nome': 'Maria'},
            {'idade': 24, 'nome': 'Pedro'},
            {'idade': 26, 'nome': 'Ana'}],
 'cidade': 'São Paulo',
 'idade': 25,
 'interesses': ['esportes', 'música', 'leitura'],
 'nome': 'João'}
```

> **OBS**: o `pprint` indenta os elementos aninhados, tornando mais fácil entender a estrutura do dicionário e da lista.

O `pprint` é especialmente útil quando você lida com estruturas de dados complexas ou grandes, pois ajuda a evitar a saída confusa e desorganizada que ocorre ao usar a função `print()` padrão. Ele melhora a legibilidade do output ao formatar adequadamente os dados exibidos.

> ## **Filtro de dados em _list comprehension_**

O filtro de dados em _list comprehension_ em Python permite aplicar uma condição a cada elemento de uma lista (ou qualquer outro iterável) e criar uma nova lista contendo apenas os elementos que atendem a essa condição. Isso permite filtrar os dados com base em critérios específicos.

A sintaxe para o filtro de dados em _list comprehension_ é a seguinte:

```python
nova_lista = [elemento for elemento in iterável if condição]
```

Isso cria uma nova lista chamada `nova_lista`, onde cada elemento é selecionado do iterável se a condição for verdadeira.

Aqui está um exemplo para ilustrar o filtro de dados em _list comprehension_:

```python
numeros = [1, 2, 3, 4, 5]

pares = [x for x in numeros if x % 2 == 0]
print(pares)  # Saída: [2, 4]
```

Nesse exemplo, queremos criar uma nova lista chamada `pares` que contenha apenas os números pares da lista `numeros`. Usamos a _list comprehension_ para iterar sobre cada elemento `x` em `numeros` e selecionar apenas os elementos que satisfazem a condição `x % 2 == 0`. Assim, a lista resultante `pares` conterá apenas os números pares da lista original.

O filtro de dados em _list comprehension_ pode ser combinado com outras operações, como o mapeamento de dados, para criar listas com transformações e filtros mais complexos. Por exemplo:

```python
numeros = [1, 2, 3, 4, 5]

quadrados_pares = [x ** 2 for x in numeros if x % 2 == 0]
print(quadrados_pares)  # Saída: [4, 16]
```

Neste exemplo, aplicamos o filtro para selecionar apenas os números pares da lista `numeros`, usando a condição `x % 2 == 0`. Em seguida, aplicamos o mapeamento para calcular o quadrado de cada número selecionado. Portanto, a lista resultante `quadrados_pares` contém os quadrados dos números pares da lista original.

O filtro de dados em _list comprehension_ é uma maneira concisa e eficiente de filtrar elementos de uma lista com base em condições específicas. Ele permite criar novas listas contendo apenas os elementos desejados, tornando a manipulação de dados mais simples e legível.