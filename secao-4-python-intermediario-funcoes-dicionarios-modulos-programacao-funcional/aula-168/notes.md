# Ordem de aplicação dos decoradores

A ordem de aplicação dos decoradores em Python é importante, pois determina a sequência em que os decoradores são aplicados a uma função. A ordem influencia o comportamento final da função decorada.

Quando vários decoradores são aplicados a uma função, a ordem de aplicação ocorre de baixo para cima, ou seja, do decorador mais próximo da função para o decorador mais externo. Isso significa que o decorador mais próximo da função será aplicado primeiro e, em seguida, os decoradores subsequentes serão aplicados na ordem em que foram especificados.

Aqui está um exemplo que ilustra a ordem de aplicação dos decoradores em Python:

```python
def decorador1(funcao):
    def funcao_decorada():
        print("Executando decorador 1")
        funcao()
    return funcao_decorada

def decorador2(funcao):
    def funcao_decorada():
        print("Executando decorador 2")
        funcao()
    return funcao_decorada

@decorador1
@decorador2
def minha_funcao():
    print("Executando minha_funcao.")

minha_funcao()
```

Neste exemplo, temos dois decoradores: `decorador1` e `decorador2`. A função `minha_funcao` é decorada com esses dois decoradores na ordem em que são especificados (`@decorador1` e em seguida `@decorador2`).

Quando chamamos `minha_funcao()`, a ordem de aplicação dos decoradores é a seguinte:

1. O decorador `decorador2` é aplicado primeiro. Ele envolve a função `minha_funcao` e adiciona código adicional à função decorada.
2. Em seguida, o decorador `decorador1` é aplicado. Ele envolve a função decorada pelo decorador `decorador2` e adiciona mais código adicional à função final decorada.

A saída do exemplo será:

```
Executando decorador 1
Executando decorador 2
Executando minha_funcao.
```

Observa-se que o decorador `decorador2` é aplicado primeiro e, em seguida, o decorador `decorador1`. Portanto, a ordem em que os decoradores são aplicados segue a ordem em que são especificados acima da definição da função decorada. É importante considerar a ordem dos decoradores ao projetar e aplicar decoradores em Python, pois isso pode afetar o comportamento esperado da função final decorada.