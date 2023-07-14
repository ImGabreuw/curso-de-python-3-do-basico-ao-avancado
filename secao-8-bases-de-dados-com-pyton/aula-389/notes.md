# Inserindo valores (INSERT INTO), DELETE sem WHERE e zerando a sqlite_sequence

## **Inserção de valores com `INSERT INTO`**

A cláusula `INSERT INTO` é usada para adicionar novos registros a uma tabela. Ela permite especificar quais colunas serão preenchidas e os valores correspondentes a serem inseridos.

A sintaxe básica do comando `INSERT INTO` é a seguinte:

```sql
INSERT INTO nome_tabela (coluna1, coluna2, coluna3, ...)
VALUES (valor1, valor2, valor3, ...);
```

Aqui está um exemplo para ilustrar como inserir um novo registro em uma tabela chamada `clientes`:

```sql
INSERT INTO clientes (nome, idade, email)
VALUES ('João', 30, 'joao@example.com');
```

Este comando insere um novo registro na tabela `clientes` com os valores 'João' para a coluna `nome`, 30 para a coluna `idade` e 'joao@example.com' para a coluna `email`.

## **Exclusão de registros sem a cláusula `WHERE`**

A cláusula `DELETE` é usada para excluir registros de uma tabela. Se não especificarmos uma cláusula `WHERE`, todos os registros da tabela serão excluídos.

A sintaxe básica do comando `DELETE` é a seguinte:

```sql
DELETE FROM nome_tabela;
```

Aqui está um exemplo de como excluir todos os registros de uma tabela chamada `produtos`:

```sql
DELETE FROM produtos;
```

Este comando exclui todos os registros da tabela `produtos`.

É importante ter cuidado ao usar essa operação, pois ela é irreversível e todos os dados serão perdidos.

## **Zerando a `sqlite_sequence`**

A tabela `sqlite_sequence` é usada internamente pelo SQLite para manter o controle dos valores de sequência (auto incremento) em uma tabela que possui uma coluna com a propriedade `AUTOINCREMENT`.

Se você quiser redefinir a sequência do contador de uma tabela específica, pode atualizar o valor correspondente na tabela `sqlite_sequence`.

Aqui está um exemplo de como zerar a sequência do contador para uma tabela chamada `tabela_exemplo`:

```sql
UPDATE sqlite_sequence SET seq = 0 WHERE name = 'tabela_exemplo';
```

Este comando atualiza o valor da coluna `seq` para 0 na tabela `sqlite_sequence` para a tabela com o nome 'tabela_exemplo'. Isso fará com que o próximo valor autoincrementado comece novamente em 1 quando um novo registro for inserido na tabela `tabela_exemplo`.

Lembre-se de substituir 'tabela_exemplo' pelo nome da tabela específica em que você deseja redefinir a sequência.
