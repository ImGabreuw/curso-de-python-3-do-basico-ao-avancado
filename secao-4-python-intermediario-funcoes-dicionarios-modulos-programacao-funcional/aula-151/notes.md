# try, except, else e finally + Built-in Exceptions

Em Python, o bloco `try` pode ser estendido com os blocos `else` e `finally` para adicionar funcionalidades extras ao tratamento de exceções.

O bloco `else` é executado somente se nenhum erro ocorrer no bloco `try`. É útil para definir código que deve ser executado apenas quando nenhuma exceção é lançada. O bloco `else` é opcional e vem imediatamente após os blocos `except`.

O bloco `finally` é sempre executado, independentemente de ocorrer uma exceção ou não. É usado para definir código que deve ser executado, independentemente do resultado do bloco `try` e dos blocos `except`. O bloco `finally` é opcional e vem depois dos blocos `except` ou, se houver, do bloco `else`.

> Geralmente o bloco `finally` é utilizado para fechar conexão com banco de dados ou buffer de arquivos

Aqui está um exemplo que demonstra o uso dos blocos `else` e `finally`:

```python
try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 / num2
except ValueError:
    print("Você deve digitar apenas números inteiros.")
except ZeroDivisionError:
    print("Não é possível realizar divisão por zero.")
else:
    print("O resultado da divisão é:", resultado)
finally:
    print("Fim do programa")
```

Neste exemplo, se não ocorrer nenhum erro durante a execução do bloco `try`, o bloco `else` será executado, exibindo a mensagem `"O resultado da divisão é: <resultado>"`. Caso ocorra uma exceção, o bloco `else` será ignorado.

Independentemente de ocorrer uma exceção ou não, o bloco `finally` será sempre executado, exibindo a mensagem "Fim do programa". É útil para definir código que deve ser executado para finalizar o programa, como a liberação de recursos ou ações de limpeza.

Em relação à hierarquia das exceções em Python, todas as exceções são subclasses da classe base `Exception`. Isso significa que você pode capturar exceções específicas e, ao mesmo tempo, capturar exceções mais genéricas. Aqui está uma hierarquia básica das exceções em Python:

```
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
```

As exceções mais genéricas, como `Exception` e `BaseException`, podem capturar várias exceções específicas. Por exemplo, capturar `Exception` capturará todos os tipos de exceção que são subclasses diretas ou indiretas de `Exception`. No entanto, é recomendável capturar exceções específicas sempre que possível, para tratar adequadamente cada tipo de erro.

Entender a hierarquia de exceções em Python permite capturar e tratar erros de forma mais precisa e eficiente, adaptando o tratamento de acordo com o tipo de exceção esperada.