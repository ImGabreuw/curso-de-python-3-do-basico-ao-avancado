# Inserindo valores usando dicionários ao invés de iteráveis

No PyMySQL, ao usar o método `execute()` para inserir valores em uma tabela, você pode passar um dicionário como parâmetro em vez de um iterável (por exemplo uma tupla). Isso permite que você especifique os valores a serem inseridos usando nomes de colunas como chaves e os respectivos valores como valores no dicionário.

Aqui está um exemplo de como inserir valores em uma tabela usando um dicionário ao invés de um iterável no PyMySQL:

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

# Valores a serem inseridos representados como um dicionário
data = {
    'name': 'Luiz',
    'age': 25,
    'email': 'luiz@example.com'
}

# Estabelece a conexão com o banco de dados
connection = pymysql.connect(
  host=db_host,
  user=db_user,
  password=db_password,
  database=db_name
)

with connection:
    # Cria um cursor para executar comandos SQL
    with connection.cursor() as cursor:
        # Monta a consulta SQL para inserir os valores usando um dicionário
        insert_query = "INSERT INTO customers (name, age, email) VALUES (%(name)s, %(age)s, %(email)s)"

        # Executa a consulta SQL passando o dicionário como parâmetro
        cursor.execute(insert_query, data)

        # Confirma a operação e aplica as alterações no banco de dados
        connection.commit()
```

Neste exemplo, primeiro importamos o módulo `pymysql` e `dotenv`. Em seguida, carregamos as variáveis de ambiente do arquivo `.env` para obter as informações de conexão com o banco de dados.

Definimos os valores a serem inseridos como um dicionário chamado `data`. Cada chave do dicionário corresponde a uma coluna da tabela e o valor associado é o valor a ser inserido.

Estabelecemos a conexão com o banco de dados usando o `with` statement, o que garante que a conexão seja fechada corretamente após a execução.

Criamos um cursor para executar comandos SQL dentro do contexto da conexão. Em seguida, montamos a consulta SQL para inserir os valores na tabela, utilizando os nomes das colunas do dicionário como placeholders.

Por fim, executamos a consulta SQL passando o dicionário `data` como parâmetro para o método `execute()` do cursor. O PyMySQL mapeará automaticamente as chaves do dicionário para os placeholders na consulta SQL.

Após executar a inserção, confirmamos as alterações e aplicamos as modificações no banco de dados chamando o método `commit()` da conexão.

Dessa forma, é possível inserir valores em uma tabela utilizando um dicionário no PyMySQL, o que torna o código mais legível e flexível, pois os valores estão associados diretamente às colunas da tabela.
