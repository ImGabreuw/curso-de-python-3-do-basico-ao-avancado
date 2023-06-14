texto = "Luiz"
iterador = iter(texto)

while True:
  try:
    letra = next(iterador)
    print(letra)
  except StopIteration:
    break