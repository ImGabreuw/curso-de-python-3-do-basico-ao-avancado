# (Parte 1) try e except para tratar exceções

O bloco `try-except` em Python é utilizado para tratar exceções que podem ocorrer durante a execução de um trecho de código. Ele permite que você capture e lide com erros de forma controlada, evitando que o programa seja interrompido abruptamente. O bloco `try` define o código que será executado, e o bloco `except` especifica como tratar as exceções que possam ocorrer.

Aqui está um exemplo básico de uso do `try-except` em Python:

```python
try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 / num2
    print("O resultado da divisão é:", resultado)
except ValueError:
    print("Você deve digitar apenas números inteiros.")
except ZeroDivisionError:
    print("Não é possível realizar divisão por zero.")
```

Neste exemplo, o bloco `try` contém o código que pode gerar exceções, no caso, a conversão das entradas de usuário em números inteiros (`int(input())`) e a divisão dos números. Se ocorrer algum erro durante a execução desse código, a execução é interrompida e passa para o bloco `except`.

No bloco `except`, são especificados os tipos de exceções que serão tratadas. No exemplo, temos dois blocos `except`: um para `ValueError`, que ocorre se a conversão para inteiro falhar devido a um valor inválido digitado pelo usuário, e outro para `ZeroDivisionError`, que ocorre quando o segundo número é igual a zero.

Se ocorrer uma exceção correspondente a algum dos tipos especificados no `except`, o código dentro desse bloco será executado. No exemplo, uma mensagem de erro adequada é exibida para cada tipo de exceção.

Caso nenhuma exceção ocorra no bloco `try`, o bloco `except` é ignorado e a execução continua normalmente após o bloco `except`.

O bloco `except` também pode ser usado sem especificar um tipo de exceção específico, capturando todas as exceções ou você pode usar `except Exception`, uma vez que a classe `Exception` é a classe "pai" de todas as exceções no Python. No entanto, é recomendável ser mais específico em relação aos tipos de exceções que você espera tratar, para evitar capturar e silenciar erros indesejados.

Veja o exemplo abaixo:

```python
try:
  num1 = 10
  # num2 = 0
  resultado = num1 / num2
  print("O resultado da divisão é:", resultado)
except:
  print("Não é possível realizar divisão por zero.")
```

Como você pode ver no código acima, o tratamento da excepção no bloco `except` não é adequado para o erro lançado, pois não se trata mais de `ZeroDivisionError`, mas sim de `NameError` uma vez que a variável `num2` não foi declarada.