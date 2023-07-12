# (parte 1) Web Scraping com Python usando requests e bs4 BeautifulSoup

Web scraping é o processo de extrair informações de páginas da web de forma automatizada. O Python oferece várias bibliotecas úteis para realizar web scraping, como o pacote `requests` para fazer solicitações HTTP e o pacote `BeautifulSoup` (bs4) para analisar e extrair dados do HTML.

Para começar a raspagem de dados, você precisa primeiro instalar as bibliotecas `requests` e `BeautifulSoup`. Você pode fazer isso usando o gerenciador de pacotes `pip` através do seguinte comando:

```
pip install bs4 requests types-requests
```

Aqui está um exemplo de como realizar web scraping com Python usando as bibliotecas `requests` e `BeautifulSoup`:

1. Importando as bibliotecas:

   Comece importando os módulos `requests` e `BeautifulSoup` no seu script Python:

   ```python
   import requests
   from bs4 import BeautifulSoup
   ```

2. Fazendo uma solicitação HTTP:

   Use o `requests` para fazer uma solicitação HTTP para a página web da qual você deseja extrair dados. Por exemplo, vamos fazer uma solicitação GET para a página de notícias do site "https://www.example.com":

   ```python
   url = "https://www.example.com"
   response = requests.get(url)
   ```

3. Analisando o HTML com o BeautifulSoup:

   O próximo passo é analisar o HTML retornado pelo `requests` usando o `BeautifulSoup`. Isso permitirá que você pesquise e extraia os dados desejados. Crie um objeto `BeautifulSoup` passando o conteúdo HTML e o parser desejado:

   ```python
   raw_html = response.text
   parsed_html = BeautifulSoup(raw_html, 'html.parser')
   ```

4. Navegando e extraindo dados:

   Agora você pode navegar pela estrutura HTML usando os métodos e propriedades fornecidos pelo `BeautifulSoup` e extrair os dados necessários. Por exemplo, vamos extrair todos os títulos de notícias da página:

   ```python
   headlines = parsed_html.find_all('h2', class_='news-title')
   
   for headline in headlines:
       print(headline.text)
   ```

   Neste exemplo, estamos usando o método `find_all()` do `BeautifulSoup` para encontrar todos os elementos `<h2>` com a classe CSS "news-title". Em seguida, percorremos cada elemento encontrado e imprimimos o texto do título da notícia.

   Você pode usar uma variedade de métodos do `BeautifulSoup`, como `find()`, `find_all()`, `select()`, entre outros, para navegar e extrair os dados conforme necessário, dependendo da estrutura HTML da página.

É importante ressaltar que ao realizar web scraping, você deve verificar se está em conformidade com as políticas do site que está acessando. Além disso, algumas páginas podem ter medidas de segurança para evitar web scraping, como captchas ou bloqueio de IP, portanto, é importante ter isso em mente ao desenvolver seu script de web scraping.

Essas são apenas as etapas básicas para realizar web scraping usando Python com as bibliotecas `requests` e `BeautifulSoup`. Existem muitos recursos e técnicas avançadas disponíveis para tornar seu web scraping mais robusto e eficiente. Recomendo explorar a documentação oficial do `requests` (https://docs.python-requests.org/) e do `BeautifulSoup` (https://www.crummy.com/software/BeautifulSoup/bs4/doc/) para obter mais informações e aprofundar seus conhecimentos.
