# (Parte 1) super e a sobreposição de membros em Python Orientado a Objetos

Em programação orientada a objetos, a função `super()` é usada para chamar um método da classe pai na classe filha. Ela permite acessar e executar métodos da classe pai, mesmo quando a classe filha substituiu ou sobrescreveu esses métodos.

Quando uma classe filha herda de uma classe pai, é comum que a classe filha queira adicionar ou modificar o comportamento dos métodos herdados da classe pai. No entanto, às vezes, é necessário executar o código do método da classe pai antes ou depois da modificação feita na classe filha. É aí que o `super()` se torna útil.

A chamada `super().nomedometodo()` dentro da classe filha permite chamar o método com o mesmo nome na classe pai. Dessa forma, é possível executar o código da classe pai e, em seguida, adicionar ou modificar o comportamento específico da classe filha.

Aqui está um exemplo que ilustra o uso de `super()` para chamar um método da classe pai e sobrepor membros:

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def saudacao(self):
        return f"Olá, meu nome é {self.nome}."


class Cliente(Pessoa):
    def __init__(self, nome, numero_cliente):
        super().__init__(nome)
        self.numero_cliente = numero_cliente
    
    def saudacao(self):
        # Chama o método saudacao() da classe pai usando super()
        mensagem_pai = super().saudacao()
        return f"{mensagem_pai} Sou um cliente com número {self.numero_cliente}."


pessoa = Pessoa("João")
print(pessoa.saudacao())  # Saída: Olá, meu nome é João.

cliente = Cliente("Maria", "12345")
print(cliente.saudacao())  # Saída: Olá, meu nome é Maria. Sou um cliente com número 12345.
```

Nesse exemplo, temos as classes `Pessoa` e `Cliente`. A classe `Cliente` herda da classe `Pessoa` e adiciona um atributo `numero_cliente`. A classe `Cliente` também sobrescreve o método `saudacao()`, mas ainda quer aproveitar a saudação da classe `Pessoa`.

Usando `super().__init__(nome)` no método `__init__()` da classe `Cliente`, o código da classe pai `Pessoa` é executado para inicializar o atributo `nome`. Em seguida, a classe `Cliente` adiciona o atributo `numero_cliente`.

No método `saudacao()` da classe `Cliente`, é chamado o método `saudacao()` da classe `Pessoa` usando `super().saudacao()`. O resultado é armazenado na variável `mensagem_pai`, permitindo que a classe `Cliente` adicione a mensagem específica para o cliente.

Dessa forma, a chamada `super()` permite acessar e usar membros e métodos da classe pai, facilitando a reutilização de código e a extensão de comportamentos nas classes filhas.