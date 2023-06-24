# Decoradores em Python (@syntax_sugar)

Em Python, os decoradores podem ser definidos utilizando  "açúcar sintático" `@`. Essa sintaxe torna mais fácil aplicar um decorador a uma função sem precisar usar a forma manual que expliquei anteriormente. 

Aqui está um exemplo que demonstra o uso de decoradores com a sintaxe `@` em Python:

```python
def decorador(funcao):
    def funcao_decorada(*args, **kwargs):
        print("Antes da execução da função.")
        resultado = funcao(*args, **kwargs)
        print("Depois da execução da função.")
        return resultado
    return funcao_decorada

@decorador
def minha_funcao():
    print("Executando minha_funcao.")

minha_funcao()
```

Neste exemplo, temos a mesma função decoradora `decorador` e a mesma função `minha_funcao` que queremos decorar. No entanto, agora usamos a sintaxe `@decorador` diretamente acima da declaração da função `minha_funcao`.

Quando executamos o código acima, o decorador é aplicado automaticamente à função `minha_funcao`. Isso significa que, ao chamar `minha_funcao()`, o código adicional dentro do `decorador` será executado.

Essa sintaxe é equivalente a chamar manualmente o decorador da seguinte maneira:

```python
minha_funcao = decorador(minha_funcao)
```


A saída do exemplo será a mesma do exemplo anterior:

```
Antes da execução da função.
Executando minha_funcao.
Depois da execução da função.
```

A sintaxe de açúcar `@` simplifica a aplicação de decoradores em Python, tornando o código mais legível e conciso. É uma forma conveniente de estender e modificar o comportamento de funções sem alterar seu código original.