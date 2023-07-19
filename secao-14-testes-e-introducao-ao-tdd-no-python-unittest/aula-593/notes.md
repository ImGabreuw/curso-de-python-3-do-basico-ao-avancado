# Unittest #1

A criação de testes automatizados com o módulo `unittest` é amplamente utilizados entre os desenvolvedores na comunidade do Python, pois ele disponibiliza várias recursos para essa finalidade em comparação ao _doctests_.

Por convenção, os arquivos e classes destinados para teste começam com _test_, mas respeitando os padrões de nomenclatura de cada um. Além disso, é comum que os testes sejam agrupados em um pasta separada do código fonte.

Para definir uma classe de teste é necessário herdar da classe `TestCase` do módulo `unittest` e em seguida declarar os métodos de testes que devem começar com `test` (caso contrário, esse teste não será executado pelo módulo).

Aqui está um exemplo de como criar teste automatizados com `unittest`:

```python
import unittest
from calculadora import soma

class TestCalculadora(unittest.TestCase):
  def test_soma_5_e_5_deve_retornar_10(self):
    self.assertEqual(
      soma(5, 5), # Resultado obtido
      10 # Resultado esperado
    )

unittest.main()
```

Além disso, é possível testar vários cenários de execução de uma função em um único teste, ao declarar uma tupla contendo as entradas (argumentos da função a ser testada) e o resultado esperados desses cenários:

```python
import unittest
from calculadora import soma

class TestCalculadora(unittest.TestCase):
  def test_soma_5_e_5_deve_retornar_10(self):
    cenarios = (
      (10, 10, 20),
      (5, 5, 10),
      (1.5, 1.5, 3.0),
      (-5, 5, 0),
      (100, 100, 200),
    )

    for x, y, esperado in cenarios:
      with self.subtest(cenario=cenario):
        x, y, esperado = cenario
        self.assertEqual(
          soma(x, y), 
          esperado
        )

unittest.main()
```

O método `subtest()` serve para executar esses vários cenários de entradas na execução de uma função. Como argumento desse método, é possível especificar os valores que serão exibidos caso um teste falhe, como por exemplo os valores de entrada e o resultado esperado.

O método `assertRaises()` serve para testar cenários que é esperado que um erro seja levantado. Para isso, é preciso definir a classe do erro (como 1º argumento) e a mensagem do erro, caso necessário (como 2º argumento). Por exemplo:

```python
import unittest
from calculadora import soma

class TestCalculadora(unittest.TestCase):
  def test_soma_com_x_diferente_de_int_ou_float_deve_lancar_assertionerror(self):
    with self.assertRaises(AssertionError):
      soma("10", 0)

unittest.main()
```