# os.walk para navegar de caminhos de forma recursiva

A função `os.walk()` é uma poderosa função do módulo `os` do Python que permite percorrer recursivamente um diretório e seus subdiretórios. Ela retorna um gerador que produz tuplas contendo o diretório atual, uma lista dos subdiretórios presentes e uma lista dos arquivos presentes em cada iteração.

Aqui está uma descrição detalhada do funcionamento da função `os.walk()`:

A assinatura da função `os.walk()` é a seguinte:

```python
os.walk(top, topdown=True, onerror=None, followlinks=False)
```

- `top`: O diretório raiz a ser percorrido. A função começará a partir deste diretório e percorrerá recursivamente todos os subdiretórios.
- `topdown` (opcional): Um valor booleano que determina a ordem em que os diretórios são listados. Se `True`, a função primeiro lista os diretórios pai antes de entrar nos subdiretórios. Se `False`, a função lista os subdiretórios antes de entrar nos diretórios pai.
- `onerror` (opcional): Uma função de tratamento de erro a ser chamada se ocorrer algum erro ao acessar um diretório. Se não for fornecida, a função lançará uma exceção.
- `followlinks` (opcional): Um valor booleano que indica se a função deve seguir links simbólicos ou não. Se `True`, ela seguirá os links simbólicos e incluirá os arquivos e diretórios vinculados. Se `False`, os links simbólicos não serão seguidos.

A função `os.walk()` retorna um gerador que produz tuplas de três elementos em cada iteração:

```python
(dirpath, dirnames, filenames)
```

- `dirpath`: O caminho completo do diretório atual.
- `dirnames`: Uma lista dos nomes dos subdiretórios presentes no diretório atual.
- `filenames`: Uma lista dos nomes dos arquivos presentes no diretório atual.

Aqui está um exemplo do mundo real que mostra como usar a função `os.walk()` para percorrer um diretório e seus subdiretórios e imprimir todos os caminhos completos dos arquivos encontrados:

```python
import os

diretorio_raiz = '/caminho/do/diretorio'

for dirpath, dirnames, filenames in os.walk(diretorio_raiz):
    for filename in filenames:
        caminho_completo = os.path.join(dirpath, filename)
        print(caminho_completo)
```

Nesse exemplo, a função `os.walk()` é usada para percorrer recursivamente o diretório especificado em `diretorio_raiz`. Em cada iteração, o loop interno percorre todos os arquivos encontrados no diretório atual (`filenames`). O caminho completo de cada arquivo é construído usando `os.path.join()` e, em seguida, é impresso na saída.

Supondo que a estrutura de diretórios em "/caminho/do/diretorio" seja a seguinte:

```
/caminho/do/diretorio/
    ├── arquivo1.txt
    ├── subdiretorio1/
    │   ├── arquivo2.txt
    │   └── arquivo3.txt
    └── subdiretorio2/
        ├── arquivo4.txt
        └── subdiretorio3/
            └── arquivo5.txt
```

A saída do código seria:

```
/caminho/do/diretorio/arquivo1.txt
/caminho/do/diretorio/subdiretorio1/arquivo2.txt
/caminho/do/diretorio/subdiretorio1/arquivo3.txt
/caminho/do/diretorio/subdiretorio2/arquivo4.txt
/caminho/do/diretorio/subdiretorio2/subdiretorio3/arquivo5.txt
```

O código percorre recursivamente o diretório raiz "/caminho/do/diretorio" e seus subdiretórios, e imprime o caminho completo de cada arquivo encontrado. Neste exemplo, ele imprimiria os caminhos completos de todos os arquivos presentes nos diretórios "subdiretorio1", "subdiretorio2" e "subdiretorio3", além do arquivo diretamente no diretório raiz.

Esse exemplo é útil quando você precisa realizar alguma operação em todos os arquivos de um diretório e seus subdiretórios, como processamento em lote, cópia, exclusão etc. A função `os.walk()` simplifica o processo de percorrer de forma recursiva e eficiente toda a estrutura de diretórios.
