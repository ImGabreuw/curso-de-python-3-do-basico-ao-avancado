# Unittest #3 - Com TDD

O Mock é uma parte essencial da biblioteca `unittest` e é usado para simular objetos ou partes do código durante o teste. Ele permite criar objetos falsos que se comportam como objetos reais, mas você pode controlar seu comportamento para melhorar a precisão dos testes

O `patch()` é uma função fornecida pelo módulo `unittest.mock` que permite substituir um objeto real por um objeto _mock_ em determinados contextos durante os testes. Isso é especialmente útil quando você deseja testar um código que depende de recursos externos, como APIs ou bancos de dados, sem realmente acessar esses recursos reais durante os testes.

Aqui está um exemplo de como usar a função `patch`:

```python
# pessoa.py
import requests


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        resposta = requests.get('localhost:8080')

        if resposta.ok:
            self.dados_obtidos = True
            return 'CONECTADO'

        self.dados_obtidos = False
        return 'ERRO 404'
```

```python
import unittest
from unittest.mock import patch
from pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Luiz', 'Otávio')

    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)

if __name__ == '__main__':
    unittest.main(verbosity=2)
```

No argumento da função `patch()`, é necessário especificar qual o recurso externo que deve ser feito o _mock_ (simulação), no caso acima foi a função `request.get()`.