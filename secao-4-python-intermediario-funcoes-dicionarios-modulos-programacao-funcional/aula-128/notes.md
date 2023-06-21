# Métodos úteis do tipo set em Python

### **Método: `conjunto.add()`**

O método `add( [elemento] )` adiciona um elemento ao conjunto. Se o elemento já estiver presente no conjunto, ele será ignorado, pois os conjuntos não permitem duplicatas. Aqui está um exemplo:

```python
meu_conjunto = {1, 2, 3}
meu_conjunto.add(4)
print(meu_conjunto)  # Saída: {1, 2, 3, 4}
```

### **Método: `conjunto.update()`**:

O método `update( [iterável] )` adiciona múltiplos elementos ao conjunto. Ele recebe um iterável, como uma lista ou outro conjunto, e adiciona cada elemento ao conjunto. Aqui está um exemplo:

```python
meu_conjunto = {1, 2, 3}
meu_conjunto.update([4, 5, 6])
print(meu_conjunto)  # Saída: {1, 2, 3, 4, 5, 6}
```

### **Método: `conjunto.clear()`**

O método `clear()` remove todos os elementos do conjunto, deixando-o vazio. Ele modifica o conjunto original. Aqui está um exemplo:

```python
meu_conjunto = {1, 2, 3}
meu_conjunto.clear()
print(meu_conjunto)  # Saída: set()
```

### **Método: `conjunto.discard(elemento)`**

O método `discard()` remove um elemento específico do conjunto, se ele estiver presente. Se o elemento não estiver no conjunto, não ocorrerá nenhum erro. Aqui está um exemplo:

```python
meu_conjunto = {1, 2, 3, 4}
meu_conjunto.discard(3)
print(meu_conjunto)  # Saída: {1, 2, 4}
```

Diferente do método `remove()`, o método `discard()` não gera uma exceção caso o elemento não exista no conjunto. Ele simplesmente não faz nada.
