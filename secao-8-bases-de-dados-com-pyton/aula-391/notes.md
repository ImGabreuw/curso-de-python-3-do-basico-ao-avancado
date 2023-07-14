# executemany - Inserindo vários valores com placeholders no SQLite

Ao lidar com inserção de vários valores em uma tabela no SQLite, a função `executemany` é útil, pois permite inserir múltiplos conjuntos de valores usando _placeholders_. Essa abordagem é mais eficiente do que executar várias consultas `execute` separadas.

Aqui está um exemplo de como usar o `executemany` para inserir vários valores em uma tabela no SQLite, usando _placeholders_, em Python:

```python
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Exemplo de inserção de vários valores com placeholders
dados = [
    ('Alice', 25),
    ('Bob', 30),
    ('Charlie', 35)
]

# Consulta SQL com placeholders
sql = "INSERT INTO usuarios (nome, idade) VALUES (?, ?)"

# Executar a inserção de vários valores
cursor.executemany(sql, dados)

# Confirmar a transação
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
```

Nesse exemplo, temos uma tabela chamada "usuarios" com duas colunas: "nome" e "idade". Usamos a função `executemany` para inserir múltiplos conjuntos de valores na tabela. A variável `dados` é uma lista de tuplas contendo os valores a serem inseridos. A consulta SQL contém dois _placeholders_ representados pelos pontos de interrogação (`?`). Em seguida, usamos `executemany` para executar a inserção dos valores, passando a consulta SQL e a lista de dados.

Após a chamada do `executemany`, é importante confirmar a transação usando `commit()` para garantir que as alterações sejam salvas permanentemente no banco de dados.

O uso de `executemany` com _placeholders_ é eficiente e recomendado para inserir vários valores de uma vez, pois reduz o número de chamadas ao banco de dados e aproveita os recursos do SQLite de forma mais eficiente.