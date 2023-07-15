# TRUNCATE e INSERT p/ limpar e criar valores na tabela com um ou mais cursores

No PyMySQL, você pode usar as instruções SQL `TRUNCATE` e `INSERT` para limpar uma tabela existente e inserir novos valores nela. Além disso, você pode usar um ou mais cursores para executar as consultas SQL correspondentes.

Aqui está um exemplo de como limpar uma tabela usando a instrução `TRUNCATE` e inserir novos valores usando a instrução `INSERT` com um ou mais cursores no PyMySQL:

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

with connection:
  with connection.cursor() as cursor1
    # Limpa a tabela existente usando TRUNCATE
    truncate_query = "TRUNCATE TABLE customers"
    cursor1.execute(truncate_query)

    # Confirma a operação e aplica as alterações no banco de dados
    connection.commit()

  with connection.cursor() as cursor2
    # Insere novos valores usando INSERT
    insert_query = "INSERT INTO customers (name, age) VALUES (%s, %s)"
    data = ("Luiz", 25)
    result = cursor2.execute(insert_query, data)

    # Confirma a operação e aplica as alterações no banco de dados
    connection.commit()

    # Exibe o número de linhas afetadas pela query SQL no banco de dados
    print(result)
```

Neste exemplo, importamos o módulo `pymysql` e estabelecemos a conexão com o banco de dados MySQL usando as informações de host, usuário, senha e nome do banco de dados.

Em seguida, criamos dois objetos de cursor, `cursor1` e `cursor2` com _context manager_, para executar comandos SQL no banco de dados e depois fechá-las corretamente.

Usamos o primeiro cursor, `cursor1`, para executar a instrução `TRUNCATE` na tabela existente. A instrução `TRUNCATE` remove todos os registros da tabela, mas mantém a estrutura da tabela intacta.

Em seguida, usamos o segundo cursor, `cursor2`, para executar a instrução `INSERT` com o método `execute`. A instrução `INSERT` insere novos valores na tabela. Utilizamos o placeholder `%s` para os valores que serão substituídos pelos valores reais na consulta. O método `execute` permite inserir 1 conjunto de valores passando uma tuplas contendo os valores a serem inseridos.

Por fim, confirmamos as alterações e aplicamos as modificações no banco de dados chamando o método `commit` da conexão.