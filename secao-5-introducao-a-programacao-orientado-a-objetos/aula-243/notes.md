# Funções decoradoras e decoradores com classes

O Python por server uma linguagem dinâmica possibilita o desenvolvedor realizar diversas abordagem a fim de facilitar a legibilidade do código, dentre elas podemos citar a utilizar de decoradores em classes para sobrescrever métodos, no caso _dunder method_, nas classes.

No exemplo abaixo, utilizaremos essa abordagem para adicionar uma implementação para o _dunder method_ `__repr__` na classe `Time`.

```python
def adiciona_repr(cls):
  def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f"{class_name}({class_dict})"
    return class_repr

  cls.__repr__ = meu_repr
  return cls

@adiciona_repr
class Time:
  def __init__(self, nome):
    self.nome = nome


time = Time("Brasil")
print(time) # Saída: Time({'nome': 'Brasil'})
```
