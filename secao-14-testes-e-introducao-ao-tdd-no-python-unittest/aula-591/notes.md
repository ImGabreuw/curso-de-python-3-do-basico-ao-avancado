# Asserções (Assertions)

No Python, você pode definir asserções a partir da palavra reservada `assert` seguido pelos seguintes argumentos:

1. Asserção (condição)

2. Mensagem de erro, caso a condição não for comprida

Aqui está um exemplo de uso do `assert`:

```python
def soma(x, y):
  assert isinstance(x, (int, float)), "x precisa ser int ou float"
  assert isinstance(y, (int, float)), "y precisa ser int ou float"
  return x + y

soma("15", 15)
```

Saída:

```console
Traceback (most recent call last):
  File "/home/gabriel/Projects/curso-de-python-3-do-basico-ao-avancado/secao-14-testes-e-introducao-ao-tdd-no-python-unittest/aula-591/example_1.py", line 5, in <module>
    soma("15", 15)
  File "/home/gabriel/Projects/curso-de-python-3-do-basico-ao-avancado/secao-14-testes-e-introducao-ao-tdd-no-python-unittest/aula-591/example_1.py", line 2, in soma
    assert isinstance(x, (int, float)), "x precisa ser int ou float"
AssertionError: x precisa ser int ou float
```

As asserções são utilizados para avisar outros desenvolvedores sobre um determinado conjunto de regras, geralmente no contexto de testes automatizados. Já no cenário de um cliente utilizar o seu código, é possível desativar as asserções a partir da opção `-O` ao executar o script Python:

```console
$ python -O main.py
```

Saída:

```console
Traceback (most recent call last):
  File "/home/gabriel/Projects/curso-de-python-3-do-basico-ao-avancado/secao-14-testes-e-introducao-ao-tdd-no-python-unittest/aula-591/example_2.py", line 5, in <module>
    soma("15", 15)
  File "/home/gabriel/Projects/curso-de-python-3-do-basico-ao-avancado/secao-14-testes-e-introducao-ao-tdd-no-python-unittest/aula-591/example_2.py", line 3, in soma
    return x + y
TypeError: can only concatenate str (not "int") to str
```

Como é possível ver, o erro levantado agora foi `TypeError` que seria o padrão do Python ao tentar realizar a operação de soma entre uma `str` e `int`.