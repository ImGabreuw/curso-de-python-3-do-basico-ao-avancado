# Problema dos parâmetros mutáveis em funções Python

O problema dos parâmetros mutáveis em funções Python ocorre quando uma função recebe um parâmetro que é um objeto mutável, como uma lista ou um dicionário, e realiza modificações nesse objeto dentro da função. Essas modificações afetam o objeto original fora da função, mesmo após a execução da função.

Isso acontece porque, em Python, os argumentos de função são passados por referência. Quando um objeto mutável é passado como argumento, a referência para esse objeto é passada para a função, e qualquer modificação feita no objeto dentro da função afetará o objeto original.

Aqui está um exemplo que ilustra o problema dos parâmetros mutáveis:

```python
def adicionar_elemento(lista, elemento):
    lista.append(elemento)

minha_lista = [1, 2, 3]
adicionar_elemento(minha_lista, 4)

print(minha_lista)  # Saída: [1, 2, 3, 4]
```

Neste exemplo, temos uma função `adicionar_elemento` que recebe uma lista e um elemento como argumentos. Dentro da função, usamos o método `append()` para adicionar o elemento à lista. No entanto, observe que a lista original `minha_lista` é modificada mesmo fora da função.

Isso ocorre porque a lista é um objeto mutável e a referência para essa lista é passada para a função. Portanto, qualquer modificação feita na lista dentro da função será refletida na lista original.

Para evitar esse problema, uma prática comum é criar uma cópia do objeto mutável dentro da função, para que as modificações sejam feitas apenas na cópia e não afetem o objeto original. Isso pode ser feito utilizando a função `list()` para criar uma nova lista ou o método `.copy()` para criar uma cópia da lista.

Aqui está um exemplo atualizado que utiliza uma cópia da lista dentro da função:

```python
def adicionar_elemento(lista, elemento):
    lista_copia = lista.copy()
    lista_copia.append(elemento)
    return lista_copia

minha_lista = [1, 2, 3]
minha_lista_atualizada = adicionar_elemento(minha_lista, 4)

print(minha_lista)  # Saída: [1, 2, 3]
print(minha_lista_atualizada)  # Saída: [1, 2, 3, 4]
```

Neste exemplo, a função `adicionar_elemento` cria uma cópia da lista usando o método `.copy()` e realiza a adição do elemento nessa cópia. A função retorna a lista atualizada, mas a lista original `minha_lista` permanece inalterada.

Entretanto, mesmo sendo uma solução ainda não é a ideal. A solução ideal é não utilizar valor padrão mutável em parâmetro.

Lembrando que nem todos os objetos em Python são mutáveis. Objetos imutáveis, como strings e tuplas, não sofrem do problema dos parâmetros mutáveis, pois não podem ser modificados após a criação.

Portanto, ao lidar com parâmetros mutáveis em funções Python, é importante estar ciente desse comportamento e tomar as medidas adequadas para evitar modificações indesejadas nos objetos originais.