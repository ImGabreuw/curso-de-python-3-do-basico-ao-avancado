# Apagando valores com DELETE, WHERE e placeholders no PyMySQL

No PyMySQL, é possível apagar valores de uma tabela usando a instrução DELETE com a cláusula WHERE para especificar uma condição de exclusão. Para garantir a segurança e evitar SQL Injection, é recomendado utilizar placeholders nos quais os valores serão substituídos de forma segura durante a execução da consulta.

Aqui está um exemplo de como apagar valores de uma tabela usando DELETE, WHERE e placeholders no PyMySQL:

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
        # Executa a instrução DELETE com a cláusula WHERE e placeholders
        delete_query = "DELETE FROM customers WHERE name = %s"
        cursor.execute(delete_query, (user_input,))

    # Confirma a operação e aplica as alterações no banco de dados
    connection.commit()
```

Neste exemplo, importamos os módulos `pymysql` e `dotenv` e carregamos as variáveis de ambiente do arquivo `.env` para obter as informações de conexão com o banco de dados.

Definimos o valor fornecido pelo usuário na variável `user_input`. Como mencionado anteriormente, é importante que esse valor seja obtido de forma segura, por exemplo, por meio de um formulário web ou de uma entrada controlada.

Estabelecemos a conexão com o banco de dados usando o `with` statement, garantindo que a conexão seja fechada corretamente após a execução.

Criamos um cursor para executar comandos SQL dentro do contexto da conexão. A instrução DELETE é utilizada para remover registros da tabela "customers", utilizando a cláusula WHERE para especificar a condição de exclusão. Neste caso, estamos excluindo registros em que o nome seja igual ao valor fornecido pelo usuário.

Ao chamar o método `execute()` do cursor, passamos o valor fornecido pelo usuário como um segundo argumento, utilizando um placeholder `%s` na consulta. O PyMySQL cuida da substituição segura desse valor durante a execução da consulta, evitando SQL Injection.

Em seguida, chamamos o método `commit()` da conexão para confirmar a operação e aplicar as alterações no banco de dados.

Dessa forma, é possível apagar valores de uma tabela usando a instrução DELETE, WHERE e placeholders no PyMySQL, garantindo a segurança e evitando ataques de SQL Injection.