# while - Condição em detalhes

Alterando o estado de uma condição do `while`:

```python
contador = 0

while contador < 10:
  print(contador)
  contador += 1

# 0
# 1
# 2
# ...
# 9
```

```python
contador = 0

while contador < 10:
  contador += 1
  print(contador)

# 1
# 2
# 3
# ...
# 10
```