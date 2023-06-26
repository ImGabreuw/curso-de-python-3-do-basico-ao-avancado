# Limite de recursão e cuidados com funções recursivas

É possível alterar o limite de recursão no Python a partir do método `setrecursionlimit()` do módulo `sys`:

```python
import sys

sys.setrecursionlimit(1004)

# ...
```

O limite padrão de recursividade no Python é de 1000 chamadas, porém esse número pode variar de acordo com a implementação do algoritmo recursivo. Por exemplo:

```python
def counter(start=0, end=10):
  print(start)

  if start >= end:
    return start

  start += 1
  return counter(start, end)

counter(end=1000)
```

Saída do código acima:

```console
0
1
...
995
966
```

Essa variação acontece, pois para cada recursão o Python armazena as informações do escopo de função de cada recursão (módulos, variáveis, etc).