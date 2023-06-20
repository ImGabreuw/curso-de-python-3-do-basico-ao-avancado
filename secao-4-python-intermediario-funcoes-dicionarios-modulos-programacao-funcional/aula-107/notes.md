# Valores padrão para parâmetros em funções Python + NoneType e None

> ## **Valores padrão para parâmetros**

Ao definir uma função, os parâmetros podem ter valores padrão. Caso o valor não seja inserido como argumento da função, o valor padrão será usado.

```python
def soma (x, y, z = None):
  if z is not None:
    print(f"{x=} {y=} {z=}", x + y + z)  
  else:
    print(f"{x=} {y=}", x + y)  

soma(1, 2) # x=1 y=2 3
soma(1, 2, 0) # x=1 y=2 z=0 3
soma(1, 2, 3) # x=1 y=2 z=3 6
```

Geralmente os valores padrão são valores considerados _falsy_ pelo Python, pois com isso é possível fazer verificações mais simples (com `is` por exemplo) e evitar bugs desnecessários.