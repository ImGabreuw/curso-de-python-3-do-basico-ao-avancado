# os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)

### `os.path.getsize()`

Essa função retorna o tamanho de um arquivo em bytes, dado o caminho completo para o arquivo. Ela fornece uma forma simples e direta de obter o tamanho de um arquivo. Aqui está um exemplo:

```python
import os

caminho_arquivo = '/caminho/do/arquivo.txt'
tamanho = os.path.getsize(caminho_arquivo)
print(f'O tamanho do arquivo é {tamanho} bytes')
```

Suponha que o arquivo "/caminho/do/arquivo.txt" tenha um tamanho de 100 bytes. A saída seria:

```
O tamanho do arquivo é 100 bytes
```

### `os.stat()`

Essa função retorna informações detalhadas sobre um arquivo, incluindo seus metadados. Ela retorna um objeto `os.stat_result` que contém vários atributos, incluindo o tamanho do arquivo. Aqui está um exemplo:

```python
import os

caminho_arquivo = '/caminho/do/arquivo.txt'
stats = os.stat(caminho_arquivo)
tamanho = stats.st_size
print(f'O tamanho do arquivo é {tamanho} bytes')
```

A função `os.stat()` retorna um objeto `os.stat_result` com vários atributos relacionados ao arquivo. Usamos `stats.st_size` para obter o tamanho do arquivo. A saída seria a mesma do exemplo anterior:

```
O tamanho do arquivo é 100 bytes
```

Aqui está uma simulação de saída para um exemplo mais completo, percorrendo um diretório e seus arquivos usando `os.path.getsize()`:

```python
import os

diretorio = '/caminho/do/diretorio'

for root, dirs, files in os.walk(diretorio):
    print(f'Pasta atual: {root}')
    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)
        tamanho = os.path.getsize(caminho_completo_arquivo)
        print(f'Arquivo: {file}, Tamanho: {tamanho} bytes')
```

Suponha que a estrutura de diretórios "/caminho/do/diretorio" contenha dois arquivos, "arquivo1.txt" de tamanho 100 bytes e "arquivo2.txt" de tamanho 200 bytes. A saída simulada seria:

```
Pasta atual: /caminho/do/diretorio
Arquivo: arquivo1.txt, Tamanho: 100 bytes
Arquivo: arquivo2.txt, Tamanho: 200 bytes
```

Esses exemplos ilustram como usar `os.path.getsize()` e `os.stat()` para obter o tamanho de um arquivo, seja de forma direta ou com informações adicionais sobre o arquivo usando `os.stat()`.
