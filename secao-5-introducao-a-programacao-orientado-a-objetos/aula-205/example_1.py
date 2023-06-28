import json

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

p1 = Pessoa("Luiz", 35)

with open("dados.json", "w", encoding="utf8") as arquivo:
  json.dump(vars(p1), arquivo)