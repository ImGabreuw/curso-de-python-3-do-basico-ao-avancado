# Criando meu primeiro arquivo do SQLite (db.sqlite3)

SQLite é um sistema de gerenciamento de banco de dados relacional leve, rápido e embutido que não requer um servidor separado. É amplamente utilizado em aplicativos que exigem um banco de dados local e simples de implementar. O Python possui um módulo chamado `sqlite3` que permite a interação com bancos de dados SQLite usando código Python.

Aqui está um exemplo básico de como usar o SQLite com Python:

```python
import sqlite3

# Conectar-se ao banco de dados (se não existir, será criado)
conexao = sqlite3.connect('banco_dados.sqlite3')

# Criar um cursor
cursor = conexao.cursor()

# Criar uma tabela
cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)')

# Inserir dados na tabela
cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', ('João', 25))
cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', ('Maria', 30))
conexao.commit()

# Executar uma consulta
cursor.execute('SELECT * FROM usuarios')
usuarios = cursor.fetchall()

# Exibir os resultados
for usuario in usuarios:
    print(usuario)

# Fechar a conexão com o banco de dados
conexao.close()
```

Neste exemplo, o código cria um banco de dados SQLite chamado "banco_dados.db" (se ele não existir) usando a função `connect()` do módulo `sqlite3`. Em seguida, um cursor é criado para executar comandos SQL no banco de dados.

Uma tabela chamada "usuarios" é criada usando o comando `CREATE TABLE IF NOT EXISTS`. Em seguida, alguns dados são inseridos na tabela usando o comando `INSERT INTO`.

Depois disso, uma consulta é executada usando o comando `SELECT * FROM usuarios`, e os resultados são recuperados usando o método `fetchall()`. Finalmente, os resultados são exibidos no console.

Por fim, a conexão com o banco de dados é fechada chamando o método `close()`.
