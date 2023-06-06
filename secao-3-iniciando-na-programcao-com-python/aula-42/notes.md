# Operador lógico "not"

> ## **Definição**

O operador lógico `não` é representado por `not`.

Este operador é responsável por retornar o complemento da expressão, ou seja, ele inverte o valor lógico da expressão. Veja na **tabela verdade**:

| condição | operação `not` |
| :------: | :------------: |
|    0     |       1        |
|    1     |       0        |

> ## **Exemplo**

```python
senha = input("Senha: ")

if not senha:
  print("Por favor insira a senha.")
```
