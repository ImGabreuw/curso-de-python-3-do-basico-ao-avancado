# groupby - agrupando valores (itertools)

A função `groupby()` do módulo `itertools` em Python é usada para agrupar elementos consecutivos em iteráveis com base em uma chave de agrupamento. Ela retorna um iterador que produz pares de chave e grupos de elementos que compartilham a mesma chave.

No exemplo abaixo, temos uma lista de dicionários chamada `alunos`, onde cada dicionário representa um aluno com um nome e uma nota. Vamos usar a função `groupby()` para agrupar os alunos com base nas suas notas.

Aqui está o código que demonstra como usar a função `groupby()` com o exemplo fornecido:

```python
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

alunos.sort(key=lambda x: x['nota'])  # Ordena os alunos por nota

for nota, grupo in groupby(alunos, key=lambda x: x['nota']):
    print(f'Alunos com nota {nota}:')
    for aluno in grupo:
        print(aluno['nome'])
    print()
```

Neste exemplo, primeiro ordenamos a lista de alunos pelo campo `'nota'` usando `alunos.sort(key=lambda x: x['nota'])`. Isso garante que os alunos com a mesma nota fiquem agrupados consecutivamente.

Em seguida, usamos a função `groupby()` passando a lista de alunos e uma função lambda que extrai a chave de agrupamento (`x['nota']`). O resultado é um iterador que produz pares de chave e grupos de alunos que compartilham a mesma nota.

No loop `for`, percorremos o iterador `groupby` e imprimimos cada grupo de alunos com a mesma nota. A variável `nota` contém a chave de agrupamento, e `grupo` contém os alunos que compartilham essa nota. Imprimimos o nome de cada aluno dentro do grupo.

A saída será:

```
Alunos com nota A:
Luiz
Fabrício
João
André

Alunos com nota B:
Letícia
Eduardo

Alunos com nota C:
Rosemary
Anderson

Alunos com nota D:
Joana
```

Observa-se que os alunos foram agrupados com base nas suas notas. Cada grupo é impresso separadamente, mostrando os alunos que compartilham a mesma nota.

É importante sempre ordenar os dados antes de agrupar, pois caso tenha uma chave já existe, mas fora de ordem, a função interpretará como uma nova chave:

```python
from itertools import groupby

alunos = ["a", "a", "a", "b", "c", "a"]
grupos = groupby(alunos)

for chave, grupo in grupos:
  print("Grupo:", chave)
  print(list(grupo))
```

Saída do exemplo acima:

```console
Grupo: a
['a', 'a', 'a']
Grupo: b
['b']
Grupo: c
['c']
Grupo: a
['a']
```

Em resumo, a função `groupby()` do módulo `itertools` é útil para agrupar elementos consecutivos em iteráveis com base em uma chave de agrupamento. No exemplo fornecido, usamos `groupby()` para agrupar os alunos com base nas suas notas e imprimir os grupos correspondentes.