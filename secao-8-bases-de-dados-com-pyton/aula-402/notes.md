# PyMySQL - um cliente MySQL feito em Python Puro 

PyMySQL é uma biblioteca em Python que permite a conexão e interação com bancos de dados MySQL utilizando apenas código Python puro, sem a necessidade de dependências externas. Ela implementa o protocolo MySQL diretamente em Python, oferecendo uma interface simples e fácil de usar para trabalhar com bancos de dados MySQL.

Primeiramente, é necessário instalar a biblioteca PyMySQL com o gerenciador de dependências `pip`:

```console
$ pip install pymysql
```

Aqui está um exemplo de como usar o PyMySQL para se conectar a um banco de dados MySQL:

```python
import pymysql

# Estabelece a conexão com o banco de dados
connection = pymysql.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='base_de_dados'
)

# Cria um cursor para executar comandos SQL
cursor = connection.cursor()

# Executa uma consulta SQL
query = "SELECT * FROM tabela"
cursor.execute(query)

# Obtém os resultados da consulta
results = cursor.fetchall()

# Exibe os resultados
for row in results:
    print(row)

# Fecha a conexão com o banco de dados
connection.close()
```

Neste exemplo, primeiro importamos o módulo `pymysql`. Em seguida, estabelecemos a conexão com o banco de dados MySQL utilizando as informações de host, usuário, senha e nome do banco de dados.

Em seguida, criamos um objeto `cursor` que nos permite executar comandos SQL no banco de dados.

Executamos uma consulta SQL usando o método `execute` do cursor, passando a consulta como parâmetro. Podemos então recuperar os resultados da consulta usando o método `fetchall`, que retorna todas as linhas resultantes da consulta como uma lista de tuplas.

Finalmente, percorremos os resultados e os exibimos. É importante lembrar de fechar a conexão com o banco de dados utilizando o método `close` para liberar os recursos adequadamente.

O PyMySQL fornece uma ampla gama de recursos e métodos para interagir com bancos de dados MySQL, incluindo inserção, atualização e exclusão de dados, além de suporte a transações.