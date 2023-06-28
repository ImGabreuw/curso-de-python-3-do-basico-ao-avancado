# Escopo da classe e de métodos da classe

O escopo de uma classe em Python se refere à visibilidade e acessibilidade dos atributos e métodos definidos dentro dela. Em outras palavras, o escopo determina onde os atributos e métodos podem ser usados e acessados dentro e fora da classe.

Os atributos e métodos definidos dentro de uma classe têm escopo de classe. Isso significa que eles são acessíveis dentro de outros métodos da mesma classe, utilizando a palavra reservada `self` para referenciar o objeto atual. Além disso, esses atributos e métodos também podem ser acessados por meio de objetos da classe fora da própria classe.

Vamos criar um exemplo com a classe "Animal" para ilustrar o escopo de classe e método:

```python
class Animal:
    # Atributo de classe
    especie = "Desconhecido"

    def __init__(self, nome):
        # Atributo de instância
        self.nome = nome

    def emitir_som(self):
        # Variável local do método
        som = "..."
        print(f"{self.nome} faz {som}")

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
```

Nesse exemplo, temos a classe "Animal" com três elementos: o atributo de classe `especie`, o método `__init__` (construtor) e os métodos `emitir_som` e `exibir_informacoes`.

O atributo `especie` é um atributo de classe, pois é definido diretamente na classe "Animal". Ele é compartilhado por todos os objetos da classe e pode ser acessado utilizando a sintaxe `nome_da_classe.nome_do_atributo` ou `self.nome_do_atributo` dentro dos métodos da classe. Ele pode ser usado para definir uma espécie padrão para todos os animais ou para compartilhar informações comuns entre eles.

O método `__init__` é o construtor da classe, responsável por inicializar o objeto e definir seus atributos. O atributo `nome` é um atributo de instância, pois é definido dentro do método `__init__` utilizando a notação `self.nome`. Cada objeto da classe "Animal" terá seu próprio valor para o atributo `nome`.

O método `emitir_som` demonstra uma variável local do método chamada `som`. Essa variável só existe dentro do método e não é acessível fora dele. É comum que métodos tenham variáveis locais para armazenar valores temporários ou intermediários.

O método `exibir_informacoes` utiliza tanto o atributo de instância `nome` quanto o atributo de classe `especie`. Ambos são acessados usando a notação `self.nome_do_atributo`. Isso permite que cada objeto da classe "Animal" tenha seu próprio nome, mas compartilhe a mesma espécie.

Agora, vamos criar objetos da classe "Animal" e chamar seus métodos:

```python
animal1 = Animal("Rex")
animal1.emitir_som()
animal1.exibir_informacoes()

animal2 = Animal("Mittens")
animal2.emitir_som()
animal2.exibir_informacoes()
```

Nesse exemplo, criamos dois objetos, `animal1` e `animal2`, da classe "Animal" com nomes diferentes. Chamamos o método `emitir_som` para cada objeto

, que exibirá o som do animal (nesse caso, apenas três pontos). Em seguida, chamamos o método `exibir_informacoes` para exibir as informações do animal, incluindo o nome e a espécie (que é um atributo de classe).

A saída esperada será:

```
Rex faz ...
Nome: Rex
Espécie: Desconhecido
Mittens faz ...
Nome: Mittens
Espécie: Desconhecido
```

Nesse exemplo, podemos ver que o atributo de classe `especie` é compartilhado por todos os objetos da classe "Animal", enquanto o atributo de instância `nome` é específico para cada objeto. Os métodos têm acesso aos atributos da classe e do objeto usando a palavra reservada `self`.
