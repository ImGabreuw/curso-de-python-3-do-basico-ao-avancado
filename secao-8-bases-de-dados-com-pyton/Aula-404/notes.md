# Usando python-dotenv e .env com pymysql.connect

A biblioteca `python-dotenv` é usada para carregar variáveis de ambiente a partir de um arquivo `.env` no ambiente Python. Combinado com o pacote `pymysql`, é possível utilizar o arquivo `.env` para armazenar as informações de conexão com o banco de dados MySQL, como host, usuário, senha e nome do banco de dados, e então utilizá-las na função `pymysql.connect()`.

Aqui está um exemplo de como usar o `python-dotenv` e o `pymysql` em conjunto:

1. Instale as dependências necessárias executando o seguinte comando no terminal:

   ```
   pip install python-dotenv pymysql types-pymysql
   ```

2. Crie um arquivo chamado `.env` no mesmo diretório do seu script Python e adicione as variáveis de ambiente para a conexão com o banco de dados. Por exemplo:

   ```properties
   DB_HOST=localhost
   DB_USER=usuario
   DB_PASSWORD=senha
   DB_NAME=base_de_dados
   ```

3. No seu script Python, importe as bibliotecas necessárias e utilize o `python-dotenv` para carregar as variáveis de ambiente do arquivo `.env`. Em seguida, utilize essas variáveis para estabelecer a conexão com o banco de dados utilizando o `pymysql`. Veja o exemplo abaixo:

   ```python
   import pymysql
   from dotenv import load_dotenv

   # Carrega as variáveis de ambiente do arquivo .env
   load_dotenv()

   # Obtém as informações de conexão do banco de dados a partir das variáveis de ambiente
   db_host = os.getenv("DB_HOST")
   db_user = os.getenv("DB_USER")
   db_password = os.getenv("DB_PASSWORD")
   db_name = os.getenv("DB_NAME")

   # Estabelece a conexão com o banco de dados MySQL
   connection = pymysql.connect(
       host=db_host,
       user=db_user,
       password=db_password,
       database=db_name
   )

   # Restante do código para interagir com o banco de dados...
   ```

   Neste exemplo, importamos as bibliotecas `pymysql` e `dotenv` e carregamos as variáveis de ambiente do arquivo `.env` utilizando a função `load_dotenv()`.

   Em seguida, utilizamos a função `os.getenv()` para obter os valores das variáveis de ambiente definidas no arquivo `.env` e atribuímos a essas variáveis locais.

   Finalmente, utilizamos as variáveis `db_host`, `db_user`, `db_password` e `db_name` para estabelecer a conexão com o banco de dados MySQL através da função `pymysql.connect()`. Essas variáveis conterão os valores definidos no arquivo `.env`.

   A partir desse ponto, você pode utilizar a conexão `connection` e executar comandos SQL, realizar consultas, atualizações ou qualquer outra interação com o banco de dados utilizando a biblioteca `pymysql`.

   > **IMPORTANTE**: Certifique-se de que o arquivo `.env` e o seu script Python estejam no mesmo diretório para que o `python-dotenv` consiga localizar e carregar corretamente as variáveis de ambiente.

Combinar o uso do `python-dotenv` e `pymysql` com o arquivo `.env` torna mais conveniente gerenciar as informações de conexão com o banco de dados em um ambiente de desenvolvimento, especialmente quando há várias configurações diferentes que podem variar dependendo do ambiente em que o código está sendo executado.
