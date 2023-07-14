# Criando minha primeira tabela no SQLite3 (DBeaver opcional)

Para criar sua primeira tabela no SQLite3 usando Python, você precisará seguir os seguintes passos:

1. Importe o módulo `sqlite3`:

   ```python
   import sqlite3
   ```

2. Conecte-se ao banco de dados SQLite:

   ```python
   connection = sqlite3.connect('db.sqlite3')
   ```

   Nesse exemplo, estamos conectando ao banco de dados SQLite chamado "db.sqlite3". Se o arquivo não existir, ele será criado automaticamente.

3. Crie um objeto cursor:

   ```python
   cursor = connection.cursor()
   ```

   O cursor é usado para executar comandos SQL e interagir com o banco de dados.

4. Execute o comando SQL para criar a tabela:

   ```python
   TABLE_NAME = "costumers"

   cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "name TEXT,"
    "weight REAL"
    ")"
   )
   ```

   Nesse exemplo, estamos criando uma tabela chamada "costumers" com três colunas: "id" (chave primária do tipo INTEGER), "nome" (do tipo TEXT) e "weight" (do tipo REAL).

5. Confirme a operação:

   ```python
   connection.commit()
   ```

   É importante chamar o método `commit()` após executar comandos que alteram o banco de dados (como criar tabelas, inserir, atualizar ou excluir dados) para garantir que as alterações sejam salvas permanentemente no banco de dados.

6. Feche o cursor e a conexão com o banco de dados:

   ```python
   cursor.close()
   connection.close()
   ```

   É uma boa prática fechar a conexão com o banco de dados quando você terminar de usá-lo.

Aqui está o exemplo completo de como criar sua primeira tabela no SQLite3 usando Python:

```python
import sqlite3

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

TABLE_NAME = "costumers"

cursor.execute(
  f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
  "("
  "id INTEGER PRIMARY KEY AUTOINCREMENT,"
  "name TEXT,"
  "weight REAL"
  ")"
)
connection.commit()

cursor.close()
connection.close()
```

Após executar o código acima, você terá um banco de dados SQLite chamado "db.sqlite3" com uma tabela chamada "costumers" pronta para ser usada. Você pode adicionar dados à tabela, fazer consultas, atualizações e muito mais. Consulte a documentação oficial do módulo `sqlite3` do Python para aprender sobre essas operações.
