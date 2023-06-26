# reduce - faz a redução de um iterável em um valor

Em Python, a função `reduce` é uma função de ordem superior (recebe um função redutora como argumento) que permite reduzir uma sequência de elementos a um único valor, aplicando repetidamente uma função a pares de elementos consecutivos.

No entanto, a função `reduce` não é uma função interna do Python padrão desde a versão 3.x. Ela foi movida para o módulo `functools`. Portanto, para usar a função `reduce`, você precisa importá-la do módulo `functools`.

Exemplo:
```python
from functools import reduce

# Função de redução para calcular a soma de uma lista de números
def somar(acumulador, numero_atual):
    return acumulador + numero_atual

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usando a função reduce para calcular a soma
result = reduce(somar, numeros, 0)
print(result)  # Saída: 15
```

Neste exemplo, a função `somar` é usada como a função de redução. Ela recebe dois argumentos, `acumulador` (iniciando em 0) e `numero_atual`, e retorna a soma desses dois valores. A função `reduce` é aplicada à lista de números, reduzindo-a a um único valor, que é a soma de todos os elementos.

Você também pode usar uma expressão lambda como a função de redução para tornar o código mais conciso:

```python
from functools import reduce

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usando uma expressão lambda para calcular a soma usando reduce
result = reduce(
  lambda acumulador, numero_atual: acumulador + numero_atual, 
  numeros, 0
)
print(result)  # Saída: 15
```

Nesse exemplo, a expressão lambda `lambda acumulador, numero_atual: acumulador + numero_atual` é usada como a função de redução. Ela recebe dois argumentos, `acumulador` (iniciando em 0) e `numero_atual`, e retorna a soma desses dois valores. A função `reduce` é aplicada à lista de números, reduzindo-a a um único valor, que é a soma de todos os elementos.

A função `reduce` pode ser usada para realizar várias operações de redução em sequências, como encontrar o produto de uma lista de números, encontrar o valor máximo ou mínimo, concatenar strings, entre outros. A escolha da função de redução depende do resultado desejado.