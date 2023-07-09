import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'

lista_clientes = [
    ['Luiz Otávio', 'Av 1, 22'],
    ['João Silva', 'R. 2, "1"'],
    ['Maria Sol', 'Av B, 3A'],
]
with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    # nome_colunas = ['Nome', 'Endereço']
    escritor = csv.writer(arquivo)

    escritor.writerow(nome_colunas)

    for cliente in lista_clientes:
        escritor.writerow(cliente)