# Context Manager com contextlib.contextmanager

Outra abordagem para criar _Context Manager_ no Python é decorar uma função geradora com `@contextmanager` da biblioteca `contextlib`.

Aqui está um exemplo sobre isso:

```python
from contextlib import contextmanager

@contextmanager
def arquivo_texto(caminho_arquivo, modo):
  arquivo = open(caminho_arquivo, modo, encoding="utf8")
  yield arquivo
  arquivo.close()

with arquivo_texto("meuarquivo.txt", "w") as arquivo:
  arquivo.write('Olá, mundo!')
```

Essa implementação funciona perfeitamente bem caso não ocorra uma exceção. Veja o exemplo abaixo:

```python
from contextlib import contextmanager

@contextmanager
def arquivo_texto(caminho_arquivo, modo):
  arquivo = open(caminho_arquivo, modo, encoding="utf8")
  yield arquivo
  arquivo.close()

with arquivo_texto("meuarquivo.txt", "w") as arquivo:
  arquivo.write('Olá, mundo!', 123)
```

Quando o Python executar a linha `arquivo.write('Olá, mundo!', 123)`, será levantada a seguinte exceção:

```
Traceback (most recent call last):
  File "/home/gabriel/Projects/curso-de-python-3-do-basico-ao-avancado/secao-5-introducao-a-programacao-orientado-a-objetos/aula-242/example_1.py", line 10, in <module>
    arquivo.write('Olá, mundo!', 123)
TypeError: TextIOWrapper.write() takes exactly one argument (2 given)
```

E esse comportamento não é o esperado para um _Context Manager_, uma vez que a exceção, caso ocorra, deve ser silenciada. Então para resolver isso utilizaremos o bloco `try-finally` em volta da implementação da função geradora `arquivo_texto`.

```python
from contextlib import contextmanager

@contextmanager
def arquivo_texto(caminho_arquivo, modo):
  try:
    arquivo = open(caminho_arquivo, modo, encoding="utf8")
    yield arquivo
  finally:
    arquivo.close()

with arquivo_texto("meuarquivo.txt", "w") as arquivo:
  arquivo.write('Olá, mundo!', 123)
```

Não é recomendado utilizar o bloco `except`, pois isso deve ser responsabilidade do desenvolvedor que estão usando o nosso _Context Manager_.
