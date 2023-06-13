# while / else (recurso peculiar do Python)

> ## **Definição**

O bloco `else` é executado quando o  `while` não for interrompido com `break`, por exemplo:

Essa sintaxe é específico do Python e é uma funcionalidade muito pouco usada.

> ## **Exemplo**

```python
i = 0

while i < 5:
  i += 1
  print(i)
else:
  print("Bloco 'else' foi executado")

# 1
# 2
# 3
# 4
# 5
# Bloco 'else' foi executado
```

```python
i = 0

while i < 5:
  i += 1
  print(i)

  if i == 3:
    break
else:
  print("Bloco 'else' foi executado")

# 1
# 2
# 3
```

```python
i = 0

while i < 5:
  i += 1

  if i == 3:
    continue
  
  print(i)
else:
  print("Bloco 'else' foi executado")

# 1
# 2
# 4
# 5
# Bloco 'else' foi executado
```