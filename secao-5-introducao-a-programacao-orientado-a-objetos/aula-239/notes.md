# `__new__` e `__init__` em classes Python

O dunder method `__new__` é responsável por criar e retornar uma nova instância de uma classe. Desse modo, esse método recebe no parâmetro `cls` uma classe.

Já o método `__init__` tem a função de inicializar uma instância já criada previamente pelo método `__new__`. Por isso, ele recebe no parâmetro `self` essa instância.

> E ambos os métodos não retornam nada (`None`);

Por baixo dos panos, o Python executa os seguintes comandos:

```python
class A:
  def __init__(self): 
    print(f"Inicializando {type(self).__name__}...")

  def __repr__(self):
    return f"{type(self).__name__}()"

a = object.__new__(A)
a.__init__()

print(a)
```

Como resultado temos:

```
Inicializando A...
A()
```
