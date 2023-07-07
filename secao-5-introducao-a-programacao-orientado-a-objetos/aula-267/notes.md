# `__init__` e `__post_init__` em dataclasses

O _dunder method_ `__post_init__()` é executado imediatamente após a chamada do `__init__()` da dataclass.

```python
from dataclasses import dataclass

@dataclass
class Pessoa:
  nome: str
  sobrenome: str

  def __post_init__(self):
    self.nome_completo = f"{self.nome} {self.sobrenome}"

p1 = Pessoa("Luiz", "Otávio")
print(p1.sobrenome)

# Saída: Luiz Otávio
```

Caso a classe não tenha o método `__init__()`, não haverá também o método `__post_init__()`.

```python
from dataclasses import dataclass

@dataclass(init=False)
class Teste:
  def __post_init__(self):
    print("POST INIT")

print(Teste())

# Saída: Teste()
```

Como pode-se observar na saída, o `print()` dentro do `__post_init__()` não foi executado, pois não existe o método `__init__()`.