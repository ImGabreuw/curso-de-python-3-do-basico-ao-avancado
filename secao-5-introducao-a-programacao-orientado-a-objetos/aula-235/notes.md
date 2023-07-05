# Notas das exceptions em Python 3.11+ (add_notes, `__notes__`)

partir do Python 3.11, foi introduzida uma nova funcionalidade chamada "Notas das exceptions" (_exception notes_). Essa funcionalidade permite que você associe notas informativas a exceções personalizadas, fornecendo detalhes adicionais sobre a exceção e como ela deve ser tratada.

Para adicionar notas a uma exceção personalizada, você precisa definir um método chamado `add_notes` dentro da classe da exceção. Esse método recebe a exceção original como argumento e pode adicionar informações adicionais às notas usando o atributo `__notes__`.

Aqui está um exemplo para ilustrar o uso das notas das exceptions:

```python
class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.__notes__ = []  # Inicializa as notas vazias

    def add_notes(self, exception):
        self.__notes__.append("Detalhes extras: " + str(exception))


def divide(a, b):
    try:
        result = a / b
    except Exception as e:
        raise MyCustomException("Ocorreu um erro durante a divisão.") from e
    return result


try:
    divide(10, 0)
except MyCustomException as e:
    e.add_notes("Divisão por zero não é permitida.")
    print(e)
    print("Notas da exceção:", e.__notes__)
```

Nesse exemplo, temos uma função `divide` que realiza uma divisão. Caso ocorra um erro durante a divisão, uma exceção `MyCustomException` é lançada com uma mensagem genérica. No entanto, usando as notas das exceptions, podemos adicionar informações adicionais à exceção.

No bloco `except`, a exceção original é capturada em `e`. Em seguida, chamamos o método `add_notes` da exceção personalizada, passando a exceção original como argumento. Nesse método, adicionamos uma nota com detalhes extras à lista `__notes__` da exceção.

Ao imprimir a exceção, podemos ver tanto a mensagem original quanto as notas adicionais. No exemplo, também imprimimos as notas explicitamente acessando o atributo `__notes__` da exceção.

As notas das exceptions são uma maneira conveniente de fornecer informações adicionais para facilitar o tratamento de exceções personalizadas. Isso pode ser útil para depuração e para fornecer detalhes úteis sobre a ocorrência da exceção.
