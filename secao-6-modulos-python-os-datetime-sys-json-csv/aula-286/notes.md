# os + shutil - Copiando arquivos e criando pastas com Python

O módulo `os` e o módulo `shutil` do Python fornecem funções para copiar arquivos e criar pastas.

1. `shutil.copy()`: A função `shutil.copy()` permite copiar um arquivo de origem para um destino especificado. Ela preserva os atributos originais do arquivo, como data de modificação. Aqui está um exemplo:

   ```python
   import shutil

   origem = '/caminho/do/arquivo.txt'
   destino = '/caminho/do/destino/arquivo.txt'

   shutil.copy(origem, destino)
   ```

   Nesse exemplo, o arquivo em "/caminho/do/arquivo.txt" é copiado para "/caminho/do/destino/arquivo.txt" usando `shutil.copy()`.

2. `os.makedirs()`: A função `os.makedirs()` é usada para criar uma ou várias pastas recursivamente. Ela cria todas as pastas necessárias para que o caminho completo especificado seja criado. Aqui está um exemplo:

   ```python
   import os

   caminho_pasta = '/caminho/do/novo/pasta'

   os.makedirs(caminho_pasta)
   ```

   Nesse exemplo, a pasta "/caminho/do/novo/pasta" é criada usando `os.makedirs()`. Se alguma das pastas no caminho especificado já existir, a função simplesmente passa por elas e cria apenas as pastas faltantes.

3. `os.path.expanduser('~')`: É usada para expandir o caractere `~` em um caminho para o diretório raiz do usuário atual. Ela retorna o caminho completo para o diretório inicial do usuário.

   O caractere `~` é uma convenção comum em sistemas Unix-like para representar o diretório raiz do usuário atual. Ao usar `os.path.expanduser('~')`, o caractere `~` é substituído pelo caminho absoluto do diretório inicial do usuário.

   Aqui está um exemplo para ilustrar o uso da função `os.path.expanduser('~')`:

   ```python
   import os

   caminho_diretorio_inicial = os.path.expanduser('~')
   print(caminho_diretorio_inicial)
   ```

   A saída desse exemplo será o caminho absoluto para o diretório inicial do usuário atual, por exemplo:

   ```
   /home/usuario
   ```

   No exemplo acima, o caractere `~` é expandido para o diretório inicial do usuário atual usando `os.path.expanduser('~')`. A função retorna o caminho absoluto correspondente ao diretório inicial do usuário.

Essas são apenas algumas das funções disponíveis nos módulos `os` e `shutil` para copiar arquivos e criar pastas em Python. Essas funções são úteis para automatizar tarefas de gerenciamento de arquivos e diretórios em programas Python.
