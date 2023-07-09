# csv.writer e csv.DictWriter para escrever em CSV

O módulo `csv` do Python também fornece as classes `csv.writer` e `csv.DictWriter` para escrever dados em arquivos CSV.

Essas classes do módulo `csv` do Python facilitam a escrita de dados em arquivos CSV, permitindo a formatação adequada dos valores e a definição dos nomes das colunas.

### `csv.writer`

A classe `csv.writer` é usada para escrever dados em um arquivo CSV. Ela permite escrever linhas de valores em formato CSV. Aqui está um exemplo:

```python
import csv

dados = [
    ['nome', 'idade', 'cidade'],
    ['João', 30, 'São Paulo'],
    ['Maria', 25, 'Rio de Janeiro']
]

with open('dados.csv', 'w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)

    for linha in dados:
        escritor.writerow(linha)
```

Nesse exemplo, temos uma lista `dados` contendo linhas de valores a serem escritas no arquivo CSV. O arquivo `dados.csv` é aberto em modo de escrita. Um objeto `csv.writer` é criado passando o arquivo como argumento.

Em seguida, iteramos sobre as linhas da lista `dados` e usamos o método `writerow()` para escrever cada linha no arquivo CSV.

O parâmetro `newline=''` é usado para evitar que linhas em branco sejam adicionadas entre as linhas de dados no arquivo CSV.

### `csv.DictWriter`

A classe `csv.DictWriter` é usada para escrever dados em um arquivo CSV com base em dicionários. Ela permite escrever linhas de valores a partir de dicionários, usando as chaves como nomes das colunas. Aqui está um exemplo:

```python
import csv

dados = [
    {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'},
    {'nome': 'Maria', 'idade': 25, 'cidade': 'Rio de Janeiro'}
]

colunas = ['nome', 'idade', 'cidade']

with open('dados.csv', 'w', newline='') as arquivo_csv:
    escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)

    escritor.writeheader()

    for linha in dados:
        escritor.writerow(linha)
```

Nesse exemplo, temos uma lista `dados` contendo dicionários que representam as linhas de dados a serem escritas no arquivo CSV. A lista `colunas` define os nomes das colunas.

O arquivo `dados.csv` é aberto em modo de escrita. Um objeto `csv.DictWriter` é criado passando o arquivo e as colunas como argumentos.

Usamos o método `writeheader()` para escrever a linha de cabeçalho no arquivo CSV, usando as chaves dos dicionários como nomes das colunas.

Em seguida, iteramos sobre os dicionários da lista `dados` e usamos o método `writerow()` para escrever cada linha no arquivo CSV.

O parâmetro `newline=''` é usado para evitar que linhas em branco sejam adicionadas entre as linhas de dados no arquivo CSV.
