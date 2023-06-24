# Funções decoradoras em geral

Em Python, as funções decoradoras são funções que envolvem outras funções para estender ou modificar seu comportamento sem modificar seu código original. Elas permitem adicionar funcionalidades extras a uma função sem precisar alterar seu código-fonte.

Aqui está um exemplo que ilustra o conceito de funções decoradoras em Python:

```python
def decorador(funcao):
    def funcao_decorada(*args, **kwargs):
        print("Antes da execução da função.")
        resultado = funcao(*args, **kwargs)
        print("Depois da execução da função.")
        return resultado
    return funcao_decorada

def minha_funcao():
    print("Executando minha_funcao.")

funcao_decorada = decorador(minha_funcao)
funcao_decorada()
```

Neste exemplo, temos a função `decorador`, que é a função decoradora em si. Ela recebe uma função como argumento (`funcao`) e retorna uma nova função interna chamada `funcao_decorada`. Essa função interna é responsável por executar o código adicional antes e depois da função original.

Em seguida, temos a função `minha_funcao`, que é a função que queremos decorar. A linha `funcao_decorada = decorador(minha_funcao)` aplica a função decoradora `decorador` à função `minha_funcao` e armazena o resultado na variável `funcao_decorada`.

Finalmente, chamamos a função decorada usando `funcao_decorada()`. Isso executará o código adicional dentro da função decoradora antes e depois da função `minha_funcao`.

A saída do exemplo será:

```
Antes da execução da função.
Executando minha_funcao.
Depois da execução da função.
```

Observe que esse exemplo não utiliza a sintaxe de açúcar (`@decorator`) para aplicar a função decoradora à função original. Em vez disso, fazemos manualmente chamando a função decoradora e atribuindo o resultado a uma nova variável. No entanto, o efeito é o mesmo: a função decorada possui o comportamento adicional fornecido pela função decoradora.