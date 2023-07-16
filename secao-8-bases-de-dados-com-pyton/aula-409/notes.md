# Inserindo vários valores com uma consulta só usando iteráveis ou dicionários

No PyMySQL, é possível inserir múltiplos valores em uma tabela usando uma única consulta SQL através do método `executemany()`. Você pode passar uma lista de iteráveis ou uma lista de dicionários como parâmetro para o `executemany()`, permitindo a inserção eficiente de vários registros de uma só vez.

Aqui estão exemplos de como inserir múltiplos valores usando uma única consulta SQL no PyMySQL com iteráveis ou dicionários:

Exemplo usando iteráveis:

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

# Valores a serem inseridos representados como uma lista de tuplas
data = [
    ('Luiz', 25),
    ('Maria', 30),
    ('João', 28)
]

# Estabelece a conexão com o banco de dados
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)

with connection:
    # Cria um cursor para executar comandos SQL
    with connection.cursor() as cursor:
        # Monta a consulta SQL para inserir os valores usando o método executemany() com iteráveis
        insert_query = "INSERT INTO customers (name, age) VALUES (%s, %s)"

        # Executa a consulta SQL passando a lista de tuplas como parâmetro
        cursor.executemany(insert_query, data)

    # Confirma a operação e aplica as alterações no banco de dados
    connection.commit()
```

Exemplo usando dicionários:

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

# Valores a serem inseridos representados como uma lista de dicionários
data = [
    {'name': 'Luiz', 'age': 25},
    {'name': 'Maria', 'age': 30},
    {'name': 'João', 'age': 28}
]

# Estabelece a conexão com o banco de dados
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)

with connection:
    # Cria um cursor para executar comandos SQL
    with connection.cursor() as cursor:
        # Monta a consulta SQL para inserir os valores usando o método executemany() com dicionários
        insert_query = "INSERT INTO customers (name, age) VALUES (%(name)s, %(age)s)"

        # Executa a consulta SQL passando a lista de dicionários como parâmetro
        cursor.executemany(insert_query, data)

    # Confirma a operação e aplica as alterações no banco de dados
    connection.commit()
```

Nos exemplos acima, primeiro importamos o módulo `pymysql` e `dotenv`. Em seguida, carregamos as variáveis de ambiente do arquivo `.env` para obter as informações de conexão com o banco de dados.

Definimos os valores a serem inseridos como uma lista de iteráveis (tuplas) ou uma lista de dicionários chamada `data`. Cada iterável ou dicionário representa um registro a ser inserido na tabela.

Em seguida, estabelecemos a conexão com o banco de dados usando o `with` statement, que garante o fechamento adequado da conexão.

Criamos um cursor para executar comandos SQL dentro do contexto da conexão. Em seguida, montamos a consulta SQL para inserir os valores na tabela.

Usamos o método `executemany()` do cursor para executar a consulta SQL. Passamos a consulta SQL como o primeiro parâmetro e a lista de iteráveis ou dicionários como o segundo parâmetro.

O PyMySQL executa a consulta SQL várias vezes, uma para cada registro na lista de iteráveis ou dicionários, inserindo todos os registros em uma única operação.

Após executar a inserção, confirmamos as alterações e aplicamos as modificações no banco de dados chamando o método `commit()` da conexão.

Dessa forma, é possível inserir múltiplos valores em uma tabela com uma única consulta SQL no PyMySQL, aproveitando a eficiência da inserção em massa e melhorando o desempenho do seu aplicativo.
