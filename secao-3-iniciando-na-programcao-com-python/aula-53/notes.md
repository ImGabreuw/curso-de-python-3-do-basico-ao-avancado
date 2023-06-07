# Flags, is, is not e None

> ## **Flag**

_Flag_ é um termo utilizado para **"marcar um local"** no código, seria uma alternativa à depuração de código.

```python
condicao = True

passou_no_if = None

if condicao:
  passou_no_if = True
  ...
else:
  ...

print("Passou no if?", passou_no_if is not None) # Passou no if? True
```

> `passou_no_if` é uma _flag_ para verificar se durante a execução do programa o interpretador passou no bloco do `if`.

> ## **Tipo: `None`**

O tipo `None` representa a ausência de valor em uma variável.

Para verificar se uma variável **é** `None`, você usa o operador `is`:

```python
var = None

print(var is None) # True
```

Para verificar se uma variável **não é** `None`, você utiliza o operator `not` para inverter a condição do `is`:

```python
var = 10

print(var is not None) # True
```