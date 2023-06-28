import json

CAMINHO_ARQUIVO = './secao-5-introducao-a-programacao-orientado-a-objetos/aula-207/dados.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]


def save_data():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


def load_data():
    with open(CAMINHO_ARQUIVO, 'r') as arquivo:
        pessoas = json.load(arquivo)
        p1 = Pessoa(**pessoas[0])
        p2 = Pessoa(**pessoas[1])
        p3 = Pessoa(**pessoas[2])

        print(p1.nome, p1.idade)
        print(p2.nome, p2.idade)
        print(p3.nome, p3.idade)


if __name__ == '__main__':
    save_data()
    load_data()
