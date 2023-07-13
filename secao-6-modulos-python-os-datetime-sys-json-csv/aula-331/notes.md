# Deque - Trabalhando com LIFO e FIFO

Em Python, um `deque` (double-ended queue) é uma estrutura de dados que suporta a inserção e remoção eficiente de elementos tanto no início quanto no final da sequência. Isso permite que você trabalhe com o `deque` tanto no modo LIFO (Last In, First Out - último a entrar, primeiro a sair) quanto no modo FIFO (First In, First Out - primeiro a entrar, primeiro a sair).

Você pode usar a classe `deque` do módulo `collections` para criar e manipular um `deque` em Python. Primeiro, é necessário importar o módulo:

```python
from collections import deque
```

Aqui está um exemplo de uso de um `deque` como uma pilha (LIFO):

```python
stack = deque()  # Criando um deque vazio

stack.append("A")  # Adicionando elementos ao deque
stack.append("B")
stack.append("C")

print(stack)  # Saída: deque(['A', 'B', 'C'])

element = stack.pop()  # Removendo o elemento do topo da pilha
print(element)  # Saída: C

print(stack)  # Saída: deque(['A', 'B'])
```

Nesse exemplo, utilizamos o método `append` para adicionar elementos ao final do `deque` e o método `pop` para remover o último elemento adicionado (topo da pilha). A saída do programa demonstra a ordem em que os elementos são adicionados e removidos, seguindo a lógica LIFO.

Agora, vamos ver um exemplo de uso de um `deque` como uma fila (FIFO):

```python
queue = deque()  # Criando um deque vazio

queue.append("X")  # Adicionando elementos ao deque
queue.append("Y")
queue.append("Z")

print(queue)  # Saída: deque(['X', 'Y', 'Z'])

element = queue.popleft()  # Removendo o elemento do início da fila
print(element)  # Saída: X

print(queue)  # Saída: deque(['Y', 'Z'])
```

Nesse caso, utilizamos o método `append` para adicionar elementos ao final do `deque` e o método `popleft` para remover o primeiro elemento adicionado (início da fila). A saída do programa demonstra a ordem em que os elementos são adicionados e removidos, seguindo a lógica FIFO.

Em resumo, o deque em Python é uma estrutura de dados versátil que permite a inserção e remoção eficiente de elementos tanto no início quanto no final, oferecendo suporte tanto a LIFO quanto a FIFO. Isso proporciona flexibilidade ao lidar com diferentes necessidades de implementação.