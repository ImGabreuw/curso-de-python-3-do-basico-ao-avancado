class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def obter_nome(self):
        return self.nome
    
    def obter_idade(self):
        return self.idade
    
    def obter_endereco(self):
        return self.endereco


class Cliente(Pessoa):
  ...

cliente = Cliente("Maria", 30, "Rua B")

help(cliente)