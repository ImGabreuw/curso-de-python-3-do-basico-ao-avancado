# count é um iterador sem fim (itertools)

A função `count()` da biblioteca `itertools` em Python é usada para gerar uma sequência infinita de números. Ela retorna um iterador que produz valores consecutivos, começando a partir de um número inicial especificado.

Aqui está um exemplo que ilustra o uso da função `count()`:

```python
from itertools import count

for i in count(start=1, step=2):
    print(i)
    if i >= 10:
        break
```

Neste exemplo, usamos `count(start=1, step=2)` para criar um iterador que gera números consecutivos a partir do número 1, aumentando de 2 em 2. No loop `for`, imprimimos cada número gerado pelo iterador até que `i` seja maior ou igual a 10. Como `count()` gera uma sequência infinita, usamos a declaração `break` para interromper o loop após um determinado limite.

A saída será:

```
1
3
5
7
9
11
```

Observe que a função `count()` gera uma sequência infinita de números consecutivos, permitindo que você controle o ponto de partida (`start`) e o incremento (`step`).

Por outro lado, a função `range()` em Python é usada para gerar uma sequência finita de números. Ela retorna um objeto de tipo `range` que representa uma sequência imutável de números.

Aqui está um exemplo que ilustra o uso da função `range()`:

```python
for i in range(1, 10, 2):
    print(i)
```

Neste exemplo, usamos `range(1, 10, 2)` para criar uma sequência de números começando em 1, aumentando de 2 em 2 e indo até 10 (exclusivo). No loop `for`, imprimimos cada número da sequência gerada por `range()`.

A saída será:

```
1
3
5
7
9
```

Observe que a função `range()` gera uma sequência finita de números, permitindo que você especifique o início, o fim e o incremento da sequência.

Em resumo, a função `count()` da biblioteca `itertools` gera uma sequência infinita de números consecutivos, enquanto a função `range()` gera uma sequência finita de números. A função `count()` é útil quando você precisa de uma sequência infinita de valores, enquanto `range()` é adequada para sequências de tamanho definido.

### **Observação**

O `count()` é um iterável e um iterador, já o `range` é apenas iterável. É possível provar isso com o seguinte exemplo:

```python
from itertools import count

c = count()
r = range(0, 10)

print("count têm '__iter__'?", hasattr(c, "__iter__"))
print("count têm '__next__'?", hasattr(c, "__next__"))
print("range têm '__iter__'?", hasattr(r, "__iter__"))
print("range têm '__next__'?", hasattr(r, "__next__"))
```

Saída do exemplo acima:

```console
count têm '__iter__' True
count têm '__next__' True
range têm '__iter__' True
range têm '__next__' False
```

Dessa forma, `count()` é um iterável e um iterador por ter respectivamente os métodos `__iter__` e `__next__`. Já o `range()` é apenas iterável, pois tem apenas o método `__iter__`.