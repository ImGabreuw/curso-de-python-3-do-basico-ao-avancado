# (Parte 2) try e except para tratar exceções

Em Python, é possível capturar e tratar mais de um tipo de exceção em um único bloco `except` usando uma **tupla para agrupar os tipos de exceção**. Além disso, a palavra-chave `as` pode ser usada para atribuir a instância da exceção capturada a uma variável, permitindo um acesso mais detalhado às informações relacionadas à exceção.

Aqui está um exemplo que mostra como capturar múltiplas exceções e usar a palavra-chave `as`:

```python
try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 / num2
    print("O resultado da divisão é:", resultado)
except (ValueError, ZeroDivisionError) as e:
    print(e.__class__.__name__)
    print(e)
```

Neste exemplo, o bloco `try` é o mesmo do exemplo anterior, onde estamos solicitando ao usuário dois números e realizando a divisão. No entanto, agora utilizamos um único bloco `except` com uma tupla `(ValueError, ZeroDivisionError)` para capturar tanto exceções do tipo `ValueError` quanto do tipo `ZeroDivisionError`.

Quando uma exceção é capturada, ela é atribuída à variável `e` através da palavra-chave `as`. Dentro do bloco `except`, é exibido o nome da classe (`ValueError` ou `ZeroDivisionError`) e a mensagem de erro.

O uso da palavra-chave `as` permite que você acesse informações adicionais sobre a exceção capturada, como mensagens de erro específicas, valores associados ou rastreamento de pilha. Você pode usar a variável atribuída (`e`, no exemplo) para realizar ações personalizadas com base nas informações da exceção.

> **OBS**: **a ordem das exceções na tupla importa**. Python irá procurar por uma correspondência do primeiro tipo de exceção na tupla, e se não encontrar, irá verificar a próxima, e assim por diante. Portanto, é importante definir a ordem das exceções de acordo com a sua lógica de tratamento de erros.