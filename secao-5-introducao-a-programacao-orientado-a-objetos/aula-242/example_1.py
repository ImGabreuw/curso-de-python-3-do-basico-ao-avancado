from contextlib import contextmanager

@contextmanager
def arquivo_texto(caminho_arquivo, modo):
  arquivo = open(caminho_arquivo, modo, encoding="utf8")
  yield arquivo
  arquivo.close()

with arquivo_texto("meuarquivo.txt", "w") as arquivo:
  arquivo.write('Olá, mundo!', 123)