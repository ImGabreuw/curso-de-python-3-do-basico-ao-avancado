# filter é um filtro funcional

Em Python, a função `filter` é usada para filtrar os elementos de um iterável (como uma lista) com base em uma função de filtro. Ela retorna um objeto filter, que é um iterador contendo apenas os elementos que atendem à condição especificada pela função de filtro.

A função `filter` recebe dois argumentos: a função de filtro e o iterável. A função de filtro deve ser uma função que retorna um valor booleano (`True` ou `False`) para cada elemento do iterável. Apenas os elementos para os quais a função de filtro retorna True serão incluídos no resultado.

Exemplo:
```python
# Função de filtro para encontrar números pares
def is_even(num):
    return num % 2 == 0

# Lista de números
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrando os números pares usando a função filter
even_numbers = filter(is_even, numbers)

# Convertendo o objeto filter em uma lista para exibir os resultados
result = list(even_numbers)
print(result)  # Output: [2, 4, 6, 8, 10]
```

Neste exemplo, a função `is_even` é usada como a função de filtro. Ela retorna True se o número fornecido for par e False caso contrário. A função `filter` é aplicada à lista de números, filtrando apenas os números pares. Em seguida, o objeto filter é convertido em uma lista para exibir os resultados.

Outra forma comum de usar a função `filter` é com a expressão lambda, que permite criar funções anônimas de forma concisa. Veja um exemplo:

```python
# Lista de números
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrando os números pares usando uma expressão lambda
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Convertendo o objeto filter em uma lista para exibir os resultados
result = list(even_numbers)
print(result)  # Output: [2, 4, 6, 8, 10]
```

Nesse exemplo, a expressão lambda é usada como a função de filtro. Ela verifica se o número é par e retorna True ou False. A função `filter` é aplicada à lista de números, filtrando apenas os números pares.

A função `filter` é uma ferramenta poderosa em Python para filtrar elementos de um iterável com base em condições específicas definidas pela função de filtro.