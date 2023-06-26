# map, partial, GeneratorType e esgotamento de Iterators

Em Python, existem algumas ferramentas úteis para trabalhar com iterações, como as funções `map`, `partial` e o conceito de esgotamento de iterators. Vou explicar cada um deles e dar exemplos para ilustrar seu uso.

### **Map**

A função `map` é usada para aplicar uma determinada função a cada item de um iterável (como uma lista) e retorna um objeto `map`, que é um iterador contendo os resultados. A função `map` recebe dois argumentos: a função a ser aplicada e o iterável.

Exemplo:

```python
# Aplicando a função square a cada elemento da lista
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

# Convertendo o objeto map em uma lista para exibir os resultados
result = list(squared_numbers)
print(result)  # Output: [1, 4, 9, 16, 25]
```

### **Partial**

A função `partial` é usada para criar uma nova função com alguns argumentos pré-definidos a partir de uma função existente. Ela permite fixar os valores de alguns dos argumentos de uma função e retornar uma nova função com os argumentos fixos.

> Essa função função utilizado do conceito de _closure_.

Exemplo:
```python
from functools import partial

# Função original
def multiply(x, y):
    return x * y

# Criando uma nova função com o argumento 'x' fixado em 2
double = partial(multiply, 2)

# Chamando a nova função com o argumento 'y' variável
result = double(5)
print(result)  # Output: 10
```

### **GeneratorType**

O `GeneratorType` é um tipo especial de objeto em Python que é usado para criar geradores. Um gerador é uma função especial que pode ser pausada e retomada em vários pontos de execução. Os geradores são usados para criar iteradores de forma mais eficiente e econômica em termos de memória.

Exemplo:
```python
# Função geradora que produz números pares
def even_numbers():
    num = 0
    while True:
        yield num
        num += 2

# Criando um gerador a partir da função geradora
evens = even_numbers()

# Iterando sobre os primeiros 5 números pares
for _ in range(5):
    print(next(evens))

# Output: 0, 2, 4, 6, 8
```

### **Esgotamento de Iterators**

Em Python, um iterator é um objeto que implementa o método `__next__()` e retorna os próximos elementos em uma sequência. Quando todos os elementos de um iterator são consumidos, ele é esgotado, o que significa que não há mais elementos disponíveis.

Exemplo:
```python
numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
print(next(iterator))  # Raises StopIteration error
```

No exemplo acima, o iterator é criado a partir da lista `numbers`. A função `next()` é usada para obter o próximo elemento do iterator. Quando todos os elementos são consumidos, a chamada subsequente a `next()` resultará em um erro `StopIteration`,indicando que o iterator foi esgotado.