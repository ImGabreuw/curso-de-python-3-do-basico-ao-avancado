# Empacotamento e desempacotamento de dicionários + *args e **kwargs

> ## **Empacotamento e desempacotamento de dicionários**

Em Python, o empacotamento e desempacotamento de dicionários são operações que permitem combinar ou separar os elementos de um dicionário de forma conveniente. 

O empacotamento de dicionário é a ação de agrupar vários elementos-chave e valores em um único dicionário. Isso pode ser feito de diferentes maneiras, mas uma das formas mais comuns é simplesmente criar um novo dicionário, atribuindo os pares chave-valor desejados. Por exemplo:

```python
dados = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}
```

Aqui, empacotamos os elementos em um dicionário chamado "dados" com três pares chave-valor: 'nome', 'idade' e 'cidade'.

Já o desempacotamento de dicionário é o processo inverso, em que separamos os elementos de um dicionário em variáveis individuais. Para isso, utilizamos o operador `**` antes do nome do dicionário. Por exemplo:

```python
dados = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}

nome, idade, cidade = dados.values()
print(nome)    # Saída: João
print(idade)   # Saída: 25
print(cidade)  # Saída: São Paulo
```

Nesse exemplo, realizamos o desempacotamento do dicionário "dados" nas variáveis "nome", "idade" e "cidade". Cada variável recebe o valor correspondente do dicionário.

É importante observar que, para que o desempacotamento funcione corretamente, é necessário que as chaves do dicionário correspondam aos nomes das variáveis de destino.

Além disso, o desempacotamento também pode ser usado para passar argumentos nomeados para uma função. Nesse caso, o dicionário contendo os argumentos é desempacotado durante a chamada da função. Por exemplo:

```python
def mostrar_informacoes(nome, idade, cidade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

dados = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}

mostrar_informacoes(**dados)
```

Nesse exemplo, desempacotamos o dicionário "dados" durante a chamada da função "mostrar_informacoes". Os valores correspondentes são passados como argumentos nomeados para a função, permitindo que ela exiba as informações corretamente.

Em resumo, o empacotamento e desempacotamento de dicionários em Python são operações úteis para combinar ou separar os elementos de um dicionário, seja para criar um novo dicionário, atribuir valores a variáveis individuais ou passar argumentos nomeados para funções.

> ## **Keyword arguments (kwargs)**

Em Python, `kwargs` é uma abreviação de "keyword arguments" (argumentos de palavra-chave) e é uma convenção usada para lidar com argumentos nomeados em uma função. O `kwargs` permite que você passe um número variável de argumentos nomeados para uma função, que são agrupados em um dicionário.

Ao usar `kwargs`, você pode definir uma função com um parâmetro prefixado com dois asteriscos (`**`). Isso indica que a função aceita argumentos nomeados arbitrários e os agrupa em um dicionário dentro da função. Cada chave do dicionário corresponderá ao nome do argumento e o valor será o valor fornecido para aquele argumento.

Aqui está um exemplo que demonstra o uso do `kwargs`:

```python
def exibir_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_informacoes(nome='João', idade=25, cidade='São Paulo')
```

Nesse exemplo, a função `exibir_informacoes` possui o parâmetro `**kwargs`, que permite que ela aceite qualquer número de argumentos nomeados. Dentro da função, esses argumentos nomeados são tratados como um dicionário, onde cada chave é o nome do argumento e o valor é o valor fornecido para esse argumento.

Ao chamar a função `exibir_informacoes` e passar os argumentos nomeados `nome`, `idade` e `cidade`, esses argumentos são agrupados no dicionário `kwargs` dentro da função. Em seguida, o loop `for` percorre o dicionário `kwargs` e exibe cada chave e valor.

A saída desse exemplo seria:

```
nome: João
idade: 25
cidade: São Paulo
```

O uso de `kwargs` é útil quando você precisa lidar com um número variável de argumentos nomeados em uma função. Ele fornece flexibilidade e permite que os usuários chamem a função com diferentes argumentos nomeados sem a necessidade de definir explicitamente todos os parâmetros na função.
