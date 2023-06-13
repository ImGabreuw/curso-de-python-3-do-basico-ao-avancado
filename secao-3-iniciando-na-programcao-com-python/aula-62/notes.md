# while + continue - pulando alguma repetição

> ## **Definição**

A palavra reservado `continue` tem a função de pular para o próximo laço do loop mais próximo.

> ## **Exemplo**

```python
contador = 1

while contador <= 10:
  contador += 1

  if contador == 5:
    print("Pulou o 5")
    continue

  print(contador)

# 1
# 2
# 3
# 4
# Pulou o 5
# 6
# 7
# 8
# 9
# 10
```