# Alterando uma lista com índices, del, append e pop (Tipo list)

> ## **Definição**

É esperado que qualquer lista seja capaz de realizar tarefas tais como:

- Recuperar um item que esteja armazenado em certa posição da lista.

- Substituir um elemento por outro, fazendo a troca de um valor que esteja armazenado por algum outro valor.

- Acrescentar um novo elemento (ao final) e estender a lista.

- Inserir um novo elemento entre outros já existentes, reorganizando as informações e o posicionamento dos elementos.

- Remover um elemento em particular, reduzindo a quantidade de elementos armazenados na lista.

Diferentes de outros tipo de coleções em Python, uma lista é:

- uma estrutura de dados linear;

- mutável (ou seja, pode ser modificada);

- de comprimento variável;

- que permite tipos diferentes de elementos (heterogênea).

É dada entre colchetes, com seus elementos separados por vírgula.

Exemplos:

- `[1, 10, 3]`

- `['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Brasília', 'Manaus’]`

- `[5, 'maçã', True, 10]`

- `[]` (Lista vazia)

> ## **Métodos úteis**

### **Recuperar um dado**

Cada elemento de uma lista é referenciado por um índice, isto é, um inteiro positivo que permite acessar um item individualmente dentro do conjunto.

```python
lstCompras = ['cereal', 'banana', 'maçã', 'melão']

print('1o item: ', lstCompras[0]) # 1o item: cereal
print('4o item: ', lstCompras[3]) # 4o item: melão
```

### **Substituir um item**

Usando o nome da lista e informando o índice do elemento a ser substituído, basta fazer uma atribuição do novo valor.

```python
lstCompras = ['cereal', 'banana', 'maçã', 'melão']
print('Lista: ', lstCompras) # Lista: ['cereal', 'banana', 'maçã', 'melão']

lstCompras[2] = 'leite'
print('Lista: ', lstCompras) # Lista: ['cereal', 'banana', 'leite', 'melão']
```

### **Acrescentando um item**

Usando o método append adicionamos um novo valor a lista, que será incluído ao seu final e estenderá o comprimento da lista.

```python
[nome da lista].append([novo elemento])
```

```python
lstCompras = ['cereal', 'banana', 'maçã', 'melão’]
lstCompras.append('leite')

print('Lista: ', lstCompras) # Lista: ['cereal', 'banana', 'maçã', 'melão', 'leite']
```

O método insert também adiciona um novo valor a lista, porém em uma posição em particular. Os itens são deslocados para que o novo elemento seja acrescentado a lista e o comprimento é estendido.

> **OBS**: não é recomendado seu uso, pois o realocamento dos elementos posteriores ao elemento inserido acarreta um alto consumo de memória, além da lentidão em sua execução.

```python
[nome da lista].insert([índice], [novo item])
```

```python
lstCompras = ['cereal', 'banana', 'maçã', 'melão']
lstCompras.insert(1,'leite')

print('Lista: ', lstCompras) # Lista: ['cereal', 'leite', 'banana', 'maçã', 'melão']
```

### **Removendo um item**

Usando o método remove podemos excluir a primeira ocorrência de um determinado item da lista.

```python
[nome da lista].remove([item])
```

```python
lstCompras=['cereal','banana','maçã','melão','banana']
lstCompras.remove('banana')
print('Lista: ', lstCompras) # Lista: ['cereal', 'maçã', 'melão', 'banana']
```

A função built-in del serve para desalocar a memória reservada e excluir uma variável. Desta forma, pode ser utilizada com listas para remover um item ou até mesmo a lista inteira.

> **OBS**: assim como o `insert()` o seu uso não é recomendado, uma vez que esse processo provoca um alto consumo de memória e tempo para ser executado.

```python
del [nome da lista][ [índice] ]

# OU

del [nome da lista]
```

```python
lstCompras = ['cereal', 'banana', 'maçã', 'melão’]
del lstCompras[0]
print('Lista: ', lstCompras) # Lista: ['banana', 'maçã', 'melão']
del lstCompras
print('Lista: ', lstCompras) # NameError: name 'lstCompras' is not defined
```

### **Outros métodos das listas**

Assim como o append, o insert e o remove, as listas contam com outros métodos úteis a diferentes propósitos de manipulação:

- count([item]): retorna o número de ocorrências de um item na lista;

- index([item]): devolve o índice (posição) da primeira ocorrência do item na lista, mas resultará em erro caso o item não esteja presente.

- sort(): ordena os elementos armazenados na lista de acordo com a sua natureza. Isto é, valores numéricos de forma crescente e itens de texto em ordem alfabética;

- reverse(): reorganiza os elementos de forma inversa, fazendo com que o primeiro se torne o último; e o último, o primeiro.

### **Funções built-in com listas**

A linguagem Python dispõe de alguma funções nativas que podem ser aplicadas a listas, são elas:

- `del [nome da lista][ [índice] ]` que, como vimos, pode remover um item da lista; ou del [nome da lista] para excluir inteiramente a variável lista da memória;

- `len([nome da lista])`, do inglês length (comprimento), que nos retorna a quantidade de elementos estão armazenados na lista;

- `max([nome da lista])` e `min([nome da lista])` que retornam, respectivamente, o maior e o menor valor dentre todos os elementos da coleção; e

- `sum([nome da lista])` devolve a somatória dos elementos armazenados em listas numéricas, não sendo aplicável a coleções com outros tipos de dados.