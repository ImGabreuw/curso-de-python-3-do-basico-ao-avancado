# Atributos de classe

Em Python, os atributos de classe são variáveis que pertencem à classe como um todo, em vez de pertencerem a instâncias individuais da classe. Esses atributos são compartilhados por todas as instâncias da classe e podem ser acessados usando a sintaxe `nome_da_classe.nome_do_atributo`.

Os atributos de classe são definidos diretamente dentro da classe, fora de qualquer método. Eles são comumente usados para armazenar informações que são compartilhadas entre todas as instâncias da classe, como configurações globais, constantes ou valores padrão.

Vamos criar um exemplo com a classe "Cachorro" para ilustrar os atributos de classe em Python:

```python
class Cachorro:
    especie = "Canis lupus familiaris"
    contador = 0
    
    def __init__(self, nome):
        self.nome = nome
        Cachorro.contador += 1
    
    def latir(self):
        print("Au au!")
    
    def exibir_informacoes(self):
        print("Nome:", self.nome)
        print("Espécie:", Cachorro.especie)
        print("Quantidade de cachorros:", Cachorro.contador)
```

Nesse exemplo, a classe "Cachorro" possui dois atributos de classe: `especie` e `contador`.

O atributo `especie` é uma variável que armazena a espécie comum de todos os cachorros. Ele é definido diretamente na classe e pode ser acessado usando a sintaxe `Cachorro.especie` dentro dos métodos da classe ou por meio de objetos da classe.

O atributo `contador` é uma variável que mantém o número total de instâncias criadas da classe "Cachorro". Ele é inicializado como zero e é incrementado no construtor da classe (`__init__`) sempre que um novo objeto da classe é criado. Assim como o atributo `especie`, o `contador` também pode ser acessado usando a sintaxe `Cachorro.contador` dentro dos métodos da classe ou por meio de objetos da classe.

O método `__init__` é o construtor da classe, e ele é responsável por inicializar o atributo `nome` de cada objeto da classe. Além disso, ele incrementa o contador de cachorros toda vez que um novo cachorro é criado.

O método `latir` é responsável por exibir o som característico de um cachorro.

O método `exibir_informacoes` exibe o nome, a espécie e a quantidade de cachorros criados até o momento. Nesse método, tanto o atributo de instância `nome` quanto o atributo de classe `especie` e `contador` são acessados.

Agora, vamos criar objetos da classe "Cachorro" e chamar seus métodos:

```python
cachorro1 = Cachorro("Max")
cachorro2 = Cachorro("Bella")

cachorro1.exibir_informacoes()
cachorro2.exibir_informacoes()
```

Nesse exemplo, criamos dois objetos, `cachorro1` e `cachorro2`, da classe "Cachorro" com nomes diferentes. Em seguida, chamamos o método `exibir_informacoes` para cada objeto.

A saída esperada será:

```
Nome: Max
Espécie: Canis lupus familiaris
Quantidade de cach

orros: 2
Nome: Bella
Espécie: Canis lupus familiaris
Quantidade de cachorros: 2
```

Nesse exemplo, podemos ver que o atributo de classe `especie` é compartilhado por todas as instâncias da classe "Cachorro", enquanto o atributo de instância `nome` é específico para cada objeto. O atributo de classe `contador` é usado para acompanhar o número total de cachorros criados até o momento.

Os atributos de classe são úteis para armazenar informações comuns a todos os objetos da classe, garantindo que essas informações sejam consistentes em todas as instâncias.