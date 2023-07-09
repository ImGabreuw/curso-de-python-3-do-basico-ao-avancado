# CSV (Comma Separated Values - Valores separados por vírgulas)

O formato CSV (Comma-Separated Values) é um formato de arquivo amplamente usado para armazenar dados tabulares em forma de texto simples. Como o nome sugere, os valores são separados por vírgulas, embora também seja comum usar outros caracteres como separadores, como ponto e vírgula (`,`) ou tabulação (`\t`).

No formato CSV, os dados são organizados em linhas e colunas, onde cada linha representa um registro ou uma entrada de dados, e cada coluna representa um campo ou um atributo dos dados.

Aqui está um exemplo de um arquivo CSV com dados de funcionários:

```
nome,idade,cargo
João,30,Analista
Maria,28,Desenvolvedora
Carlos,35,Gerente
```

Nesse exemplo, a primeira linha é chamada de linha de cabeçalho, onde os nomes das colunas são especificados. Nas linhas subsequentes, temos os dados dos funcionários separados por vírgulas.

O formato CSV é amplamente utilizado devido à sua simplicidade e compatibilidade com várias aplicações e programas. É comumente utilizado para importar e exportar dados entre diferentes sistemas e para compartilhar dados em formato de tabela. 

No entanto, o formato CSV tem algumas limitações. Por exemplo, não há um padrão estrito para representar tipos de dados, então todos os valores são tratados como texto. Além disso, se um valor contiver uma vírgula, aspas ou caracteres especiais, pode ser necessário usar aspas ou escapar os caracteres para evitar ambiguidades na leitura dos dados.

Regras básicas do formato CSV:

1. Delimitador: Os valores em cada linha são separados por um caractere delimitador, geralmente uma vírgula (`,`), ponto e vírgula (`;`) ou tabulação (`\t`).

2. Quebra de linha: Cada linha representa um registro de dados e é geralmente terminada por uma quebra de linha. A quebra de linha pode ser representada por um caractere específico, como a sequência `\n` ou o caractere de nova linha.

3. Citação de campos: Os campos podem ser envoltos em aspas (") quando contêm o caractere delimitador ou a quebra de linha. Isso permite que valores com caracteres especiais sejam corretamente interpretados. Por exemplo:

   ```
   nome,idade,cidade
   "João",30,"São Paulo"
   "Maria",25,"Rio de Janeiro"
   ```

4. Cabeçalho opcional: A primeira linha do arquivo CSV geralmente contém o cabeçalho, que descreve os nomes das colunas. No entanto, o cabeçalho é opcional e alguns arquivos CSV podem não tê-lo.

5. Valores vazios: Os campos podem estar vazios, o que é representado por dois caracteres delimitadores consecutivos. Por exemplo:

   ```
   nome,idade,cidade
   "João",, "São Paulo"
   ```

6. Caracteres especiais: Se um campo contiver o caractere delimitador, a quebra de linha ou as aspas, esses caracteres devem ser devidamente escapados para evitar ambiguidades. Geralmente, eles são duplicados ou precedidos por um caractere de escape, como aspas duplas. Por exemplo:

   ```
   nome,frase
   "João", "Ele disse: ""Olá!"""
   ```

Essas são algumas das regras básicas do formato CSV. É importante observar que, embora seja um formato amplamente utilizado, a falta de um padrão formal pode levar a variações na interpretação do formato em diferentes aplicativos e implementações.

O Python fornece a biblioteca padrão `csv` que facilita a leitura e gravação de arquivos CSV, lidando automaticamente com a maioria das regras mencionadas acima. Ela oferece recursos para processar dados CSV de forma eficiente, tornando mais fácil a manipulação desse tipo de arquivo no Python.
