# isinstance() - para saber se objeto é de determinado tipo

A função `isinstance()` em Python é utilizada para verificar se um objeto pertence a um determinado tipo. Ela retorna `True` se o objeto for do tipo especificado e `False` caso contrário.

A sintaxe básica da função `isinstance()` é a seguinte:

```python
isinstance(objeto, tipo)
```

- `objeto`: O objeto a ser verificado.

- `tipo`: O tipo que se deseja verificar.

A função `isinstance()` é útil quando se deseja realizar operações condicionais com base no tipo de um objeto.

Aqui está um exemplo de uso da função `isinstance()`:

```python
lista = ["a", 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {"nome": "Luiz"}]

for elemento in lista:
    if isinstance(elemento, set):
        print(f"O elemento {elemento} é um conjunto.")
    elif isinstance(elemento, list):
        print(f"O elemento {elemento} é uma lista.")
    elif isinstance(elemento, dict):
        print(f"O elemento {elemento} é um dicionário.")
    elif isinstance(elemento, (int, float))
        print(f"O elemento {elemento} é um número.")
    else:
        print(f"O elemento {elemento} não é um número, conjunto, lista ou dicionário.")
```

Neste exemplo, temos uma lista chamada `lista` com diferentes tipos de objetos. Utilizamos um loop `for` para percorrer cada elemento da lista. Em seguida, utilizamos a função `isinstance()` para verificar o tipo de cada elemento.

No corpo do loop, temos condições `if` e `elif` que verificam se o elemento é do tipo desejado. Se a condição for verdadeira, uma mensagem específica é exibida. Caso contrário, uma mensagem genérica é exibida indicando que o tipo não é um conjunto, lista ou dicionário.

  > **OBS**: ferramentas mais modernas como VS Code e PyCharm, possuem um servidor rodando em background que analisa o código constantemente. Dessa forma, em condições com validações como `isinstance(...)` essas ferramentas já fazem um **_smart casting_** do elemento e atribuí o tipo especificado no segundo argumento função `isinstance(...)`.

Dessa forma, o exemplo demonstra como usar a função `isinstance()` para verificar o tipo de um objeto e executar diferentes ações com base no resultado. Essa função é útil para lidar com diferentes tipos de dados e aplicar lógica condicional de acordo com o tipo encontrado.