# dataclasses - O que são dataclasses?

O módulo `dataclasses` fornece um decorador e funções para automatizar a criação de métodos como `__init__()`, `__repr__()`, `__eq__()`.

```python
from dataclasses import dataclass

@dataclass
class Pessoa:
  nome: str
  idade: int

if __name__ = "__main__":
  p1 = Pessoa("Luiz", 30)
  print(p1)
  # Saída: Pessoa(nome="Luiz", idade=30)
```
