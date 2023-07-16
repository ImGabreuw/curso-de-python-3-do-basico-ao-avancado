# Trocando o cursor para retornar dicionários - pymysql.cursors.DictCursor

No PyMySQL, é possível alterar o comportamento do cursor para retornar dicionários em vez de tuplas ao executar consultas SQL. Isso pode ser feito utilizando o cursor `pymysql.cursors.DictCursor`, que retorna cada registro da consulta como um dicionário, em que as colunas são mapeadas para seus respectivos valores.

Aqui está um exemplo de como trocar o cursor para retornar dicionários usando `pymysql.cursors.DictCursor` no PyMySQL:

```python
import pymysql
import pymysql.cursors
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém as informações de conexão do banco de dados a partir das variáveis de ambiente
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Estabelece a conexão com o banco de dados
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name, cursorclass=pymysql.cursors.DictCursor)

with connection:
    # Cria um cursor para executar comandos SQL
    with connection.cursor() as cursor:
        # Executa a consulta SELECT
        select_query = "SELECT * FROM customers"
        cursor.execute(select_query)

        # Obtém todos os resultados da consulta como dicionários
        results = cursor.fetchall()

        # Exibe os resultados
        for row in results:
            print(row)
```

Neste exemplo, importamos o módulo `pymysql.cursors` e `dotenv`, e carregamos as variáveis de ambiente do arquivo `.env` para obter as informações de conexão com o banco de dados.

Estabelecemos a conexão com o banco de dados usando o `with` statement, garantindo que a conexão seja fechada corretamente após a execução.

Criamos um cursor para executar comandos SQL dentro do contexto da conexão, e passamos o parâmetro `cursorclass=pymysql.cursors.DictCursor` ao criar a conexão. Isso informa ao PyMySQL para utilizar o `DictCursor`, que retornará os resultados das consultas como dicionários.

Em seguida, executamos a consulta SELECT desejada usando o método `execute()` do cursor.

Utilizando o método `fetchall()`, obtemos todos os resultados da consulta como uma lista de dicionários. Cada dicionário representa um registro da tabela, em que as chaves correspondem aos nomes das colunas e os valores são os valores das colunas correspondentes.

Por fim, percorremos a lista de resultados e exibimos os valores de cada registro.

Ao utilizar o `pymysql.cursors.DictCursor`, é possível ter os resultados das consultas SQL diretamente como dicionários, o que pode facilitar o acesso aos valores através das chaves (nome das colunas).