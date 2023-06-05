# Operador Lógico "and"

> ## **Definição**

O operador lógico `e` é representado por `and`.

Para que uma expressão com `and` seja avaliada como verdadeira é necessários que todas as condições sejam verdadeiras, como é possível ver na **tabela verdade**:

| condição 1 | condição 2 | operação `and` |
| :--------: | :--------: | :------------: |
|     1      |     1      |       1        |
|     1      |     0      |       0        |
|     0      |     1      |       0        |
|     0      |     0      |       0        |

São considerados valores _falsy_: `0`, `0.0`, `''`, `""` e `False`

**OBS**: o tipo `None` serve para representar a **ausência de valor**

> ## **Exemplo**

```python
# Avaliação de curto circuito
print(True and False and True) # False
```

A **avaliação de curto circuito** é quando o interpretador do Python ao se deparar com uma condição falsa em uma expressão com operador `and`, ele **ignora as outras condições** mesmo que sejam verdadeiras.

```python
print(True and 0 and True) # False
```
