# Manipulando caminhos, pastas e arquivos no Python com pathlib (aula externa)

O módulo `pathlib` do Python fornece uma interface orientada a objetos para manipular caminhos de arquivo e diretório de forma mais intuitiva e eficiente. Ele simplifica a interação com o sistema de arquivos, oferecendo métodos e atributos convenientes. Aqui estão alguns dos principais métodos e conceitos do módulo `pathlib`:

1. `Path`: O `Path` é a classe principal do módulo `pathlib`. Ele representa um caminho de arquivo ou diretório. Você pode criar um objeto `Path` passando uma string que representa o caminho:

   ```python
   from pathlib import Path

   # Criando um objeto Path para um arquivo
   caminho_arquivo = Path('/caminho/do/arquivo.txt')

   # Criando um objeto Path para um diretório
   caminho_diretorio = Path('/caminho/do/diretorio')
   ```

2. Atributos de `Path`:

   - `.name`: Retorna o nome do arquivo ou diretório.
   - `.parent`: Retorna o diretório pai do arquivo ou diretório.
   - `.suffix`: Retorna a extensão do arquivo.
   - `.stem`: Retorna o nome do arquivo sem a extensão.

   ```python
   caminho_arquivo = Path('/caminho/do/arquivo.txt')

   print(caminho_arquivo.name)    # arquivo.txt
   print(caminho_arquivo.parent)  # /caminho/do
   print(caminho_arquivo.suffix)  # .txt
   print(caminho_arquivo.stem)    # arquivo
   ```

3. Métodos de `Path`:

   - `.exists()`: Verifica se o arquivo ou diretório existe.
   - `.is_file()`: Verifica se o caminho é um arquivo.
   - `.is_dir()`: Verifica se o caminho é um diretório.
   - `.mkdir()`: Cria um diretório.
   - `.unlink()`: Exclui um arquivo.
   - `.rename(novo_nome)`: Renomeia o arquivo ou diretório.

   ```python
   caminho_arquivo = Path('/caminho/do/arquivo.txt')

   if caminho_arquivo.exists():
       print("O arquivo existe!")

   if caminho_arquivo.is_file():
       print("É um arquivo!")

   caminho_diretorio = Path('/caminho/do/novo_diretorio')

   if not caminho_diretorio.exists():
       caminho_diretorio.mkdir()
       print("Diretório criado!")

   caminho_arquivo.unlink()
   print("Arquivo excluído!")
   ```

4. Iteração com `Path`:

   - `iterdir()`: Retorna um iterador com os caminhos dos arquivos e diretórios no diretório atual.
   - `glob()`: Retorna um gerador com os caminhos que correspondem a um padrão específico.

   ```python
   caminho_diretorio = Path('/caminho/do/diretorio')

   for caminho in caminho_diretorio.iterdir():
       print(caminho)

   # Usando glob para listar apenas os arquivos .txt
   for caminho in caminho_diretorio.glob('*.txt'):
       print(caminho)
   ```

5. O método `__truediv__`:

   O método `__truediv__` no módulo `pathlib` do Python é um método especial que permite a divisão de caminhos de diretórios, criando um novo objeto `Path` resultante da concatenação dos caminhos. Quando usamos o operador de divisão (`/`) entre dois objetos `Path`, o método `__truediv__` é acionado automaticamente e retorna um novo objeto `Path` que representa o caminho resultante da concatenação dos caminhos.

   Aqui está um exemplo para ilustrar o uso do método `__truediv__`:

   ```python
   from pathlib import Path

   caminho_diretorio = Path('/caminho/do/diretorio')
   caminho_arquivo = Path('arquivo.txt')

   caminho_completo = caminho_diretorio / caminho_arquivo
   print(caminho_completo)
   ```

   Neste exemplo, temos um objeto `Path` chamado `caminho_diretorio` que representa um diretório `'/caminho/do/diretorio'` e um objeto `Path` chamado `caminho_arquivo` que representa o arquivo `'arquivo.txt'`.

   Ao usar o operador de divisão (`/`) entre os objetos `caminho_diretorio` e `caminho_arquivo`, o método `__truediv__` é acionado e retorna um novo objeto `Path`, `caminho_completo`, que representa o caminho completo do arquivo dentro do diretório.

   A saída será:

   ```
   /caminho/do/diretorio/arquivo.txt
   ```

   Dessa forma, o uso do método `__truediv__` no módulo `pathlib` torna a manipulação de caminhos de diretórios mais conveniente, permitindo a concatenação de caminhos de forma simples e legível.

6. Método `home()`:

   O método `home()` retorna o caminho do diretório home do usuário atual. Esse método é útil quando você precisa acessar arquivos ou diretórios dentro do diretório home do usuário sem se preocupar com o sistema operacional específico. Aqui está um exemplo:

   ```python
   from pathlib import Path

   caminho_home = Path.home()
   print(caminho_home)
   ```

   A saída será o caminho do diretório home do usuário atual, como por exemplo: `/home/seu_usuario` (em sistemas Unix-like) ou `C:\Users\seu_usuario` (em sistemas Windows).

7. Método `touch()`:

   O método `touch()` cria um arquivo vazio no caminho especificado. Se o arquivo já existir, ele atualiza o carimbo de data/hora de acesso e modificação do arquivo. Aqui está um exemplo:

   ```python
   from pathlib import Path

   caminho_arquivo = Path('/caminho/do/arquivo.txt')
   caminho_arquivo.touch()
   ```

   Nesse exemplo, o método `touch()` é usado para criar o arquivo `arquivo.txt` no caminho especificado. Se o arquivo já existir, ele será atualizado com um novo carimbo de data/hora.

   Você também pode usar o método `touch()` com o argumento `exist_ok=True` para evitar uma exceção caso o arquivo já exista:

   ```python
   from pathlib import Path

   caminho_arquivo = Path('/caminho/do/arquivo.txt')
   caminho_arquivo.touch(exist_ok=True)
   ```

   Esses são exemplos do uso do método `home()` e `touch()` no módulo `pathlib` do Python. O método `home()` é útil para acessar o diretório home do usuário atual, enquanto o método `touch()` é útil para criar ou atualizar um arquivo. Ambos os métodos são úteis para interagir com o sistema de arquivos de forma conveniente e portável.

8. Método `read_text()`:
   O método `read_text()` é usado para ler o conteúdo de um arquivo de texto e retorná-lo como uma string. Ele simplifica a leitura de arquivos de texto, eliminando a necessidade de abrir, ler e fechar manualmente o arquivo. Aqui está um exemplo:

   ```python
   from pathlib import Path

   caminho_arquivo = Path('/caminho/do/arquivo.txt')

   conteudo = caminho_arquivo.read_text()
   print(conteudo)
   ```

   Nesse exemplo, o método `read_text()` é chamado no objeto `Path` que representa o arquivo `/caminho/do/arquivo.txt`. O conteúdo do arquivo é lido e atribuído à variável `conteudo`, que é então impressa na saída.

9. Método `write_text()`:
   O método `write_text()` é usado para gravar o conteúdo de uma string em um arquivo de texto. Ele cria ou substitui o arquivo de texto com o conteúdo fornecido. Aqui está um exemplo:

   ```python
   from pathlib import Path

   caminho_arquivo = Path('/caminho/do/arquivo.txt')

   conteudo = 'Este é o conteúdo do arquivo.'

   caminho_arquivo.write_text(conteudo)
   ```

   Nesse exemplo, o método `write_text()` é chamado no objeto `Path` que representa o arquivo `/caminho/do/arquivo.txt`. O conteúdo da string `conteudo` é gravado no arquivo, substituindo o conteúdo anterior, se houver.

   É importante mencionar que tanto o `read_text()` quanto o `write_text()` assumem que o arquivo está codificado em UTF-8, a menos que você especifique um encoding diferente como um argumento opcional.

10. Context Manager `open`:
    No módulo `pathlib` do Python, o contexto manager `open()` é uma forma conveniente de abrir um arquivo de texto usando um objeto `Path` como contexto. Ele permite a leitura ou escrita do arquivo, garantindo que o arquivo seja corretamente fechado após o uso, mesmo em casos de exceção.

    Aqui está como usar o contexto manager `open()` com `Path`:

    ```python
    from pathlib import Path

    caminho_arquivo = Path('/caminho/do/arquivo.txt')

    # Leitura do arquivo usando o contexto manager
    with caminho_arquivo.open() as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

    # Escrita no arquivo usando o contexto manager
    with caminho_arquivo.open(mode='w') as arquivo:
        arquivo.write('Este é o conteúdo do arquivo.')
    ```

    No exemplo acima, o objeto `Path` `caminho_arquivo` representa o caminho do arquivo `/caminho/do/arquivo.txt`.

    Ao usar o contexto manager `with`, o arquivo é aberto dentro do bloco `with` e atribuído ao identificador `arquivo`. Você pode ler o conteúdo do arquivo usando o método `read()` ou escrever no arquivo usando o método `write()`.

    Uma vez que o bloco `with` é concluído, o arquivo é automaticamente fechado, independentemente do fluxo normal ou de exceções ocorridas dentro do bloco. Isso garante que os recursos sejam liberados corretamente e que o arquivo seja fechado adequadamente após o uso.

    O uso do contexto manager `open()` com `Path` oferece uma sintaxe mais concisa e legível para manipulação de arquivos, tornando o código mais organizado e seguro. É uma alternativa conveniente ao uso direto da função `open()` em conjunto com `try/finally` para garantir o fechamento adequado do arquivo.
