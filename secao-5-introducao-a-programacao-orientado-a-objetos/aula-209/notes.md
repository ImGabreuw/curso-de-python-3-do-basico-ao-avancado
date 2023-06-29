# Métodos de classe (@classmethod) + factories methods (métodos fábrica)

Em Python, os métodos de classe são métodos que pertencem à classe em si, em vez de pertencerem a instâncias individuais da classe. Esses métodos são definidos usando o decorador `@classmethod`. 

A principal diferença entre um método de classe e um método de instância é que um método de classe recebe a própria classe como primeiro argumento, tradicionalmente chamado de `cls`, em vez da instância da classe, que é tradicionalmente chamada de `self`. Embora seja uma convenção, você pode usar qualquer nome para esses parâmetros.

Aqui está um exemplo de como definir um método de classe em Python:

```python
class MinhaClasse:
    contador = 0

    def __init__(self):
        MinhaClasse.contador += 1

    @classmethod
    def obter_contagem(cls):
        return cls.contador
```

Neste exemplo, a classe `MinhaClasse` possui um atributo de classe chamado `contador` que rastreia o número de instâncias criadas. O método `__init__` é o construtor da classe e é chamado sempre que uma nova instância da classe é criada. O método de classe `obter_contagem` retorna o valor atual do contador de instâncias.

Aqui está como você pode usar esses métodos:

```python
objeto1 = MinhaClasse()
objeto2 = MinhaClasse()
objeto3 = MinhaClasse()

print(MinhaClasse.obter_contagem())  # Saída: 3
```

Observe que o método `obter_contagem` é chamado na própria classe, em vez de em uma instância específica da classe. O método de classe tem acesso aos atributos da classe, permitindo que você realize operações relacionadas à classe em si, em vez de em instâncias individuais.

Os métodos de classe são úteis em várias situações, como para criar **métodos de fábrica** que retornam instâncias da classe, para fornecer comportamentos específicos da classe ou para realizar operações que envolvem a classe em geral. Veja o exemplo abaixo:

```python
class Pessoa:
  def __init__(self, nome_completo, idade):
    self.nome_completo = nome_completo
    self.idade = idade

  @classmethod
  def criar_pessoa(cls, nome, sobrenome, idade):
    nome_completo = nome + sobrenome

    return cls(
      nome_completo,
      idade
    )

p1 = Pessoa.criar_pessoa("Luiz", "Otávio", 35)
```

Observe que o método `criar_pessoa` é chamado diretamente pelo nome classe e não a a partir de uma instância. Geralmente os métodos de fábricas são úteis quando há uma regra de negócio específica na criação de instâncias de uma classe, como é possível ver no exemplo acima, no qual a propriedade `nome_completo` deve conter o nome e o sobrenome que são passados como argumento da método. 