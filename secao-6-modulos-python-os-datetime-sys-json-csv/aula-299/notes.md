# Variáveis de ambiente com os.getenv, os.environ e python-dotenv

Variáveis de ambiente são valores que podem ser definidos no sistema operacional ou em um contexto de execução específico e que podem ser acessados por um programa. Elas são úteis para armazenar informações sensíveis ou configurações que podem variar dependendo do ambiente em que o programa está sendo executado, como chaves de API, credenciais de banco de dados, diretórios de arquivos, etc.

No Python, existem algumas maneiras de acessar e configurar variáveis de ambiente. Duas bibliotecas comumente usadas para lidar com variáveis de ambiente são `os` e `python-dotenv`. A biblioteca `os` fornece acesso a várias funcionalidades do sistema operacional, incluindo variáveis de ambiente, enquanto `python-dotenv` é uma biblioteca que permite carregar variáveis de ambiente a partir de arquivos `.env`.

A função `os.getenv()` é usada para acessar o valor de uma variável de ambiente específica. Ela recebe o nome da variável de ambiente como argumento e retorna o valor correspondente se a variável existir ou `None` caso contrário. Aqui está um exemplo de uso:

```python
import os

# Obtendo o valor da variável de ambiente "API_KEY"
api_key = os.getenv("API_KEY")

if api_key:
    # Usando a API key
    print("API key:", api_key)
else:
    print("A variável de ambiente API_KEY não está definida.")
```

Agora, em relação à biblioteca `python-dotenv`, ela permite carregar variáveis de ambiente de um arquivo `.env` localizado no diretório do seu projeto. Essa biblioteca é útil quando você não deseja definir as variáveis de ambiente diretamente no sistema operacional, mas sim em um arquivo separado. Para usar o `python-dotenv`, você precisa instalá-lo primeiro usando o gerenciador de pacotes `pip`.

Aqui está um exemplo de como usar o `python-dotenv`:

1. Instale a biblioteca:

   ```bash
   pip install python-dotenv
   ```

2. Crie um arquivo chamado `.env` no diretório do seu projeto e adicione as variáveis de ambiente nele. Por exemplo:

   ```
   API_KEY=my-api-key
   DATABASE_URL=postgresql://username:password@localhost/dbname
   ```

3. No seu código Python, carregue as variáveis de ambiente do arquivo `.env` usando `python-dotenv` e acesse-as com `os.getenv()`:

   ```python
   import os
   from dotenv import load_dotenv

   # Carregando as variáveis de ambiente do arquivo .env
   load_dotenv()

   # Obtendo o valor da variável de ambiente "API_KEY"
   api_key = os.getenv("API_KEY")

   if api_key:
       # Usando a API key
       print("API key:", api_key)
   else:
       print("A variável de ambiente API_KEY não está definida.")
   ```

Dessa forma, você pode armazenar suas configurações em um arquivo `.env` separado e carregá-las facilmente usando o `python-dotenv`, mantendo as informações sensíveis fora do código-fonte e permitindo que o mesmo código seja executado em diferentes ambientes sem alterações.
