# Introdução ao método __init__ (inicializador de atributos)

Em classes no Python, existe uma palavra reservada chamada `self`. Ela é responsável por fazer referência à instância atual da classe. Desse modo, ao colocar o `self` como parâmetro de uma função, ela se torna um método da classe e esse parâmetro é gerenciado pelo Python.

Além disso, existe o dunder `__init__` que é uma das funções que são executadas no momento da criação de um novo objeto. Nos parâmetros, após o self, você pode colocar os nomes dos atributos presentes na classe que serão inseridos quando for instanciar uma nova classe. No corpo dessa função, você declara os atributos da classe e os inicializa com base nos valores passados como argumento de `__init()__` da seguinte forma:

```python
class Pessoa:
  def __init__(self, nome, sobrenome):
      self.nome = nome
      self.sobrenome = sobrenome

p1 = Pessoa("Luiz", "Otávio")
```

Essa forma é muito mais conveniente para definir as propriedades de uma classe. Um exemplo equivalente ao anterior, porém sem utilizar o dunder `__init__()`seria da seguinte forma:

```python
class Pessoa:
  ...

p1 = Pessoa()
p1.nome = "Luiz"
p1.sobrenome = "Otávio"
```

O `self` no primeiro exemplo exerce o mesmo papel de `p1`, pois ambos exercem a função de fazer referência a instância da classe `Pessoa` o qual permite manipular seus atributos da forma que quiser.