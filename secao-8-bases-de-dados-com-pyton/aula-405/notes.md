# CREATE TABLE para criar tabela com PRIMARY KEY no PyMySQL

No PyMySQL, você pode usar uma consulta SQL `CREATE TABLE` para criar uma tabela em um banco de dados MySQL. Ao criar a tabela, você pode definir uma coluna como `PRIMARY KEY`, o que a torna única e identifica exclusivamente cada registro na tabela.

Aqui está um exemplo de como criar uma tabela com uma coluna `PRIMARY KEY` usando o PyMySQL:

```python
import pymysql
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém as informações de conexão do banco de dados a partir das variáveis de ambiente
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Estabelece a conexão com o banco de dados MySQL
connection = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

with connection:
  # Cria um cursor para executar comandos SQL
  with connection.cursor() as cursor:
    # Define a consulta SQL para criar a tabela
    query = """
    CREATE TABLE IF NOT EXISTS customers (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        age INT NOT NULL,
        PRIMARY KEY (id)
    )
    """

    # Executa a consulta SQL
    cursor.execute(query)

    # Confirma a operação e aplica as alterações no banco de dados
    connection.commit()
```

Neste exemplo, primeiro importamos o módulo `pymysql`. Em seguida, estabelecemos a conexão com o banco de dados MySQL utilizando as informações de host, usuário, senha e nome do banco de dados.

Em seguida, criamos um objeto `cursor` com o _context manager_ que nos permite executar comandos SQL no banco de dados e após o seu uso fechá-la corretamente.

Na consulta, criamos uma tabela chamada "costumers" com três colunas: "id", "name" e "age". A coluna "id" é definida como `PRIMARY KEY` e `AUTO_INCREMENT`, o que significa que ela será única e incrementada automaticamente a cada novo registro inserido na tabela.

Executamos a consulta SQL usando o método `execute` do cursor, passando a consulta como parâmetro.

Por fim, confirmamos a operação e aplicamos as alterações no banco de dados utilizando o método `commit` da conexão.
