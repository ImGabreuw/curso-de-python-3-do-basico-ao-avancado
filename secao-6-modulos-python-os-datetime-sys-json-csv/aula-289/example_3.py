import json

dados = {
    "nome": "João",
    "idade": 30,
    "casado": True,
    "filhos": ["Maria", "Pedro"],
    "endereco": {
        "rua": "Rua Principal",
        "cidade": "São Paulo",
        "estado": "SP"
    }
}

json_string = json.dumps(dados, ensure_ascii=False, indent=4)
print(json_string)