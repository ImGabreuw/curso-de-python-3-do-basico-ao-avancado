# (Parte 2) Métodos úteis nos dicionários Python (dict)

Claro! Vou explicar cada um dos métodos adicionais do dicionário em Python e fornecer exemplos para ilustrar seu uso.

### **Método: `dicionario.copy()`**

O método `copy()` cria uma cópia superficial (shallow copy) do dicionário. A cópia resultante contém os mesmos pares de chave-valor, mas é um objeto separado. Aqui está um exemplo:

```python
meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
copia_dicionario = meu_dicionario.copy()
print(copia_dicionario)  # Saída: {'chave1': 'valor1', 'chave2': 'valor2'}
```

### **Método: `dicionario.get()`**
O método `get( [chave], [valor padrão] )` retorna o valor associado à chave especificada. Se a chave estiver presente no dicionário, o método retorna o valor correspondente. Caso contrário, ele retorna o valor padrão fornecido. Isso pode ser útil quando você deseja evitar um erro de chave inexistente. Aqui está um exemplo:

```python
meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
valor = meu_dicionario.get('chave3', 'valor_padrao')
print(valor)  # Saída: valor_padrao
```

### **Método: `dicionario.pop()`**

O método `pop( [chave], [valor padrão] )` remove e retorna o valor associado à chave especificada. Se a chave estiver presente no dicionário, o método a remove e retorna o valor correspondente. Caso contrário, ele retorna o valor padrão fornecido. Isso pode ser útil quando você deseja remover um item específico do dicionário. Aqui está um exemplo:

```python
meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
valor = meu_dicionario.pop('chave1', 'valor_padrao')
print(valor)  # Saída: valor1
print(meu_dicionario)  # Saída: {'chave2': 'valor2'}
```

### **Método: `dicionario.popitem()`**

O método `popitem()` remove e retorna um par chave-valor aleatório do dicionário como uma tupla. Isso pode ser útil quando você precisa remover um item do dicionário, mas não se importa em qual item será removido. Aqui está um exemplo:

```python
meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
par = meu_dicionario.popitem()
print(par)  # Saída: ('chave3', 'valor3')
print(meu_dicionario)  # Saída: {'chave1': 'valor1', 'chave2': 'valor2'}
```

### **Método: `dicionario.update()`**

O método `update( [outro dicionário] )` atualiza o dicionário com os pares de chave-valor de outro dicionário ou de uma sequência de pares chave-valor. Isso pode ser útil quando você deseja adicionar ou substituir vários itens no dicionário. Aqui está um exemplo:

```python
meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
outro_dicionario = {'chave3': 'valor3', 'chave4': 'valor4'}
meu_dicionario.update(outro_dicionario)
print(meu_dicionario)  # Saída: {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3', 'chave4': 'valor4'}
```