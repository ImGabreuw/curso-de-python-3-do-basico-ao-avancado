# SELECT do SQL com fetch no SQLite3 do Python

No SQLite3 do Python, para realizar consultas `SELECT` e obter os resultados, você pode utilizar o método `execute` para executar a consulta e, em seguida, usar os métodos `fetchone`, `fetchall` ou `fetchmany` para recuperar os dados retornados pela consulta. Esses métodos são usados para buscar as linhas resultantes da consulta e retornam os dados em diferentes formatos.

Aqui está um exemplo de como executar uma consulta `SELECT` no SQLite3 do Python e usar os métodos `fetchone`, `fetchall` e `fetchmany` para recuperar os resultados:

```python
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Exemplo de consulta SELECT
sql = "SELECT nome, idade FROM usuarios"

# Executar a consulta
cursor.execute(sql)

# Recuperar um único resultado usando fetchone
resultado = cursor.fetchone()
print(resultado)  # Exibe uma tupla com os dados do resultado

# Recuperar todos os resultados usando fetchall
resultados = cursor.fetchall()
for resultado in resultados:
    print(resultado)  # Exibe uma tupla com os dados de cada resultado

# Recuperar um número específico de resultados usando fetchmany
cursor.execute(sql)
resultados = cursor.fetchmany(2)  # Recupera os dois primeiros resultados
for resultado in resultados:
    print(resultado)  # Exibe uma tupla com os dados de cada resultado

# Fechar a conexão com o banco de dados
conn.close()
```

Nesse exemplo, primeiro estabelecemos a conexão com o banco de dados e criamos um cursor para executar as consultas. Em seguida, definimos a consulta SELECT desejada.

Usamos o método `execute` para executar a consulta SQL. Depois disso, usamos o método `fetchone` para recuperar o primeiro resultado retornado pela consulta. O resultado é retornado como uma tupla de valores correspondentes às colunas selecionadas na consulta.

Também podemos usar o método `fetchall` para recuperar todos os resultados retornados pela consulta. Ele retorna uma lista de tuplas, onde cada tupla contém os dados de uma linha da consulta.

Além disso, o método `fetchmany` permite especificar o número de resultados que você deseja recuperar. Nesse exemplo, especificamos 2, o que significa que queremos recuperar os dois primeiros resultados da consulta.

É importante ressaltar que, após executar a consulta e recuperar os resultados, você deve percorrer os resultados imediatamente, pois eles serão perdidos assim que você executar outra consulta ou fechar a conexão com o banco de dados.