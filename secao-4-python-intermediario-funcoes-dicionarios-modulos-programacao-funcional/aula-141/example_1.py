pseudo_dict = [
  ("a", "valor a"),
  ("b", "valor b"),
  ("c", "valor c"),
]

dc = {
  chave: valor
  for chave, valor in pseudo_dict
}

print(dc)