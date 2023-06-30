# Herança Simples - Python Orientado a Objetos

A herança é um conceito fundamental da programação orientada a objetos que permite criar classes que herdam características e comportamentos de outras classes. Em Python, você pode implementar a herança simples, na qual uma classe filha herda atributos e métodos de uma única classe pai.

A sintaxe básica para definir uma classe que herda de outra classe em Python é a seguinte:

```python
class ClassePai:
    # Definição da classe pai

class ClasseFilha(ClassePai):
    # Definição da classe filha
```

Na declaração da classe filha, você coloca o nome da classe pai entre parênteses após o nome da classe filha, indicando que a classe filha está herdando da classe pai. Isso faz com que a classe filha tenha acesso a todos os atributos e métodos da classe pai.

Vamos considerar o exemplo de duas classes: Pessoa e Cliente. A classe Pessoa pode ter atributos como nome, idade e endereço, juntamente com métodos relacionados à pessoa, como definir nome, obter idade, etc. A classe Cliente é uma classe derivada (ou filha) da classe Pessoa, ou seja, Cliente herda os atributos e métodos da classe Pessoa.

Aqui está um exemplo que ilustra essa herança:

```python
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
```

Neste exemplo, a classe Pessoa é a classe pai e a classe Cliente é a classe filha.

Agora podemos criar instâncias das classes Pessoa e Cliente e acessar seus atributos e métodos:

```python
pessoa = Pessoa("João", 25, "Rua A")
print(pessoa.obter_nome())  # Saída: João
print(pessoa.obter_idade())  # Saída: 25
print(pessoa.obter_endereco())  # Saída: Rua A

cliente = Cliente("Maria", 30, "Rua B")
print(cliente.obter_nome())  # Saída: Maria (herdado da classe Pessoa)
print(cliente.obter_idade())  # Saída: 30 (herdado da classe Pessoa)
print(cliente.obter_endereco())  # Saída: Rua B (herdado da classe Pessoa)
```

Neste exemplo, a classe Cliente herda os métodos `obter_nome()`, `obter_idade()` e `obter_endereco()` da classe Pessoa.

> ## **Method Resolution Order (MRO)**

O Method Resolution Order (MRO) é o algoritmo utilizado em Python para determinar a ordem em que as classes são pesquisadas quando um método é chamado em uma hierarquia de classes. A MRO define a prioridade de resolução dos métodos em uma classe derivada quando existem métodos com o mesmo nome nas classes pai.

No exemplo anterior, temos a classe Pessoa como classe pai e a classe Cliente como classe filha. Quando um método é chamado em um objeto da classe Cliente, o Python verifica a MRO para determinar a ordem de pesquisa do método nas classes envolvidas.

Em Python, a MRO segue o algoritmo C3 Linearization, que garante a consistência da ordem de resolução dos métodos em todas as situações. Nesse algoritmo, a ordem de pesquisa começa pela própria classe e, em seguida, percorre a hierarquia de herança de forma apropriada.

Vamos examinar o exemplo anterior e considerar como a MRO seria aplicada a ele:

```python
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
```

No caso acima, a ordem de resolução dos métodos segue a sequência `Cliente` -> `Pessoa` -> `object`. Isso significa que, se um método for chamado em um objeto da classe Cliente, o Python procurará primeiro na própria classe Cliente, depois na classe Pessoa e, por fim, na classe base `object` (que é a classe mãe de todas as classes em Python).

Vamos considerar um exemplo que demonstre a MRO e a resolução de métodos:

```python
cliente = Cliente("Maria", 30, "Rua B")
print(cliente.obter_nome())  # Saída: Maria
```

Nesse exemplo, quando o método `obter_nome()` é chamado em `cliente`, o Python verifica a classe Cliente. Como o método não é encontrado nessa classe, a pesquisa continua na classe Pai, que é a classe Pessoa. O método é encontrado nessa classe e é executado, retornando o nome "Maria".

Você pode visualizar o MRO a partir da função `help()` que mostra todas as informações de um objeto. Veja o exemplo abaixo:

```python
cliente = Cliente("Maria", 30, "Rua B")

help(cliente)
```

A seguir a saída da função `help()`

```
Help on Cliente in module __main__ object:

class Cliente(Pessoa)
 |  Cliente(nome, idade, endereco)
 |  
 |  Method resolution order:
 |      Cliente
 |      Pessoa
 |      builtins.object
 |  
 |  Methods inherited from Pessoa:
 |  
 |  __init__(self, nome, idade, endereco)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  obter_endereco(self)
 |  
 |  obter_idade(self)
 |  
 |  obter_nome(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Pessoa:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
```

A MRO garante que a resolução de métodos ocorra de maneira consistente e previsível em hierarquias de classes mais complexas, mesmo quando várias classes pai e heranças múltiplas estão envolvidas. O algoritmo C3 Linearization é responsável por definir a ordem correta de resolução dos métodos com base na hierarquia de herança definida.