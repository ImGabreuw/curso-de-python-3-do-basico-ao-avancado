# Conversa - tipos built-in, documentação, tipo imutáveis, métodos de string

Tipos build-in (ou embutidos) são tipo nativo do Python.

Os principais são: `str`, `int`, `float` e `bool`; Eles também são imutáveis, ou seja, não é possível alterar o valor dela após sua criação. Exemplo:

```python
string = "Python"

string[3] = "b" # TypeError: 'str' object does not support item assignment
```

No cenário acima, é possível utilizar o fatiamento de strings como alternativa:

```python
string = "Python"
outra_string = f"{string[:3]}b{string[4:]}"

print(string) # Python
print(outra_string) # Pytbon
```