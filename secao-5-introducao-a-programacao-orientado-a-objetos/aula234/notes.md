# Levantando e tratando suas Exceptions (Exceções)

Diferentemente de outras linguagem como JavaScript e Java, por exemplo, é denotado a ação de **lançar** uma exceção, já no Python utiliza **levantar**, mas ambas possuem a mesma finalidade que é notificar o usuário ou cliente sobre exceção que ocorreu.

No Python, para levantar uma exceção usa-se a palavra reservada `raise`, como é possível ver no código abaixo:

```python
class MeuError(Exception):
  ...

def levantar_excecao():
  raise MeuError("A mensagem de erro", "outra coisa")
```

Os valores passados como argumento no método construtor de `MeuError` é armazenada dentro de uma tupla chamada de `args`.

```python
class MeuError(Exception):
  ...

def levantar_excecao():
  raise MeuError("A mensagem de erro", "outra coisa")

try:
  levantar_excecao()
except MeuError as error:
  print(error.args)

# Saída: ("A mensagem de erro", "outra coisa")
```

Além disso é possível relançar uma exceção capturada pelo bloco `except` por meio de `raise` sem argumentos, por exemplo:

```python
class MeuError(Exception):
  ...

def levantar_excecao():
  raise MeuError("A mensagem de erro", "outra coisa")

try:
  levantar_excecao()
except MeuError as error:
  print(error.args)
  raise
```

Outra forma de relançar uma exceção é lançar uma exceção customizada, por exemplo, e indicar qual exceção causou isso utilizado a palavra reservada `from`. Veja o exemplo abaixo:

```python
class MeuError(Exception):
  ...

class OutroError(Exception):
  ...

def levantar_excecao():
  raise MeuError("A mensagem de erro", "outra coisa")

try:
  levantar_excecao()
except MeuError as error:
  print(error.args)
  exception_ = OutroError("Relançando exceção")
  raise exception_ from error
```

O código acima resultou na seguinte saída:

```
('A mensagem de erro', 'outra coisa')
Traceback (most recent call last):
  File "/home/gabriel/Projects/curso-de-python-3-do-basico-ao-avancado/secao-5-introducao-a-programacao-orientado-a-objetos/aula234/main.py", line 11, in <module>
    levantar_excecao()
  File "/home/gabriel/Projects/curso-de-python-3-do-basico-ao-avancado/secao-5-introducao-a-programacao-orientado-a-objetos/aula234/main.py", line 8, in levantar_excecao
    raise MeuError("A mensagem de erro", "outra coisa")
__main__.MeuError: ('A mensagem de erro', 'outra coisa')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/gabriel/Projects/curso-de-python-3-do-basico-ao-avancado/secao-5-introducao-a-programacao-orientado-a-objetos/aula234/main.py", line 15, in <module>
    raise exception_ from error
__main__.OutroError: Relançando exceção
```