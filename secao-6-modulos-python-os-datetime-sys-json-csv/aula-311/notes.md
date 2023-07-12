# requests para requisições HTTP com Python (entenda request e response)

O pacote `requests` é uma biblioteca popular em Python usada para fazer requisições HTTP. Ele fornece uma interface simples e elegante para enviar solicitações HTTP e receber respostas dos servidores.

Para começar a usar o `requests`, você precisa instalá-lo primeiro. Você pode fazer isso usando o gerenciador de pacotes `pip` através do seguinte comando:

```
pip install requests types-requests
```

> **OBS**: o módulo `types-requests` são as tipagens do módulo `requests`, logo só é necessário instalá-lo caso você tenha um linter de código configurado no seu editor.

Agora, vamos entender como funcionam as solicitações e respostas HTTP usando o `requests`:

1. Importando a biblioteca:

   Para começar, importe o módulo `requests` no seu script Python:

   ```python
   import requests
   ```

2. Fazendo uma solicitação GET:

   Para enviar uma solicitação GET a um servidor, use a função `get()` do `requests` e passe a URL do recurso que você deseja acessar como argumento:

   ```python
   response = requests.get('https://www.example.com')
   ```

   Isso enviará uma solicitação GET ao servidor em `https://www.example.com` e armazenará a resposta na variável `response`.

   > **OBS**: a porta padrão de servidores rodando HTTP é 80, já aqueles em HTTPs é 433. Por isso que ao acessar `https://www.google.com.br` não precisa especificar a porta, pois o navegador automaticamente define a porta 433.

3. Acessando a resposta:

   A resposta retornada pela solicitação HTTP contém várias informações. Aqui estão algumas das propriedades e métodos mais comuns que você pode usar:

   - `status_code`: Retorna o código de status da resposta HTTP (por exemplo, 200 para OK, 404 para Não encontrado).
   - `text`: Retorna o conteúdo da resposta como texto.
   - `json()`: Retorna o conteúdo da resposta como um objeto JSON, se aplicável.
   - `headers`: Retorna os cabeçalhos da resposta como um dicionário.

   ```python
   print(response.status_code)  # Imprime o código de status da resposta
   print(response.text)  # Imprime o conteúdo da resposta como texto
   print(response.json())  # Imprime o conteúdo da resposta como objeto JSON
   print(response.headers)  # Imprime os cabeçalhos da resposta
   ```

   Você pode usar essas propriedades e métodos para extrair as informações necessárias da resposta HTTP.

4. Enviando dados em uma solicitação POST:

   Além das solicitações GET, o `requests` também suporta outros métodos HTTP, como POST, PUT e DELETE. Para enviar dados em uma solicitação POST, você pode passar um dicionário contendo os dados no argumento `data`:

   ```python
   data = {'username': 'johndoe', 'password': 'secretpassword'}
   response = requests.post('https://www.example.com/login', data=data)
   ```

   Neste exemplo, estamos enviando um POST para `https://www.example.com/login` com os dados do usuário (nome de usuário e senha) no corpo da solicitação.

Esses são apenas exemplos básicos de como usar o `requests` para fazer solicitações HTTP e acessar as respostas. A biblioteca oferece muito mais funcionalidades, como suporte a autenticação, cabeçalhos personalizados, envio de arquivos, sessões persistentes e muito mais.
