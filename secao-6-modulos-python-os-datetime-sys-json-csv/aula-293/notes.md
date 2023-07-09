# csv.reader e csv.DictReader para ler arquivos CSV

O módulo `csv` do Python fornece as classes `csv.reader` e `csv.DictReader` para ler arquivos CSV. Essas classes permitem a leitura dos dados do arquivo CSV linha por linha, facilitando o processamento dos valores.

Essas classes do módulo `csv` facilitam a leitura e o processamento de arquivos CSV no Python. Dependendo da estrutura do arquivo CSV e das necessidades do seu projeto, você pode escolher entre `csv.reader` ou `csv.DictReader` para ler e manipular os dados do arquivo CSV de forma adequada.

### `csv.reader`

A classe `csv.reader` é usada para ler arquivos CSV e retorna os valores como listas de strings. Cada linha do arquivo CSV é retornada como uma lista, em que cada elemento representa o valor de uma coluna. Aqui está um exemplo:

```python
import csv

with open('dados.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)

    for linha in leitor:
        print(linha)
```

Nesse exemplo, o arquivo `dados.csv` é aberto em modo de leitura. Em seguida, um objeto `csv.reader` é criado passando o arquivo como argumento. O objeto `leitor` permite iterar sobre as linhas do arquivo.

Cada linha é retornada como uma lista de strings. Você pode acessar os valores individuais de cada coluna usando a indexação da lista. Por exemplo, `linha[0]` retorna o valor da primeira coluna, `linha[1]` retorna o valor da segunda coluna e assim por diante.

### `csv.DictReader`

A classe `csv.DictReader` é usada para ler arquivos CSV e retorna os valores como dicionários. Cada linha do arquivo CSV é retornada como um dicionário, em que as chaves são os nomes das colunas e os valores são os valores correspondentes. Aqui está um exemplo:

```python
import csv

with open('dados.csv', 'r') as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)

    for linha in leitor:
        print(linha)
```

Nesse exemplo, o arquivo `dados.csv` é aberto em modo de leitura. Um objeto `csv.DictReader` é criado passando o arquivo como argumento. O objeto `leitor` permite iterar sobre as linhas do arquivo.

Cada linha é retornada como um dicionário, em que as chaves são os nomes das colunas definidos na primeira linha (cabeçalho) do arquivo CSV e os valores são os valores correspondentes de cada coluna.

Você pode acessar os valores individuais de cada coluna usando a notação de dicionário. Por exemplo, `linha['nome']` retorna o valor da coluna "nome", `linha['idade']` retorna o valor da coluna "idade" e assim por diante.
