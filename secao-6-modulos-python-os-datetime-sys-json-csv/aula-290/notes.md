# json.dump e json.load com arquivos

O método `json.dump()` é usado para escrever um objeto Python em um arquivo no formato JSON, enquanto o método `json.load()` é usado para ler um arquivo JSON e convertê-lo em um objeto Python.

Aqui está um exemplo que utiliza `json.dump()` e `json.load()` com arquivos:

```python
import json

# Dados a serem escritos no arquivo
dados = {
    "nome": "João",
    "idade": 30,
    "casado": True
}

# Escrevendo dados em um arquivo JSON
with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo)

# Lendo dados de um arquivo JSON
with open("dados.json", "r") as arquivo:
    dados_lidos = json.load(arquivo)

print(dados_lidos)
```

Nesse exemplo, o objeto `dados` contém informações sobre uma pessoa. O método `json.dump()` é usado para escrever esses dados em um arquivo chamado "dados.json". O modo de abertura do arquivo é "w", que significa escrita.

Em seguida, o método `json.load()` é usado para ler os dados do arquivo JSON "dados.json" e convertê-los de volta para um objeto Python. O modo de abertura do arquivo é "r", que significa leitura.

Por fim, os dados lidos são impressos na saída. A saída seria:

```
{'nome': 'João', 'idade': 30, 'casado': True}
```

Assim, `json.dump()` permite escrever dados em um arquivo JSON, enquanto `json.load()` permite ler dados de um arquivo JSON e convertê-los de volta para um objeto Python. Esses métodos são úteis para armazenar e recuperar dados estruturados em formato JSON.
