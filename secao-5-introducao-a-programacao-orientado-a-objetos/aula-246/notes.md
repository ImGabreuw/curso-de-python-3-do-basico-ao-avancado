# Classes decoradoras (Decorator classes)

Classes decoradoras em Python são classes que permitem adicionar funcionalidade extra a outras classes ou funções existentes, sem modificar diretamente o código dessas classes ou funções. Elas seguem o padrão de projeto chamado "Decorator", que é uma forma de estender o comportamento de um objeto sem precisar criar subclasses.

A ideia básica é que a classe decoradora envolve ou "decora" outra classe ou função, fornecendo uma interface adicional ou modificando seu comportamento. Essa abordagem é útil quando você deseja adicionar recursos a uma classe ou função existente, sem precisar alterar seu código original.

Vamos ver um exemplo para ilustrar como as classes decoradoras funcionam:

```python
class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Logging message: {self.func.__name__} foi chamado.")
        return self.func(*args, **kwargs)

@Logger
def soma(a, b):
    return a + b

resultado = soma(2, 3)
print(resultado)
```

Nesse exemplo, temos a classe `Logger`, que é uma classe decoradora. Ela recebe uma função como parâmetro em seu construtor e a armazena no atributo `func`. Em seguida, implementamos o método `__call__`, que é invocado quando a função decorada é chamada.

No exemplo, decoramos a função `soma` com a classe `Logger` usando o símbolo `@`. Isso significa que a função `soma` será envolvida pela classe `Logger`, adicionando a funcionalidade de exibir uma mensagem de log sempre que a função for chamada.

Quando chamamos a função `soma`, a classe `Logger` é instanciada e o método `__call__` é executado. A mensagem de log é exibida e, em seguida, a função `soma` original é chamada com os argumentos fornecidos. O resultado é retornado e podemos imprimi-lo.

A saída do exemplo será:

```
Logging message: soma foi chamado.
5
```

Como podemos ver, a classe decoradora `Logger` adiciona uma funcionalidade extra (a exibição de uma mensagem de log) à função `soma`, sem modificar diretamente seu código. Isso permite a extensão de classes e funções de maneira flexível e modular.
