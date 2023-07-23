# Structural Pattern Matching no Python (Match/Case, mais que Swtich/Case)

> ## **Introdução**

O Python 3.10 introduziu a sintaxe `match-case` (também conhecida como `match`), que é uma nova forma de fazer comparações mais concisas e expressivas em comparação ao tradicional `if-else`.

Antes do Python 3.10, para fazer comparações de padrões múltiplos, costumávamos usar várias declarações `if-else` para verificar diferentes casos. No entanto, com `match-case`, podemos agrupar várias condições em uma única declaração, tornando o código mais legível e conciso.

Aqui está um exemplo que mostra como usar `match-case` em comparação com `if-else`:

Exemplo usando if-else:

```python
def execute_command(command):
    if command == 'ls':
        print('$ listing files')
    elif command == 'cd':
        print('$ changing directory')
    else:
        print('$ command not implemented')

    print('...rest of the code')
```

Exemplo usando match-case:

```python
def execute_command(command):
    match command:
        case 'ls':
            print('$ listing files')
        case 'cd':
            print('$ changing directory')
        case _:
            print('$ command not implemented')

    print('...rest of the code')
```

Neste exemplo, usamos `match` para substituir o `if`. Cada caso é declarado usando `case` seguido pelo valor esperado. O caso especial `_` é usado como um curinga (wildcard), equivalente ao `else`, para capturar todos os outros valores que não correspondem aos casos anteriores.

O uso de `match-case` torna o código mais limpo e fácil de ler, especialmente quando há muitos casos diferentes para comparar. É uma adição bem-vinda ao Python para tornar as estruturas de controle mais expressivas e poderosas. No entanto, é importante notar que o `match-case` está disponível apenas a partir do Python 3.10.

> ## **Execução de métodos/funções no `match`**

No Python 3.10, a funcionalidade `match-case` foi estendida para permitir a execução de métodos e funções diretamente dentro dos casos correspondentes.

No exemplo que você forneceu, temos uma função chamada `execute_command` que recebe um comando como argumento e, em seguida, executa diferentes ações com base no comando usando `match-case`.

```python
def execute_command(command):
    match command.split():
        case ['ls', path, *_]:
            print('$ listing files from', path)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não é obrigatório
            print('$ command not implemented')

    print('...rest of the code')
```

Vamos entender o que está acontecendo no código:

1. A função `execute_command` recebe um comando como entrada. Esse comando é uma string que pode representar diferentes ações, como "ls" (listar arquivos), "cd" (mudar de diretório) ou outros comandos (não implementados).

2. O `match-case` é usado para fazer comparações com base nos comandos fornecidos. A expressão `command.split()` divide a string do comando em uma lista de palavras, onde cada palavra é um elemento da lista.

3. Em seguida, temos vários casos (`case`) que correspondem aos diferentes comandos. Se o comando corresponder a um dos casos, a ação associada será executada. Note que agora podemos executar diretamente ações dentro dos casos.

4. O caso padrão `_` é opcional e será executado caso o comando não corresponda a nenhum dos casos anteriores.

Exemplo de uso da função `execute_command`:

```python
execute_command("ls /home/user/documents")
# Saída: $ listing files from /home/user/documents
# ...rest of the code

execute_command("cd /home/user/music")
# Saída: $ changing directory to /home/user/music
# ...rest of the code

execute_command("echo Hello")
# Saída: $ command not implemented
# ...rest of the code
```

No exemplo acima, a função `execute_command` é chamada três vezes com comandos diferentes. A cada chamada, o `match-case` verifica o comando e executa a ação correspondente ou o caso padrão.

É importante observar que a funcionalidade `match-case` está disponível apenas a partir do Python 3.10. Se você estiver usando uma versão anterior do Python, não terá acesso a esse recurso e precisará usar uma estrutura de controle diferente, como `if-elif-else`.

> ## **Listas nos casos do `match`**

No Python 3.10, o `match-case` permite que você use listas com padrões específicos para simplificar a comparação de diferentes casos em uma única declaração. Isso é feito usando o operador `|` (_pipe_) para definir padrões alternativos dentro da lista.

Vamos entender como o código funciona e, em seguida, fornecer um exemplo:

```python
def execute_command(command):
    match command.split():
        case ['ls' | 'list', path, *_]:
            print('$ listing files from', path)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')
```

Neste exemplo, temos uma função chamada `execute_command` que recebe um comando como argumento e, em seguida, usa o `match-case` para comparar diferentes casos com base no comando.

1. O `command.split()` divide a string do comando em uma lista de palavras, onde cada palavra é um elemento da lista.

2. No primeiro caso (`case ['ls' | 'list', path, *_]:`), usamos o operador `|` para definir que o padrão pode ser "ls" ou "list". Se o comando for "ls" ou "list", esse caso será correspondido. Além disso, usamos `path` e `*_` para capturar valores adicionais que podem seguir o comando (os argumentos adicionais).

3. No segundo caso (`case ['cd', path]:`), comparamos se o comando é "cd" seguido de `path`.

4. O caso padrão `_` é opcional e será executado caso o comando não corresponda a nenhum dos casos anteriores.

Exemplo de uso da função `execute_command`:

```python
execute_command("ls /home/user/documents")
# Saída: $ listing files from /home/user/documents
# ...rest of the code

execute_command("list /home/user/music")
# Saída: $ listing files from /home/user/music
# ...rest of the code

execute_command("cd /home/user/music")
# Saída: $ changing directory to /home/user/music
# ...rest of the code

execute_command("echo Hello")
# Saída: $ command not implemented
# ...rest of the code
```

No exemplo acima, a função `execute_command` é chamada quatro vezes com comandos diferentes. A cada chamada, o `match-case` verifica o comando e executa a ação correspondente ou o caso padrão.

O uso de listas com padrões alternativos é uma forma poderosa e legível de realizar comparações em uma única declaração. O Python 3.10 tornou a sintaxe mais expressiva e flexível, permitindo escrever código mais limpo e conciso em comparação com as versões anteriores do Python.

> ## **_Case guard_ no `match`**

O `case guard` é uma funcionalidade poderosa introduzida no Python 3.10 que permite aplicar condições adicionais para verificar se um determinado caso deve ou não ser correspondido no `match-case`. É uma forma de adicionar filtros ou condições extras para melhor controlar a lógica de correspondência dos casos.

Vamos entender como o código funciona e fornecer um exemplo:

```python
def execute_command(command):
    match command.split():
        case ['ls' | 'list', *directories] if len(directories) > 1:
            for directory in directories:
                print('$ listing ALL directories from', directory)
        case ['ls' | 'list', *directories] if len(directories) == 1:
            print('$ listing ONE directory from', directories[0])
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')
```

Neste exemplo, a função `execute_command` recebe um comando como argumento e usa o `match-case` para comparar diferentes casos com base no comando.

1. O `command.split()` divide a string do comando em uma lista de palavras, onde cada palavra é um elemento da lista.

2. No primeiro caso (`case ['ls' | 'list', *directories] if len(directories) > 1:`), usamos o `case guard` com `if len(directories) > 1` para verificar se a lista `directories` tem mais de um elemento. Se a condição for verdadeira, o caso será correspondido e o código dentro desse caso será executado. Neste caso, usamos um loop para listar todos os diretórios presentes.

3. No segundo caso (`case ['ls' | 'list', *directories] if len(directories) == 1:`), usamos o `case guard` com `if len(directories) == 1` para verificar se a lista `directories` tem um ou nenhum elemento. Se a condição for verdadeira, o caso será correspondido e o código dentro desse caso será executado. Neste caso, listamos apenas um diretório.

4. O terceiro caso (`case ['cd', path]:`) corresponde ao comando "cd" seguido de um diretório. Não há necessidade de um `case guard` neste caso, pois não há condições adicionais a serem verificadas.

5. O caso padrão `_` é opcional e será executado caso o comando não corresponda a nenhum dos casos anteriores.

Exemplo de uso da função `execute_command`:

```python
execute_command("ls /home/user/documents /home/user/downloads")
# Saída:
# $ listing ALL directories from /home/user/documents
# $ listing ALL directories from /home/user/downloads
# ...rest of the code

execute_command("ls /home/user/music")
# Saída:
# $ listing ONE directory from /home/user/music
# ...rest of the code

execute_command("cd /home/user/music")
# Saída: $ changing directory to /home/user/music
# ...rest of the code

execute_command("echo Hello")
# Saída: $ command not implemented
# ...rest of the code
```

No exemplo acima, a função `execute_command` é chamada quatro vezes com comandos diferentes. A cada chamada, o `structural pattern match` verifica o comando e executa a ação correspondente ou o caso padrão, levando em conta as condições adicionais fornecidas pelos `case guards`.

O uso do `case guard` torna o `match-case` ainda mais flexível e poderoso, permitindo que você implemente lógica mais complexa de correspondência de casos. É uma adição valiosa ao Python 3.10 para lidar com cenários mais sofisticados de correspondência de padrões.

> **`as` statement no `match`**

O `as` statement no `match-case` é uma funcionalidade que foi introduzida no Python 3.10, para permitir que você atribua nomes a padrões específicos durante a correspondência nos casos. Ele é útil quando você deseja capturar valores específicos dentro dos padrões correspondentes e usá-los posteriormente no código.

Vamos entender como o código funciona e fornecer um exemplo:

```python
def execute_command(command):
    match command.split():
        case ['ls' | 'list' as the_command, *directories] as the_list if len(directories) > 1:
            for directory in directories:
                print('$ listing ALL directories from', directory)
            print(f'{the_command=}, {the_list=}')
        case ['ls' | 'list', *directories] if len(directories) == 1:
            print('$ listing ONE directory from', directories[0])
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')
```

Neste exemplo, a função `execute_command` recebe um comando como argumento e usa o `match-case` para comparar diferentes casos com base no comando.

1. O `command.split()` divide a string do comando em uma lista de palavras, onde cada palavra é um elemento da lista.

2. No primeiro caso (`case ['ls' | 'list' as the_command, *directories] as the_list if len(directories) > 1:`), usamos o "as" statement para atribuir o valor correspondente ao padrão `[ls | list]` a uma variável chamada `the_command`. Além disso, também atribuímos o valor completo do padrão (ou seja, a lista de palavras após `['ls' | 'list']`) a uma variável chamada `the_list`. Essas variáveis podem ser usadas posteriormente no código. O "as" statement é usado tanto para `the_command` quanto para `the_list`.

3. No segundo caso (`case ['ls' | 'list', *directories] if len(directories) == 1:`), não usamos o `as`, pois não precisamos atribuir valores específicos a variáveis nesse caso.

4. O terceiro caso (`case ['cd', path]:`) corresponde ao comando "cd" seguido de um diretório. Não há necessidade de usar o `as` neste caso, pois não há variáveis adicionais a serem capturadas.

5. O caso padrão `_` é opcional e será executado caso o comando não corresponda a nenhum dos casos anteriores.

Exemplo de uso da função `execute_command`:

```python
execute_command("ls /home/user/documents /home/user/downloads")
# Saída:
# $ listing ALL directories from /home/user/documents
# $ listing ALL directories from /home/user/downloads
# the_command='ls', the_list=['ls', '/home/user/documents', '/home/user/downloads']
# ...rest of the code

execute_command("ls /home/user/music")
# Saída:
# $ listing ONE directory from /home/user/music
# ...rest of the code

execute_command("cd /home/user/music")
# Saída: $ changing directory to /home/user/music
# ...rest of the code

execute_command("echo Hello")
# Saída: $ command not implemented
# ...rest of the code
```

No exemplo acima, a função `execute_command` é chamada quatro vezes com comandos diferentes. A cada chamada, o `match-case` verifica o comando e executa a ação correspondente ou o caso padrão. As variáveis `the_command` e `the_list` são usadas apenas no primeiro caso, onde são capturadas pelo `as` e depois impressas na saída.

O uso do `as` torna o `match-case` ainda mais poderoso, permitindo que você capture e utilize valores específicos dentro dos casos correspondentes para realizar tarefas mais complexas. É uma adição valiosa ao Python 3.10 para melhorar a flexibilidade e expressividade do `match-case`.

> ## **Dicionários no `match`**

No Python 3.10, o `match-case` também suporta a correspondência de padrões usando dicionários. Você pode utilizar um dicionário como padrão e verificar se o dicionário possui determinadas chaves e valores específicos.

Vamos entender como o código funciona e fornecer um exemplo:

```python
def execute_command(command):
    match command:
        case {'command': 'ls', 'directories': [_, *_]}:
            for directory in command['directories']:
                print('$ listing ALL directories from', directory)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')
```

Neste exemplo, a função `execute_command` recebe um comando como argumento e usa o `match-case` para comparar diferentes casos com base no comando.

1. O primeiro caso (`case {'command': 'ls', 'directories': [_, *_]}`) usa um dicionário como padrão, verificando se o dicionário possui as chaves `'command'` e `'directories'` com valores específicos. O valor associado à chave `'command'` deve ser exatamente `'ls'`, e o valor associado à chave `'directories'` deve ser uma lista com pelo menos um elemento (capturado como `_`) seguido de zero ou mais elementos (capturados como `*_`).

2. No caso anterior, usamos o operador `*_` para capturar qualquer número de elementos adicionais na lista de diretórios. Isso permite que você liste todos os diretórios presentes no dicionário, independentemente do número de elementos.

3. O caso padrão `_` é opcional e será executado caso o comando não corresponda a nenhum dos casos anteriores.

Exemplo de uso da função `execute_command`:

```python
execute_command({'command': 'ls', 'directories': ['/home/user/documents', '/home/user/downloads']})
# Saída:
# $ listing ALL directories from /home/user/documents
# $ listing ALL directories from /home/user/downloads
# ...rest of the code

execute_command({'command': 'ls', 'directories': ['/home/user/music']})
# Saída:
# $ listing ALL directories from /home/user/music
# ...rest of the code

execute_command({'command': 'cd', 'path': '/home/user/music'})
# Saída: $ command not implemented
# ...rest of the code

execute_command({'command': 'echo', 'message': 'Hello'})
# Saída: $ command not implemented
# ...rest of the code
```

No exemplo acima, a função `execute_command` é chamada quatro vezes com diferentes dicionários como comandos. A cada chamada, o `match-case` verifica o dicionário e executa a ação correspondente ou o caso padrão. O uso de dicionários como padrões torna a correspondência mais flexível e permite que você verifique diferentes chaves e valores nos dicionários para executar tarefas específicas.

O `match-case` é uma funcionalidade poderosa introduzida no Python 3.10, tornando o código mais expressivo e facilitando o tratamento de vários casos diferentes de forma concisa.

> ## **Classes no `match`**

No Python 3.10, o `match-case` também suporta a correspondência de padrões usando classes como parte da sintaxe do match. Você pode criar classes específicas para representar os dados que serão usados como padrões nos casos.

Vamos entender como o código funciona e fornecer um exemplo:

```python
from dataclasses import dataclass

@dataclass
class Command:
    command: str
    directories: list[str]


def execute_command(command: Command):
    match command:
        case Command(command='ls', directories=[_, *_]):
            for directory in command.directories:
                print('$ listing ALL directories from', directory)
        case Command(command='cd', directories=[_, *_]):
            for directory in command.directories:
                print('$ changing to', directory)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')
```

Neste exemplo, criamos uma classe chamada `Command` usando o decorador `@dataclass` para facilitar a definição da classe e inicializar os atributos. Essa classe possui dois atributos: `command`, que representa o comando em si, e `directories`, que representa uma lista de diretórios associados ao comando.

A função `execute_command` agora recebe um objeto da classe `Command` como argumento e usa o `match-case` para comparar diferentes casos com base no comando e diretórios.

1. No primeiro caso (`case Command(command='ls', directories=[_, *_]):`), verificamos se o objeto `command` possui os atributos `command` e `directories` com os valores específicos. O valor associado ao atributo `command` deve ser exatamente `'ls'`, e o valor associado ao atributo `directories` deve ser uma lista com pelo menos um elemento (capturado como `_`) seguido de zero ou mais elementos (capturados como `*_`).

2. No segundo caso (`case Command(command='cd', directories=[_, *_]):`), verificamos se o objeto `command` possui os atributos `command` e `directories` com os valores específicos. O valor associado ao atributo `command` deve ser exatamente `'cd'`, e o valor associado ao atributo `directories` deve ser uma lista com pelo menos um elemento (capturado como `_`) seguido de zero ou mais elementos (capturados como `*_`).

3. O caso padrão `_` é opcional e será executado caso o comando não corresponda a nenhum dos casos anteriores.

Exemplo de uso da função `execute_command`:

```python
command1 = Command(command='ls', directories=['/home/user/documents', '/home/user/downloads'])
execute_command(command1)
# Saída:
# $ listing ALL directories from /home/user/documents
# $ listing ALL directories from /home/user/downloads
# ...rest of the code

command2 = Command(command='cd', directories=['/home/user/music'])
execute_command(command2)
# Saída:
# $ changing to /home/user/music
# ...rest of the code

command3 = Command(command='echo', directories=[])
execute_command(command3)
# Saída: $ command not implemented
# ...rest of the code
```

No exemplo acima, criamos três objetos da classe `Command` com diferentes comandos e diretórios. A função `execute_command` é chamada três vezes com esses objetos como argumentos. A cada chamada, o `match-case` verifica o objeto `command` e executa a ação correspondente ou o caso padrão.

O uso de classes como padrões no `match-case` permite que você crie objetos mais estruturados e com atributos bem definidos, tornando a correspondência de padrões mais legível e organizada. Essa é mais uma forma de tornar o código mais expressivo e eficiente usando o `match-case` introduzido no Python 3.10.