# (Parte 1) Escopo de funções e módulos em Python + global

> ## **Definição**

Escopo é o local onde um código pode ser utilizado.

Existem 2 classificações de escopo: 

- Global: o código pode ser utilizado em qualquer

  > Para criar uma variável global é necessário defini-la com `global` antes do nome e depois atribuir um valor a ela.

- Local: o código é restrito a apenas um determinado local

Existe também o escopo de funções, o qual o código definido no corpo dela não é visível de fora da função. Por exemplo:

```python
def escopo():
  # Escopo da função
  x = 1
  print(x)

escopo() # 1
print(x) # Erro: variável não foi definida
```

```python
x = 1

def escopo():
  print(x)

escopo() # 1
print(x) # 1
```

No caso acima, a variável `x` está definida no mesmo escopo da função (escopo do módulo), desse modo tanto o `print()` dentro da função `escopo` quanto o de fora, podem ser executados.

De forma geral, o escopo funciona como uma árvore, sendo a raiz o escopo global e as ramificações como os escopos locais onde elas seguem um nível hierárquico, o nó "pai" pode acessar os escopos dos nós "filhos", mas os nós "filhos" não pode acessar o escopo do nó "pai".