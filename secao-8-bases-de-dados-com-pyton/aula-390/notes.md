# Usando placeholders para maior segurança (bindings) no SQLite

Usando _placeholders_ para maior segurança, também conhecido como bindings, é uma prática recomendada ao lidar com consultas SQL no SQLite (e em outros bancos de dados) para evitar ataques de injeção de SQL. Em vez de concatenar diretamente os valores na consulta SQL, você usa _placeholders_ para representar os valores e, em seguida, liga esses valores aos _placeholders_ usando uma função ou método fornecido pelo driver do banco de dados.

No SQLite, o formato do placeholder é o símbolo de interrogação (`?`). Aqui está um exemplo de como usar _placeholders_ em uma consulta SQL usando Python:

```python
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Exemplo de consulta SQL com placeholders
nome = 'Alice'
idade = 25

# Consulta SQL com placeholders
sql = "SELECT * FROM usuarios WHERE nome = ? AND idade = ?"
cursor.execute(sql, (nome, idade))

# Obter resultados da consulta
resultados = cursor.fetchall()

# Exibir os resultados
for resultado in resultados:
    print(resultado)

# Fechar a conexão com o banco de dados
conn.close()
```

Neste exemplo, a consulta SQL contém dois _placeholders_ representados pelos pontos de interrogação (`?`). Em seguida, usamos o método `execute` do cursor para executar a consulta SQL e passamos uma tupla contendo os valores a serem ligados aos _placeholders_.

Ao usar _placeholders_, o driver do SQLite se encarrega de lidar com a formatação e _escaping_ adequados dos valores, garantindo que eles sejam tratados como dados, não como parte do comando SQL. Isso ajuda a prevenir ataques de injeção de SQL, onde um invasor poderia inserir instruções maliciosas nas entradas do usuário.

Portanto, o uso de _placeholders_ para maior segurança é uma prática recomendada ao escrever consultas SQL, pois ajuda a proteger seu banco de dados contra ataques de injeção de SQL.