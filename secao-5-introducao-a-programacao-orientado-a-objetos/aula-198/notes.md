# class - Classes são moldes para criar novos objetos

Em programação, a classe é uma estrutura fundamental que permite definir objetos com características e comportamentos específicos. Uma classe serve como um modelo (molde) para criar objetos (ou instâncias) que possuem suas próprias propriedades e métodos.

A nomenclatura de classes segue o padrão _PascalCase_, por convenção, por exemplo:

```python
class Pessoa:
  ...
```

Além disso, para instanciar uma classe, ou seja, criar um objeto, utilize os parênteses `()` após o nome da classe.

```python
p1 = Pessoa()

print(isinstance(p1, Pessoa)) # Saída: True
```

Aqui está um exemplo simples de uma classe `Pessoa` em Python:

```python
class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def exibirInformacoes(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Cidade:", self.cidade)

    def fazerAniversario(self):
        self.idade += 1
        print("Feliz aniversário! Agora você tem", self.idade, "anos.")
```

Nesse exemplo, a classe `Pessoa` tem três atributos: nome, idade e cidade. Ela também possui dois métodos: `exibirInformacoes()`, que exibe os detalhes da pessoa na tela, e `fazerAniversario()`, que incrementa a idade da pessoa em 1 e exibe uma mensagem de feliz aniversário.

Agora, vamos criar um objeto da classe `Pessoa` e chamar seus métodos:

```python
pessoa1 = Pessoa("João", 25, "São Paulo")
pessoa1.exibirInformacoes()
pessoa1.fazerAniversario()
```

Nesse caso, criamos um objeto chamado `pessoa1` da classe `Pessoa` e definimos seus atributos. Em seguida, chamamos o método `exibirInformacoes()` para mostrar os detalhes da pessoa na tela. Por fim, chamamos o método `fazerAniversario()`, que atualiza a idade da pessoa e exibe a mensagem de feliz aniversário com a nova idade.

A saída esperada será:

```
Nome: João
Idade: 25
Cidade: São Paulo
Feliz aniversário! Agora você tem 26 anos.
```

