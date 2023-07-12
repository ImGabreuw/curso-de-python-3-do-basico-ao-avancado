# Adicionando "encoding" no BeautifulSoup 4 para evitar problemas com caracteres

Uma coisa comum de ocorrer quando trabalhamos com o `BeautifulSoup` é problemas com caracteres. Isso ocorre devido a uma falha na detecção do _encoding_.

> Para mais informações sobre codificação de caracteres, clique [aqui](https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/):

Caso queira mudar a codificação de caracteres, envie os bytes diretamente para o BeautifulSoup e passe o valor da codificação de caracteres no atributo "from_encoding". Exemplo (para `utf-8`):

```python
BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')
```

> **IMPORTANTE**: Perceba que foi utilizado response.content" ao invés de "response.text", pois assim é possível obter os bytes.

Aqui está um exemplo de definir o encoding para UTF-8:

```python
bytes_html = response.content
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')
```
