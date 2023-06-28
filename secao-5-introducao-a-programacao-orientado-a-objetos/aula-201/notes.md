# Entendendo self em classes Python

Em Python, a palavra reservada `self` é usada dentro de uma classe para referenciar o próprio objeto da classe. Ela é usada como o primeiro parâmetro em todos os métodos da classe, incluindo o método especial `__init__` (construtor) e outros métodos personalizados.

Ao definir um método em uma classe, o parâmetro `self` é usado para referenciar o objeto em si, permitindo que você acesse seus atributos e métodos. Quando um método é chamado em um objeto da classe, o Python automaticamente passa uma referência a esse objeto como o valor do parâmetro `self`, permitindo que o método interaja com os dados do objeto.

Veja o exemplo a seguir de como o Python faz isso:

```python
class Carro:
  def __init__(self, nome):
    self.nome = nome

  def acelerar(self):
    print(self.nome, "está acelerando...")

fusca = Carro("Fusca")
fusca.acelerar() # Saída: Fusca está acelerando...

# O que o Python faz de baixo dos panos
Carro.acelerar(fusca) # Saída: Fusca está acelerando...
```

Por exemplo, considere a seguinte classe "Carro":

```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
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
        print("Velocidade:", self.velocidade, "km/h")
```

Nesse exemplo, a classe "Carro" possui três atributos: `marca`, `modelo` e `velocidade`. Ela também possui três métodos: `acelerar`, `frear` e `exibirInformacoes`.

O método `__init__` é o construtor da classe, onde definimos os atributos `marca`, `modelo` e `velocidade`, e utilizamos o `self` para fazer referência ao próprio objeto sendo criado.

O método `acelerar` recebe um valor de incremento e adiciona esse valor à velocidade do carro, utilizando o `self` para acessar o atributo `velocidade` do objeto.

O método `frear` recebe um valor de decremento e diminui a velocidade do carro, verificando se a velocidade é maior ou igual ao decremento. Caso seja, diminui o decremento da velocidade, caso contrário, define a velocidade como zero.

O método `exibirInformacoes` exibe as informações do carro na tela, utilizando o `self` para acessar os atributos `marca`, `modelo` e `velocidade` do objeto.

Agora, vamos criar um objeto da classe "Carro" e chamar seus métodos:

```python
carro1 = Carro("Toyota", "Corolla")
carro1.exibirInformacoes()
carro1.acelerar(50)
carro1.exibirInformacoes()
carro1.frear(20)
carro1.exibirInformacoes()
```

Nesse exemplo, criamos um objeto chamado "carro1" da classe "Carro" e definimos os atributos `marca` como "Toyota" e `modelo` como "Corolla". Em seguida, chamamos o método `exibirInformacoes` para mostrar as informações do carro na tela. Em seguida, chamamos o método `acelerar` para aumentar a velocidade do carro em 50 km/h e chamamos novamente o método `exibirInformacoes` para verificar a nova velocidade. Por fim, chamamos o método `frear` para diminuir a velocidade do carro em 20 km/h e exibimos novamente as informações do carro.

A saída esperada será:

```
Marca: Toyota
Modelo: Corolla
Velocidade: 0 km/h
Marca: Toyota
Modelo: Corolla
Velocidade: 50 km/h
Marca: Toyota
Modelo: Corolla
Velocidade: 30 km/h
```

Nesse exemplo, a utilização do `self` permite que cada objeto da classe "Carro" mantenha seus próprios valores de atributos, permitindo o correto armazenamento e manipulação dos dados relacionados a cada carro específico.

Em resumo, a palavra reservada `self` em Python é usada para referenciar o objeto atual dentro de uma classe. Ela permite que você acesse os atributos e métodos do objeto e manipule seus dados de forma adequada. É uma convenção amplamente adotada em Python, embora o nome do parâmetro possa ser alterado (embora não seja recomendado) desde que seja o primeiro parâmetro em todos os métodos da classe.
