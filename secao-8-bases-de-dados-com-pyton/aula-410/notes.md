# Lendo valores com SELECT, cursor.execute e cursor.fetchall no PyMySQL

No PyMySQL, para ler valores de uma tabela usando uma consulta SELECT, você pode usar o método `execute()` do objeto cursor para executar a consulta e, em seguida, o método `fetchall()` para recuperar todos os resultados da consulta em forma de lista de tuplas. O `fetchall()` retorna todos os registros selecionados pela consulta.

Aqui está um exemplo de como ler valores de uma tabela usando SELECT, `cursor.execute()` e `cursor.fetchall()` no PyMySQL:

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

# Estabelece a conexão com o banco de dados
with pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name) as connection:
    # Cria um cursor para executar comandos SQL
    with connection.cursor() as cursor:
        # Executa a consulta SELECT
        select_query = "SELECT * FROM customers"
        cursor.execute(select_query)

        # Obtém todos os resultados da consulta
        results = cursor.fetchall()

        # Exibe os resultados
        for row in results:
            print(row)
```

Neste exemplo, importamos os módulos `pymysql` e `dotenv` e carregamos as variáveis de ambiente do arquivo `.env` para obter as informações de conexão com o banco de dados.

Estabelecemos a conexão com o banco de dados usando o `with` statement, garantindo que a conexão seja fechada corretamente após a execução.

Criamos um cursor para executar comandos SQL dentro do contexto da conexão. Em seguida, executamos a consulta SELECT desejada usando o método `execute()` do cursor. A consulta selecionará todos os registros da tabela "customers".

Em seguida, utilizamos o método `fetchall()` para obter todos os resultados da consulta como uma lista de tuplas. Cada tupla representa um registro da tabela, com os valores nas posições correspondentes às colunas selecionadas.

Finalmente, percorremos a lista de resultados e exibimos os valores de cada registro.

Ao executar o código acima, os valores selecionados pela consulta SELECT serão exibidos. Você pode personalizar a consulta SELECT para selecionar colunas específicas, adicionar condições, ordenar os resultados, entre outras opções, de acordo com as necessidades do seu aplicativo.
