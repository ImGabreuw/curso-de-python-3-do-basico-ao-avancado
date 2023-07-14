# UPDATE no SQLite com Python

No SQLite com Python, a operação `UPDATE` é usada para modificar os dados existentes em uma tabela. Ela permite atualizar valores de colunas em registros específicos com base em uma condição definida pela cláusula `WHERE`.

Aqui está um exemplo de como usar a operação `UPDATE` no SQLite com Python:

```python
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Exemplo de UPDATE com a cláusula WHERE
sql = "UPDATE usuarios SET idade = 30 WHERE nome = 'Alice'"

# Executar a operação de atualização
cursor.execute(sql)

# Confirmar a transação
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
```

Nesse exemplo, estamos usando a cláusula `UPDATE` para modificar o valor da coluna "idade" na tabela "usuarios". A consulta SQL possui a cláusula `SET idade = 30` para definir o novo valor da coluna "idade" como 30. A cláusula `WHERE nome = 'Alice'` é usada para especificar a condição em que a atualização deve ser realizada, neste caso, apenas para o registro com o nome "Alice".

Após a execução da consulta, a transação é confirmada usando `commit()` para salvar permanentemente as alterações no banco de dados.

É importante ressaltar que a cláusula `WHERE` é essencial para garantir que apenas os registros desejados sejam atualizados. Sem a cláusula `WHERE`, a operação de atualização afetará todos os registros da tabela. Portanto, é importante especificar a condição correta para evitar atualizações indesejadas.

Além disso, ao usar a operação `UPDATE` no SQLite com Python, é necessário confirmar a transação com `commit()` para salvar as alterações permanentemente no banco de dados.