# Doctests

Doctests é uma maneira de realizar testes automatizados, porém dentro da DocString de uma função. Para isso é necessário colocar `>>>` e logo em seguida a execução dessa função com os argumentos desejados. Além disso, na linha de baixo coloque o retorno esperado da execução da função.

Aqui está um exemplo de como criar _Doctests_.

```python
def soma(x, y):
  """Soma x e y

  >>> soma(10, 20)
  30
  """

  assert isinstance(x, (int, float)), "x precisa ser int ou float"
  assert isinstance(y, (int, float)), "y precisa ser int ou float"
  return x + y
```

Após declarar os testes, é necessário executá-los dentro da do bloco `if __name__ == "__main__"` da seguinte maneira:

```python
if __name__ == "__main__":
  import doctest
  doctest.testmod()
```

Caso o teste passe com sucesso, nenhuma mensagem será exibida no console, caso contrário será exibido uma mensagem com o valor esperado e obtido ou uma exceção.

Além disso, é possível habilitar o modo `verbose` na função `doctest.testmod()`:

```python
if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)
```

Para criar testes onde um erro é esperado, é necessário indicar a mensagem de erro esperado, no caso basta indicar a primeira linha (que geralmente vai começar com `Traceback (most recent call last):`) e a última linha, que contém a mensagem do erro levantado. Por exemplo:

```python
def soma(x, y):
  """Soma x e y

  >>> soma(10, 20)
  30

  >>> soma("10", 20)
  Traceback (most recent call last):
  ...
  AssertionError: x precisa ser int ou float
  """

  assert isinstance(x, (int, float)), "x precisa ser int ou float"
  assert isinstance(y, (int, float)), "y precisa ser int ou float"
  return x + y
```

> **IMPORTANTE**: não esquecer de adicionar `...` na mensagem de erro esperado

A declaração de testes utilizado _doctest_ é idêntica ao testar um código dentro do _Python Console_.