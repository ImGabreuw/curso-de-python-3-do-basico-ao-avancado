# Como o for funciona por baixo dos panos? (next, iter, iterável e iterador)

> ## **Objetos iteráveis**

### **Definição**

Um objeto é classificado como iterável quando é implementado o método `__iter__()`. Esse método retorna um **iterador** que é responsável por gerenciar qual elemento deve ser retornado após a execução do método `__next__()`.

É possível obter o iterador de um objeto iterável a partir da função `iter()`. Além disso, existe a função `next()` que é idêntica ao `__next__()`.

Caso o método `next()` ou `__next__()` seja executado mesmo não tendo um próximo elemento, será lançado o erro `StopIteration`.

> ## **Exemplo**

```python
texto = "Luiz"

print(texto.__iter__()) # <str_iterator object at 0x7f6b02cdb730>
print(iter(texto)) # <str_iterator object at 0x7f6b02cdb730>

texto = texto.__iter__()

print(texto.__next__()) # L
print(texto.__next__()) # u
print(next(texto)) # i
print(next(texto)) # z

print(next(texto))
# Traceback (most recent call last):
#   File "/home/gabriel/Projects/curso-de-python-3-do-basico-ao-avancado/secao-3-iniciando-na-programcao-com-python/aula-74/example-1.py", line 12, in <module>
#     print(texto.__next__())
# StopIteration
```

Simulando o comportamento do `for` com `while`:

```python
texto = "Luiz"
iterador = iter(texto)

while True:
  try:
    letra = next(iterador)
    print(letra)
  except StopIteration:
    break

# L
# u
# i
# z
```