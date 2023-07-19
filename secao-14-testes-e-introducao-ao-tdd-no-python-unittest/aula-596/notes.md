# Unittest #4 - Executando e organizando todos os testes

Geralmente, os arquivos de testes são agrupados na pasta `tests/` na raiz do projeto, pois assim facilita a localização desses testes.

Para executar todos os testes dentro de um projeto, basta executar o seguinte comando:

```console
$ python -m unittest -v
```

Lembrando que para que isso funcione, todos os arquivos de testes devem ser o seguinte trecho de código:

```python
if __name__ == "__main__":
  unittest.main()
```

Caso você opte por separar os arquivos de teste na pasta `tests/`, as importações podem quebrar já que o caminho relativo mundo, então para resolver isso, é possível manipular o `sys.path` do Python com o seguinte trecho de código:

```python
try:
  import sys
  import path

  sys.path.append(
    os.path.abspath(
      os.path.join(
        os.path.dirname(__file__),
        "../src"
      )
    )
  )
except:
  raise
```

Lembrando que esse trecho de código deve ser colocar no topo do arquivo, antes das importações.