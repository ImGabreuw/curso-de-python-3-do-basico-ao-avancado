# split, join e strip são métodos muito úteis da str

> ## **Método: `split()`**

### **Definição**

Esse método separa uma string em uma lista a partir de um caractere fornecido como argumento, por padrão é utilizado o espaço em branco.

Além disso, é possível utilizar expressões regulares (_RegEx_) para realizar uma separação mais complexa.

### **Exemplo**

```python
frase = "Olha só que coisa interessante"

print(frase.split()) 
# ['Olha', 'só', 'que', 'coisa', 'interessante']
```

```python
frase = "Olha só, que coisa interessante"

print(frase.split(","))
# ['Olha só', ' que coisa interessante']
```

> ## **Método: `strip`**

### **Definição**

Esse método remove os espaços em branco no começo e no final de uma string.

Além disso, existem 2 variações desse método:

- `rstrip()`: remove os espaços em branco do lado direito da string

- `lstrip()`: remove os espaços em branco do lado esquerdo da string

### **Exemplo**

```python
frase = "  Olá mundo!  "
print(frase.strip())

# Olá mundo!
```

```python
frase = "  Olá mundo!  "
print(frase.rstrip())

#   Olá mundo!
```

```python
frase = "  Olá mundo!  "
print(frase.lstrip())

# Olá mundo!
```

> ## **Método: `join()`**

### **Definição**

Esse método junta cada elemento de uma lista em uma string a partir de um caractere de junção.

### **Exemplo**

```python
lista = ["Python", "é", "uma", "linguagem", "de", "programação"]

print(" ".join(lista))
# Python é uma linguagem de programação
```

```python
lista = ["Python", "é", "uma", "linguagem", "de", "programação"]

print("-".join(lista))
# Python-é-uma-linguagem-de-programação
```