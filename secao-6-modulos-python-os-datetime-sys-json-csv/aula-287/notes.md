# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python

O módulo `os` e o módulo `shutil` do Python fornecem funções para apagar, copiar, mover e renomear pastas.

1. Apagando pastas com `shutil.rmtree()`: A função `shutil.rmtree()` permite remover uma pasta e todo o seu conteúdo de forma recursiva. Ela exclui tanto os arquivos quanto as subpastas dentro da pasta especificada. Aqui está um exemplo:

   ```python
   import shutil

   pasta_para_apagar = '/caminho/da/pasta'
   shutil.rmtree(pasta_para_apagar)
   ```

   Nesse exemplo, a pasta em "/caminho/da/pasta" e todo o seu conteúdo são apagados usando `shutil.rmtree()`.

2. Copiando pastas com `shutil.copytree()`: A função `shutil.copytree()` também pode ser usada para copiar pastas, conforme mencionado anteriormente. Aqui está um exemplo de cópia de uma pasta:

   ```python
   import shutil

   origem_pasta = '/caminho/da/pasta_origem'
   destino_pasta = '/caminho/do/destino/pasta_destino'

   shutil.copytree(origem_pasta, destino_pasta)
   ```

   Nesse exemplo, a pasta em "/caminho/da/pasta_origem" e todo o seu conteúdo são copiados para "/caminho/do/destino/pasta_destino" usando `shutil.copytree()`.

3. Movendo pastas com `shutil.move()`: A função `shutil.move()` permite mover uma pasta e todo o seu conteúdo para um novo local. Ela pode ser usada para renomear uma pasta também. Aqui está um exemplo:

   ```python
   import shutil

   pasta_origem = '/caminho/da/pasta_origem'
   novo_caminho_pasta = '/novo/caminho/pasta'

   shutil.move(pasta_origem, novo_caminho_pasta)
   ```

   Nesse exemplo, a pasta em "/caminho/da/pasta_origem" e todo o seu conteúdo são movidos para "/novo/caminho/pasta" usando `shutil.move()`.

4. Renomeando pastas com `os.rename()`: A função `os.rename()` permite renomear uma pasta. Ela recebe o caminho atual da pasta e o novo nome da pasta. Aqui está um exemplo:

   ```python
   import os

   caminho_pasta_atual = '/caminho/da/pasta_atual'
   novo_nome_pasta = 'novo_nome'

   os.rename(caminho_pasta_atual, novo_nome_pasta)
   ```

   Nesse exemplo, a pasta em "/caminho/da/pasta_atual" é renomeada para "novo_nome" usando `os.rename()`.

Essas são algumas das funções disponíveis nos módulos `os` e `shutil` para apagar, copiar, mover e renomear pastas em Python. É importante tomar cuidado ao usar essas funções, especialmente ao apagar ou mover pastas, para evitar a perda de dados importantes. Certifique-se de ter permissões adequadas e faça testes antes de realizar operações destrutivas.
