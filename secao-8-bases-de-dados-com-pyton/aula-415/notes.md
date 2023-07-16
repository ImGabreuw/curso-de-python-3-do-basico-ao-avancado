# SSCursor, SSDictCursor e scroll para conjuntos de dados muito grandes no PyMySQL

No PyMySQL, quando se trabalha com conjuntos de dados muito grandes, é possível utilizar os cursores `SSCursor` e `SSDictCursor` para otimizar o desempenho e reduzir o consumo de memória. Esses cursores são conhecidos como "cursores em rolagem" (scrollable cursors) e permitem percorrer os resultados da consulta em lotes, em vez de carregar todos os resultados na memória de uma só vez.

Aqui está um exemplo de como usar os cursores `SSCursor` e `SSDictCursor` e a técnica de "rolagem" para processar conjuntos de dados muito grandes no PyMySQL:

Usando SSCursor:

```python
import pymysql
from pymysql.cursors import SSCursor
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém as informações de conexão do banco de dados a partir das variáveis de ambiente
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Estabelece a conexão com o banco de dados
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name, cursorclass=SSCursor)

with connection:
    # Cria um cursor em rolagem para executar comandos SQL
    with connection.cursor() as cursor:
        # Executa a consulta SELECT
        select_query = "SELECT * FROM customers"
        cursor.execute(select_query)

        # Processa os 5 primeiros registros
        for row in cursor.fetchall_unbuffered():
          print(row)

          if row["id"] >= 5:
            break
```

Usando SSDictCursor:

```python
import pymysql
from pymysql.cursors import SSDictCursor
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém as informações de conexão do banco de dados a partir das variáveis de ambiente
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Estabelece a conexão com o banco de dados
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name, cursorclass=SSDictCursor)

with connection:
    # Cria um cursor em rolagem para executar comandos SQL
    with connection.cursor() as cursor:
        # Executa a consulta SELECT
        select_query = "SELECT * FROM customers"
        cursor.execute(select_query)

        # Processa os 5 primeiros registros
        for row in cursor.fetchall_unbuffered():
          print(row)

          if row["id"] >= 5:
            break
```

Nesses exemplos, importamos o módulo `pymysql` e `dotenv`, e carregamos as variáveis de ambiente do arquivo `.env` para obter as informações de conexão com o banco de dados.

Estabelecemos a conexão com o banco de dados usando o `with` statement, garantindo que a conexão seja fechada corretamente após a execução.

Criamos um cursor em rolagem (scrollable cursor) especificando o parâmetro `cursorclass=SSCursor` ou `cursorclass=SSDictCursor` na criação da conexão. O `SSCursor` é usado quando se deseja retornar os resultados como tuplas, enquanto o `SSDictCursor` é usado para retornar os resultados como dicionários.

Executamos a consulta SELECT desejada usando o método `execute()` do cursor.

Em seguida, utilizamos o método `fetchall_unbuffered()` para obter os resultados sob demanda, ou seja, essa função retorna um generator, desse modo apenas o registro atual será salvo em memória, reduzindo drasticamente o consumo de memória em grandes conjuntos de registros. Entretanto essa abordagem tem uma limitação, não é possível navegar para trás com o método `cursor.scroll()`. Além disso, o método `fetchall_unbuffered()` pode ter sua iteração interrompido, mas pode retomá-la posteriormente de onde parou.

Processamos os registros dentro de um loop, continuando a buscar e processar os registros em lotes até que não haja mais registros a serem lidos.

Dessa forma, usando os cursores `SSCursor` ou `SSDictCursor` e a técnica de rolagem, é possível lidar de forma eficiente com conjuntos de dados muito grandes no PyMySQL, reduzindo o consumo de memória e otimizando o desempenho ao processar os resultados em lotes.
