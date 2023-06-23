# raise - lançando exceções (erros)

Em Python, a palavra-chave `raise` é utilizada para explicitamente lançar exceções durante a execução de um programa. Ela permite que você crie suas próprias exceções ou gere exceções pré-definidas para indicar erros ou situações excepcionais.

Existem duas maneiras principais de usar o `raise` em Python. A primeira é criar e lançar uma nova exceção personalizada, criando uma instância de uma classe de exceção. A segunda é re-lançar uma exceção capturada anteriormente, usando a palavra-chave `raise` sem argumentos.

Aqui está um exemplo de criação e lançamento de uma nova exceção personalizada:

```python
class MeuErroPersonalizado(Exception):
    pass

def dividir(x, y):
    if y == 0:
        raise MeuErroPersonalizado("Divisão por zero não é permitida.")
    return x / y

try:
    resultado = dividir(10, 0)
except MeuErroPersonalizado as e:
    print(e)
```

Neste exemplo, criamos uma classe de exceção personalizada chamada `MeuErroPersonalizado`, que herda da classe base `Exception`. A função `dividir()` verifica se o divisor é igual a zero e, nesse caso, lança uma exceção `MeuErroPersonalizado` usando `raise`. 

Dentro do bloco `try-except`, capturamos a exceção `MeuErroPersonalizado` usando um bloco `except` correspondente. A exceção capturada é atribuída à variável `e` usando a palavra-chave `as`, e então imprimimos a mensagem de erro.

Além de criar e lançar exceções personalizadas, também é possível re-lançar exceções capturadas anteriormente usando o `raise` sem argumentos. Isso é útil quando você deseja propagar uma exceção para um nível superior de tratamento de erros.

Aqui está um exemplo de re-lançamento de exceção:

```python
def dividir(x, y):
    try:
        resultado = x / y
    except ZeroDivisionError:
        print("Divisão por zero não é permitida.")
        raise

try:
    dividir(10, 0)
except ZeroDivisionError:
    print("Erro: divisão por zero.")
```

Neste exemplo, a função `dividir()` tenta realizar a divisão de `x` por `y`. Se ocorrer um `ZeroDivisionError`, a exceção é capturada, uma mensagem de erro é exibida e a exceção é re-lançada usando `raise` sem argumentos.

No bloco `try-except` externo, capturamos novamente o `ZeroDivisionError` e exibimos uma mensagem de erro diferente. Isso permite que a exceção seja tratada em diferentes níveis hierárquicos do código, com mensagens de erro e ações diferentes em cada nível.

Em resumo, a palavra-chave `raise` em Python é utilizada para lançar exceções. Você pode criar exceções personalizadas e lançá-las usando `raise`, ou re-lançar exceções capturadas anteriormente para propagar o erro para níveis superiores de tratamento de exceções. Isso permite um controle mais preciso sobre o fluxo de exceções em seu programa.