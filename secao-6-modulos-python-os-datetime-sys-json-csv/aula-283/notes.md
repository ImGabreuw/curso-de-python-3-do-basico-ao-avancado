# os.listdir para navegar em caminhos

A função `os.listdir()` é usada para obter uma lista de nomes de arquivos e diretórios presentes em um diretório específico. Ela retorna uma lista de strings contendo os nomes dos arquivos e diretórios encontrados no diretório especificado.

Aqui está um exemplo que demonstra o uso da função `os.listdir()`:

```python
import os

diretorio = '/caminho/do/diretorio'

lista_arquivos = os.listdir(diretorio)

for arquivo in lista_arquivos:
    print(arquivo)
```

Neste exemplo, a função `os.listdir()` é usada para obter a lista de arquivos e diretórios presentes no diretório `/caminho/do/diretorio`. A lista resultante é armazenada na variável `lista_arquivos`. Em seguida, um loop é usado para percorrer cada nome de arquivo ou diretório na lista e imprimir na saída.

A saída do exemplo será uma lista dos nomes dos arquivos e diretórios encontrados no diretório especificado.

É importante mencionar que a função `os.listdir()` retorna apenas os nomes dos arquivos e diretórios, sem incluir os caminhos completos. Se você precisar obter os caminhos completos, poderá combiná-los com a função `os.path.join()`. Por exemplo:

```python
import os

diretorio = '/caminho/do/diretorio'

lista_arquivos = os.listdir(diretorio)

for arquivo in lista_arquivos:
    caminho_completo = os.path.join(diretorio, arquivo)
    print(caminho_completo)
```

Nesse caso, a variável `caminho_completo` armazenará o caminho completo de cada arquivo ou diretório encontrado no diretório especificado.
