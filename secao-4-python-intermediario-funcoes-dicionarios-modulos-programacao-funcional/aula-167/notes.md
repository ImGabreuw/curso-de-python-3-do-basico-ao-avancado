# Decoradores com parâmetros

Em Python, é possível criar decoradores que aceitam parâmetros. Isso permite personalizar o comportamento do decorador para atender a requisitos específicos. Para criar decoradores com parâmetros, é necessário adicionar uma camada extra de funções.

Aqui está um exemplo que ilustra o uso de decoradores com parâmetros em Python:

```python
def decorador_com_parametro(parametro):
    def decorador(funcao):
        def funcao_decorada(*args, **kwargs):
            print("Parâmetro do decorador:", parametro)
            print("Antes da execução da função.")
            resultado = funcao(*args, **kwargs)
            print("Depois da execução da função.")
            return resultado
        return funcao_decorada
    return decorador

@decorador_com_parametro("Meu parâmetro")
def minha_funcao():
    print("Executando minha_funcao.")

minha_funcao()
```

Neste exemplo, temos uma função decoradora `decorador_com_parametro` que aceita um parâmetro `parametro`. Essa função decoradora retorna uma função interna `decorador`, que é o decorador real.

A função `decorador` envolve a função original (`funcao`) e retorna outra função interna `funcao_decorada`. A função `funcao_decorada` executa o código adicional do decorador e, em seguida, chama a função original.

Usando a sintaxe de açúcar `@decorador_com_parametro("Meu parâmetro")`, aplicamos o decorador com o parâmetro especificado à função `minha_funcao`.

Quando chamamos `minha_funcao()`, o decorador é aplicado com o parâmetro fornecido. O código adicional dentro da função decoradora é executado antes e depois da função `minha_funcao`, exibindo o parâmetro passado.

A saída do exemplo será:

```
Parâmetro do decorador: Meu parâmetro
Antes da execução da função.
Executando minha_funcao.
Depois da execução da função.
```

Observação: ao criar decoradores com parâmetros, é importante garantir que as funções decoradas e os parâmetros estejam alinhados corretamente para evitar erros.