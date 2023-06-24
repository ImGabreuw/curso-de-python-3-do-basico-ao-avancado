# Variáveis livres + nonlocal (locals, globals)

> ## **Variável livre**

Em Python, uma variável livre é uma variável definida em um escopo externo ao de uma função aninhada, mas que é referenciada dentro dessa função, ou seja, ela pode ser acessada e usada pela função, mesmo que não seja uma variável local dentro dela. Essa capacidade é conhecida como "captura de variáveis".

Aqui está um exemplo que ilustra o conceito de variáveis livres em Python:

```python
def exterior():
    x = 10

    def interior():
        print(x)  # Acessando a variável "x" definida no escopo da função exterior

    return interior

funcao = exterior()
funcao()  # Output: 10
```

Nesse exemplo, temos duas funções aninhadas: `exterior()` e `interior()`. A função `exterior()` define uma variável `x` com o valor 10. A função `interior()` está aninhada dentro de `exterior()` e imprime o valor de `x`.

A linha `funcao = exterior()` cria uma instância da função `interior()` e atribui a essa instância à variável `funcao`. Quando chamamos `funcao()`, ela executa o corpo da função `interior()`, acessando a variável `x` definida na função `exterior()` e imprimindo o valor 10.

Neste exemplo, a variável `x` é uma variável livre para a função `interior()`, pois ela é referenciada dentro dessa função, embora seja definida no escopo da função `exterior()`. A função `interior()` captura essa variável livre e pode usá-la normalmente.

> ## **Escopo de variáveis**

Em Python, existem três palavras-chave relacionadas ao escopo de variáveis: `nonlocal`, `locals` e `globals`.

### **`nonlocal`**

A palavra-chave `nonlocal` é usada dentro de uma função aninhada para indicar que uma variável não é local a essa função nem global, mas pertence a um escopo externo específico.

Ela é usada para acessar e modificar variáveis de um escopo superior ao da função aninhada imediata.

Aqui está um exemplo que demonstra o uso de `nonlocal`:

```python
def exterior():
    x = 10

    def interior():
        nonlocal x
        x = 20

    interior()
    print(x)  # Output: 20

exterior()
```

Neste exemplo, a função `interior()` usa a palavra-chave `nonlocal` para indicar que a variável `x` não é local a ela, mas pertence ao escopo da função `exterior()`. Ao atribuir o valor 20 a `x` dentro da função `interior()`, a variável `x` no escopo da função `exterior()` é modificada.

### **`locals()`**

`locals()` é uma função embutida em Python que retorna um dicionário que representa o escopo local atual.

Esse dicionário contém as variáveis e seus valores no escopo atual.

Aqui está um exemplo que mostra o uso de `locals()`:

```python
def minha_funcao():
    a = 10
    b = 20
    escopo_local = locals()
    print(escopo_local)

minha_funcao()
```

Neste exemplo, a função `minha_funcao()` usa `locals()` para obter um dicionário do escopo local atual. Em seguida, ele imprime o conteúdo desse dicionário. A saída será um dicionário que contém as variáveis `a` e `b` juntamente com seus valores.

### **`globals()`**

`globals()` é uma função embutida em Python que retorna um dicionário que representa o escopo global atual.

Esse dicionário contém as variáveis e seus valores no escopo global.

Aqui está um exemplo que mostra o uso de `globals()`:

```python
x = 10

def minha_funcao():
    escopo_global = globals()
    print(escopo_global['x'])

minha_funcao()
```

Neste exemplo, temos uma variável global `x` com o valor 10. A função `minha_funcao()` usa `globals()` para obter o dicionário do escopo global atual e, em seguida, imprime o valor da variável `x` acessando-a através do dicionário `escopo_global`.

Essas palavras-chave e funções podem ser úteis ao lidar com escopos de variáveis em Python, permitindo acessar e manipular variáveis em diferentes níveis de escopo.
