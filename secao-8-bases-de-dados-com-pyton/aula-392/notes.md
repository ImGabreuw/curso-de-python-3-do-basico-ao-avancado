# execute e executemany com dicionários e lista de dicionários no SQLite

Ao trabalhar com dicionários ou listas de dicionários no SQLite, podemos usar as funções `execute` e `executemany` juntamente com os placeholders para inserir ou atualizar os dados no banco de dados. Essas funções permitem mapear os valores dos dicionários para os placeholders de forma eficiente.

Para que isso funcione é necessário que o placeholder tenha o mesmo nome da chave do dicionário com os dados a serem utilizados no comando SQL.

Aqui está um exemplo de como usar `execute` e `executemany` com dicionários e lista de dicionários no SQLite, usando placeholders, em Python:

### **Usando `execute` com dicionário**

```python
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Exemplo de inserção usando execute com dicionário
dados = {
    'nome': 'Alice',
    'idade': 25
}

# Consulta SQL com placeholders
sql = "INSERT INTO usuarios (nome, idade) VALUES (:nome, :idade)"

# Executar a inserção com execute
cursor.execute(sql, dados)

# Confirmar a transação
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
```

Nesse exemplo, usamos a função `execute` para inserir um conjunto de valores representados por um dicionário na tabela "usuarios". A consulta SQL utiliza placeholders no formato `:chave`, onde cada chave do dicionário é mapeada para o respectivo placeholder.

**Usando `executemany` com lista de dicionários:**

```python
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Exemplo de inserção usando executemany com lista de dicionários
dados = [
    {
        'nome': 'Alice',
        'idade': 25
    },
    {
        'nome': 'Bob',
        'idade': 30
    },
    {
        'nome': 'Charlie',
        'idade': 35
    }
]

# Consulta SQL com placeholders
sql = "INSERT INTO usuarios (nome, idade) VALUES (:nome, :idade)"

# Executar a inserção de vários valores com executemany
cursor.executemany(sql, dados)

# Confirmar a transação
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
```

Nesse exemplo, utilizamos a função `executemany` para inserir múltiplos conjuntos de valores representados por uma lista de dicionários na tabela "usuarios". A consulta SQL também usa placeholders no formato `:chave` para mapear as chaves dos dicionários aos placeholders correspondentes.

Tanto com `execute` quanto com `executemany`, o uso de dicionários ou listas de dicionários juntamente com placeholders facilita a inserção ou atualização de dados no SQLite, pois permite mapear os valores dos dicionários diretamente para os placeholders de forma eficiente e segura contra injeção de SQL.
