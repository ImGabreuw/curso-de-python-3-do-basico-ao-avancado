# rowcount, rownumber e lastrowid para detalhes de consultas executadas

No PyMySQL, existem algumas propriedades e métodos úteis para obter detalhes sobre as consultas executadas, como `rowcount`, `rownumber` e `lastrowid`.

- `rowcount`: A propriedade `rowcount` retorna o número de linhas afetadas pela consulta mais recente. Ela é útil para saber quantas linhas foram modificadas, inseridas ou excluídas em uma operação de atualização ou deleção.

- `rownumber`: A propriedade `rownumber` retorna o número da linha atual sendo processada durante um loop que itera sobre os resultados de uma consulta. Essa propriedade é útil para acompanhar o número de linha atual durante o processamento dos resultados.

- `lastrowid`: O método `lastrowid` retorna o ID do último registro inserido em uma tabela com uma coluna de autoincremento. Ele é útil quando você precisa recuperar o ID do último registro inserido para uso posterior.

Aqui está um exemplo de como usar essas propriedades e método no PyMySQL:

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
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)

with connection:
    # Cria um cursor para executar comandos SQL
    with connection.cursor() as cursor:
        # Executa uma consulta SELECT
        select_query = "SELECT * FROM customers"
        cursor.execute(select_query)

        # Obtém todos os resultados da consulta
        results = cursor.fetchall()

        # Exibe o número de linhas retornadas pela consulta
        print("Número de linhas retornadas:", cursor.rowcount)

        # Processa os resultados
        for row in results:
            row_number = cursor.rownumber  # Número da linha atual
            customer_id = row["id"]
            customer_name = row["name"]

            print(f"Linha {row_number}: ID={customer_id}, Nome={customer_name}")

        # Executa uma inserção
        insert_query = "INSERT INTO customers (name) VALUES ('John')"
        cursor.execute(insert_query)

        # Obtém o ID do último registro inserido
        last_insert_id = cursor.lastrowid
        print("Último ID inserido:", last_insert_id)
```

Neste exemplo, importamos o módulo `pymysql` e `dotenv`, e carregamos as variáveis de ambiente do arquivo `.env` para obter as informações de conexão com o banco de dados.

Estabelecemos a conexão com o banco de dados usando o `with` statement, garantindo que a conexão seja fechada corretamente após a execução.

Criamos um cursor para executar comandos SQL dentro do contexto da conexão.

Executamos uma consulta SELECT e usamos o método `fetchall()` para obter todos os resultados. Em seguida, utilizamos a propriedade `rowcount` para obter o número de linhas retornadas pela consulta.

Em seguida, percorremos os resultados usando um loop e exibimos o número da linha atual (`rownumber`), o ID do cliente (`id`) e o nome do cliente (`name`).

Em seguida, executamos uma inserção e utilizamos o método `lastrowid` para obter o ID do último registro inserido.

Assim, podemos utilizar essas propriedades e método para obter informações úteis sobre as consultas executadas, como o número de linhas afetadas, o número da linha atual e o ID do último registro inserido.
