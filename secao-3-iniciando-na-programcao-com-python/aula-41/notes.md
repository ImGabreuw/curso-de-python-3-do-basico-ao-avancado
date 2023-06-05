# Operador Lógico "or"

> ## **Definição**

O operador lógico `ou` (inclusivo) é representado por `or`.

Para que uma expressão com `orr` seja avaliada como verdadeira é necessários que pelo menos uma condição sejam verdadeiras, como é possível ver na **tabela verdade**:

| condição 1 | condição 2 | operação `and` |
| :--------: | :--------: | :------------: |
|     1      |     1      |       1        |
|     1      |     0      |       1        |
|     0      |     1      |       1        |
|     0      |     0      |       0        |

São considerados valores _falsy_: `0`, `0.0`, `''`, `""` e `False`

**OBS**: o tipo `None` serve para representar a **ausência de valor**

Expressões lógicas com `or` e `and` podem se tornar ambíguas. Com isso, é recomendado utilizar os parênteses para esclarecer tais expressões:

```python
entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = "123456"

if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
  print("Entrar")
else:
  print("Sair")
```

> ## **Exemplo**

```python
# Avaliação de curto circuito
print(True or False) # True
```

A avaliação de curto circuito em expressões com `or` é quando o interpretador do Python ao se deparar com uma condição verdadeira, ele **ignora as outras condições** mesmo que sejam falsas.

```python
print(0 or False or 0.0 or "abc" or True) # abc
print(0 or False or 0.0 or True or "abc") # True
```

No Python, assim como no JavaScript, as expressões lógicas retornam o primeiro valor verdadeiro.
