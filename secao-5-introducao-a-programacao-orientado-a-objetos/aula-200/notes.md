# Métodos em instâncias de classes Python

Métodos em classes são funções definidas dentro de uma classe que podem ser chamadas para executar ações específicas ou manipular os dados dos objetos da classe. Esses métodos são semelhantes às funções regulares, mas estão associados a uma classe específica e podem acessar os atributos e outros métodos da classe por meio da palavra-chave `self`.

Vamos criar um exemplo da classe `Carro` em Python para ilustrar o uso de métodos:

```python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    
    def acelerar(self, incremento):
        self.velocidade += incremento
    
    def frear(self, decremento):
        if self.velocidade >= decremento:
            self.velocidade -= decremento
        else:
            self.velocidade = 0
    
    def exibirInformacoes(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)
        print("Velocidade:", self.velocidade, "km/h")
```

Nesse exemplo, a classe `Carro` possui quatro atributos: marca, modelo, ano e velocidade. Ela também possui três métodos: `acelerar`, `frear` e `exibirInformacoes`.

O método `acelerar` recebe um valor de incremento e aumenta a velocidade do carro em função desse incremento. O método `frear` recebe um valor de decremento e diminui a velocidade do carro em função desse decremento, garantindo que a velocidade não seja negativa.

O método `exibirInformacoes` exibe as informações do carro na tela, incluindo a marca, o modelo, o ano e a velocidade atual.

Agora, vamos criar um objeto da classe `Carro` e chamar seus métodos:

```python
carro1 = Carro("Toyota", "Corolla", 2022)
carro1.exibirInformacoes()
carro1.acelerar(50)
carro1.exibirInformacoes()
carro1.frear(20)
carro1.exibirInformacoes()
```

Nesse caso, criamos um objeto chamado `carro1` da classe `Carro` e definimos seus atributos. Em seguida, chamamos o método "exibirInformacoes" para mostrar os detalhes do carro na tela. Em seguida, chamamos o método `acelerar` para aumentar a velocidade do carro em 50 km/h e novamente chamamos o método `exibirInformacoes` para verificar a nova velocidade. Por fim, chamamos o método `frear` para diminuir a velocidade do carro em 20 km/h e exibimos novamente as informações do carro.

A saída esperada será:

```
Marca: Toyota
Modelo: Corolla
Ano: 2022
Velocidade: 0 km/h

Marca: Toyota
Modelo: Corolla
Ano: 2022
Velocidade: 50 km/h

Marca: Toyota
Modelo: Corolla
Ano: 2022
Velocidade: 30 km/h
```