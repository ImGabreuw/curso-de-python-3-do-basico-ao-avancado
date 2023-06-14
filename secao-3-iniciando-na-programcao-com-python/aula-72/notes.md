# Introdução ao for / in - estrutura de repetição para coisas finitas

> ## **For**

### **Definição**

Na maioria dos casos, é utilizado o `for` ao invés do `while` quando é conhecido o número de repetições de um laço.

### **Exemplo**

No caso abaixo, o número de repetições é determinada pelo tamanho do string armazenada em `texto`. Dessa forma, é muito mais conveniente o uso do `for`.

```python
texto = "Python"
i = 0

while i < len(texto):
  print(texto[i])
  i += 1

# P
# y
# t
# h
# o
# n
```

```python
texto = "Python"

for c in texto:
  print(c)

# P
# y
# t
# h
# o
# n
```

> `c` é uma variável da estrutura `for` que armazena o valor de cada posição do elemento a ser iterado, no caso acima, esse elemento é a `"Python"`.