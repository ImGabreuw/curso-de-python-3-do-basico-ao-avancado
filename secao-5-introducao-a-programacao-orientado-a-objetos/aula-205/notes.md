# `__dict__` e vars para atributos de instância

Em Python, os atributos de instância de um objeto podem ser acessados e modificadas usando o atributo especial `__dict__` ou a função embutida `vars()`. Ambas as abordagens permitem obter um dicionário contendo os atributos e seus respectivos valores para um objeto específico.

O atributo especial `__dict__` é um dicionário que contém todos os atributos de instância e seus valores para um objeto. Cada chave no dicionário é o nome do atributo e o valor correspondente é o valor atual desse atributo. É possível acessar e modificar os atributos diretamente através do dicionário `__dict__`.

A função embutida `vars(objeto)` retorna o mesmo dicionário `__dict__` para o objeto fornecido como argumento. Ela é uma forma mais conveniente de acessar o dicionário de atributos de instância.

Vamos criar um exemplo com a classe "Pessoa" para ilustrar o uso de `__dict__` e `vars()`:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        print("Informações da pessoa:")
        print(self.__dict__)

p1 = Pessoa("Alice", 25)
p2 = Pessoa("Bob", 30)

p1.exibir_informacoes()
print(vars(p2))
```

Nesse exemplo, a classe "Pessoa" tem dois atributos de instância: `nome` e `idade`.

No método `__init__`, esses atributos são inicializados com os valores passados como argumentos.

O método `exibir_informacoes` imprime o dicionário `__dict__` do objeto, que contém todos os atributos de instância e seus respectivos valores.

Criamos dois objetos, `p1` e `p2`, da classe "Pessoa" com diferentes valores para os atributos `nome` e `idade`. Em seguida, chamamos o método `exibir_informacoes` para `p1` e utilizamos a função `vars(p2)` para exibir o dicionário de atributos de instância de `p2`.

A saída esperada será:

```
Informações da pessoa:
{'nome': 'Alice', 'idade': 25}
{'nome': 'Bob', 'idade': 30}
```

Podemos ver que tanto o acesso direto ao atributo especial `__dict__` quanto o uso da função `vars()` nos fornecem os mesmos dicionários contendo os atributos e seus valores para os objetos `p1` e `p2`.

Essas abordagens podem ser úteis para inspecionar os atributos de instância de um objeto dinamicamente, especialmente quando o número de atributos é desconhecido ou pode variar. Além disso, você também pode usar esses dicionários para modificar os valores dos atributos de instância de forma dinâmica, se necessário.

### **Observação**

O dunder **dict** ou a função `vars()` é muito útil para a serialização de objetos em JSON, veja o exemplo abaixo:

```python
import json

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

p1 = Pessoa("Luiz", 35)

with open("dados.json", "w", encoding="utf8") as arquivo:
  json.dump(vars(p1), arquivo)
```

Conteúdo do arquivo `dados.json`:

```json
{ "nome": "Luiz", "idade": 35 }
```

Já para deserializar os dados de um objeto, basta utilizar o desempacotador de dicionários (`**`):

```python

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

dados = { "nome": "Luiz", "idade": 35 }

p1 = Pessoa(**dados)

print(p1.nome, p1.idade) # Saída: Luiz 35
```