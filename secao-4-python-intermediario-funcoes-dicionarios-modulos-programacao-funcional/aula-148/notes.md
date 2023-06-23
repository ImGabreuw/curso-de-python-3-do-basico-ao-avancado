# yield from em generator functions

O operador `yield from` é uma construção poderosa introduzida no Python 3 que simplifica a implementação de _generator functions_ compostas. Ele permite delegar a geração de valores para outra _generator function_ de forma transparente, evitando a necessidade de escrever loops adicionais.

Ao utilizar o `yield from`, é possível estabelecer uma relação de delegação entre a _generator function_ externa e a _generator function_ interna, permitindo que os valores gerados pela função interna sejam diretamente repassados para a função externa.

Aqui está um exemplo para ilustrar o uso do `yield from`:

```python
def contador_externo():
    yield from contador_interno()

def contador_interno():
    n = 1
    while n <= 3:
        yield n
        n += 1

for num in contador_externo():
    print(num)
```

Nesse exemplo, temos duas _generator functions_: `contador_externo` e `contador_interno`. A função `contador_externo` utiliza o `yield from` para delegar a geração de valores para a função `contador_interno`. A função `contador_interno` gera os números de 1 a 3.

Ao chamar a função `contador_externo` dentro de um loop for, ela atua como um intermediário, passando diretamente os valores gerados pela função `contador_interno` para o loop for. A saída do código será:

```
1
2
3
```

> Os valores gerados pela função `contador_interno` são repassados sem a necessidade de escrever um loop adicional na função `contador_externo`. O `yield from` trata automaticamente a delegação dos valores gerados, simplificando o código.

O `yield from` também pode ser utilizado com iteráveis além de _generator functions_. Isso significa que é possível delegar a iteração de uma lista, por exemplo, para outra _generator function_ usando a mesma sintaxe do `yield from`.

Em resumo, o `yield from` é uma construção útil para criar _generator functions_ compostas, onde é possível delegar a geração de valores para outras _generator functions_ ou iteráveis, evitando a complexidade de escrever loops adicionais.