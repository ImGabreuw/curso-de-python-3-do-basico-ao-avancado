# Funções recursivas, recursividade e Stack Overflow

As funções recursivas são funções que se chamam a si mesmas durante sua execução. Essa técnica é conhecida como recursividade. Ela permite resolver problemas de forma elegante, dividindo-os em subproblemas menores e resolvendo-os em etapas sucessivas.

Ao usar a recursão, é importante definir um caso base que encerre a chamada recursiva e evitar que a função seja chamada infinitamente. Caso contrário, pode ocorrer um estouro de pilha (stack overflow), que é quando a pilha de chamadas recursivas fica tão grande que excede a capacidade de memória disponível.

Vamos ver um exemplo simples de uma função recursiva para calcular o fatorial de um número:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)  # Saída: 120
```

Neste exemplo, a função `factorial` é definida para calcular o fatorial de um número `n`. A recursão é utilizada ao chamar a própria função `factorial` dentro da definição da função. O caso base é quando `n` é igual a 0, retornando 1. Caso contrário, a função chama recursivamente `factorial(n - 1)` e multiplica o resultado por `n`.

No entanto, é importante ter cuidado ao usar recursão, pois é possível ocorrer um estouro de pilha se a recursão não for controlada corretamente. Isso acontece quando a função recursiva é chamada repetidamente sem atingir o caso base. Por exemplo:

```python
def infinite_recursion():
    infinite_recursion()

infinite_recursion()  # Raises RecursionError: maximum recursion depth exceeded
```

Neste exemplo, a função `infinite_recursion` chama a si mesma sem um caso base definido. Isso leva a um estouro de pilha (stack overflow), resultando em um erro `RecursionError`.

Para evitar um estouro de pilha (_Call Stack_), é importante garantir que a recursão atinja um caso base em algum momento. Além disso, é possível definir um limite de recursão, utilizando um contador ou condicionando a recursão a uma condição específica.

Em resumo, as funções recursivas são aquelas que se chamam a si mesmas durante a execução. A recursividade é uma técnica poderosa para resolver problemas dividindo-os em subproblemas menores. No entanto, é necessário definir um caso base para encerrar a recursão e evitar um estouro de pilha (stack overflow).