# Interpolação de string com % em Python

> ## **Definição**

Existem 3 tipos de formatação de strings no Python:

1. f-strings (recomendado)

2. `.format()`

3. Interpolação

A interpolação com _placeholder_ (`%`) é tem a seguinte sintaxe:

```python
"<placeholder 1> <placeholder 2>" % (<valor 1>, <valor 2>)
```

**IMPORTANTE**: o número de _placeholders_ precisa ser igual ao dos valores inseridos após o `%`. Caso contrário será lançado um `TypeError`

Existem 4 tipos de _placeholder_:

- `%s`: string

- `%d` ou `%i`: int

- `%.<número de casas decimais>f`: float

- `%<número de dígitos>x`: hexadecimais com as letras minúsculas (`abcdef0123456789`)

- `%<número de dígitos>X`: hexadecimais com as letras maiúsculas (`ABCDEF0123456789`)

> ## **Exemplo**

```python
nome = "Luiz"
preco = 1000.95897643

print("%s, o preço é R$%.2f" % (nome, preco))
# Luiz, o preço é R$1000.96
```

```python
num = 15

print("O hexadecimal de %d é %04x" % (num, num))
# O hexadecimal de 15 é 000f
```
