# Salvando dados Python em JSON com módulo json

O módulo `json` em Python é usado para trabalhar com dados JSON (JavaScript Object Notation). Ele fornece funções para serializar objetos Python em formato JSON e desserializar dados JSON em objetos Python. Isso é útil quando você precisa armazenar dados estruturados ou trocar informações com outros sistemas que suportam JSON.

Aqui está um exemplo básico de como usar o módulo `json` para gravar e ler dados em um arquivo:

```python
import json

# Dicionário com dados
dados = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Gravando os dados em um arquivo JSON
with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo)

# Lendo os dados de um arquivo JSON
with open("dados.json", "r") as arquivo:
    dados_lidos = json.load(arquivo)

# Exibindo os dados lidos
print(dados_lidos)
```

Neste exemplo, temos um dicionário `dados` contendo algumas informações. Usamos a função `json.dump()` para escrever esses dados em um arquivo JSON chamado "dados.json". Em seguida, usamos a função `json.load()` para ler os dados do arquivo JSON e armazená-los na variável `dados_lidos`. Por fim, imprimimos os dados lidos na saída.

O resultado impresso será:

```
{'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
```

O módulo `json` também fornece outras funções úteis, como `json.dumps()` e `json.loads()`, que permitem serializar e desserializar dados JSON em formato de string, em vez de usar arquivos. Isso é útil quando você precisa transmitir ou armazenar dados JSON em um formato diferente de arquivos.

```python
import json

# Dicionário com dados
dados = {
    "nome": "Maria",
    "idade": 25,
    "cidade": "Rio de Janeiro"
}

# Serializando os dados em uma string JSON
dados_json = json.dumps(dados)

# Exibindo a string JSON
print(dados_json)

# Desserializando a string JSON em um objeto Python
dados_objeto = json.loads(dados_json)

# Exibindo o objeto Python
print(dados_objeto)
```

Neste exemplo, usamos `json.dumps()` para serializar o dicionário `dados` em uma string JSON. Em seguida, usamos `json.loads()` para desserializar a string JSON e obter o objeto Python correspondente.

O resultado impresso será:

```
{"nome": "Maria", "idade": 25, "cidade": "Rio de Janeiro"}
{'nome': 'Maria', 'idade': 25, 'cidade': 'Rio de Janeiro'}
```

Esses são apenas exemplos básicos de como usar o módulo `json` em Python para trabalhar com arquivos JSON. O módulo `json` fornece uma variedade de recursos e opções para manipular dados JSON mais complexos e lidar com casos específicos, como personalização da serialização ou desserialização. Consulte a documentação oficial do Python para obter mais detalhes sobre o módulo `json`.
