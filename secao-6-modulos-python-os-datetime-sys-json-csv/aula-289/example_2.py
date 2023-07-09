import json
from typing import TypedDict

# Definindo um TypedDict para representar informações de uma pessoa
class Pessoa(TypedDict):
    nome: str
    idade: int
    casado: bool

# Criando um objeto Pessoa
pessoa = Pessoa(nome="João", idade=30, casado=True)

# Convertendo objeto Pessoa em string JSON
json_string = json.dumps(pessoa)
print(json_string)
# Saída: {"nome": "João", "idade": 30, "casado": true}

# Convertendo string JSON em objeto Pessoa
pessoa_de_json: Pessoa = json.loads(json_string)
print(pessoa_de_json)
# Saída: {'nome': 'João', 'idade': 30, 'casado': True}