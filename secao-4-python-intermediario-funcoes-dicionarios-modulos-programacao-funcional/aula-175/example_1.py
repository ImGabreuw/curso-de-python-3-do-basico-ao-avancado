from itertools import groupby

alunos = ["a", "a", "a", "b", "c", "a"]
grupos = groupby(alunos)

for chave, grupo in grupos:
  print("Grupo:", chave)
  print(list(grupo))