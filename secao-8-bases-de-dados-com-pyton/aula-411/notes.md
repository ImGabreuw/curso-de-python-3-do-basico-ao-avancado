# Lendo valores com WHERE (mais uma vez, explico cuidados com _SQL Injection_)

Ao ler valores de uma tabela usando uma cláusula WHERE em uma consulta SELECT no PyMySQL, é possível filtrar os resultados com base em uma condição específica. No entanto, é importante tomar cuidado para evitar ataques de _SQL Injection_ ao utilizar valores fornecidos pelo usuário em uma cláusula WHERE.

Aqui está um exemplo de como ler valores com uma cláusula WHERE e evitar _SQL Injection_ no PyMySQL:

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

# Valor fornecido pelo usuário
user_input = "John"

# Estabelece a conexão com o banco de dados
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)

with connection:
    # Cria um cursor para executar comandos SQL
    with connection.cursor() as cursor:
        # Executa a consulta SELECT com cláusula WHERE e parâmetro seguro
        select_query = "SELECT * FROM customers WHERE name = %s"
        cursor.execute(select_query, (user_input,))

        # Obtém todos os resultados da consulta
        results = cursor.fetchall()

        # Exibe os resultados
        for row in results:
            print(row)
```

Neste exemplo, importamos os módulos `pymysql` e `dotenv` e carregamos as variáveis de ambiente do arquivo `.env` para obter as informações de conexão com o banco de dados.

Definimos o valor fornecido pelo usuário na variável `user_input`. É importante que este valor seja obtido de forma segura, por exemplo, através de um formulário web ou de uma entrada controlada.

Em seguida, estabelecemos a conexão com o banco de dados usando o `with` statement, garantindo que a conexão seja fechada corretamente após a execução.

Criamos um cursor para executar comandos SQL dentro do contexto da conexão. A consulta SELECT utiliza uma cláusula WHERE para filtrar os resultados com base no valor fornecido pelo usuário. Utilizamos `%s` como um placeholder na consulta.

Ao chamar o método `execute()` do cursor, passamos o valor fornecido pelo usuário como um segundo argumento, mas o PyMySQL cuida da segurança e evita _SQL Injection_ ao substituir corretamente o valor do placeholder `%s` na consulta.

Em seguida, utilizamos o método `fetchall()` para obter todos os resultados da consulta como uma lista de tuplas. Cada tupla representa um registro da tabela, com os valores nas posições correspondentes às colunas selecionadas.

Por fim, percorremos a lista de resultados e exibimos os valores de cada registro.

Ao utilizar parâmetros seguros como descrito acima, você garante que o valor fornecido pelo usuário seja tratado de forma segura e evita ataques de _SQL Injection_. É importante sempre utilizar parâmetros seguros ao incorporar valores fornecidos pelo usuário em consultas SQL para manter a segurança do sistema.
