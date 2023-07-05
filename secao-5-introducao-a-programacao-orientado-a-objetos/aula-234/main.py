class MeuError(Exception):
  ...

class OutroError(Exception):
  ...

def levantar_excecao():
  raise MeuError("A mensagem de erro", "outra coisa")

try:
  levantar_excecao()
except MeuError as error:
  print(error.args)
  exception_ = OutroError("Relançando exceção")
  raise exception_ from error