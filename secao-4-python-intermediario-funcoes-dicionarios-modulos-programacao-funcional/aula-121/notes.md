# (Parte 1) Métodos úteis nos dicionários Python (dict)

> ## **Dunder method**

Dunder (Double underscore) methods, também conhecidos como "métodos mágicos" ou "métodos especiais", são métodos predefinidos em Python que possuem um nome especial começando e terminando com dois underscores. Esses métodos permitem que você defina o comportamento específico de objetos em relação a operações comuns, como adição, subtração, iteração, comparação, entre outros.

Os _dunder methods_ são chamados automaticamente pelo interpretador Python em certas situações, quando certas operações são realizadas em objetos. Eles permitem que você adicione funcionalidades especiais às suas classes, tornando-as mais intuitivas e poderosas.

Por exemplo, o método `__init__` é um _dunder method_ especial que é chamado automaticamente quando um objeto é criado a partir de uma classe. Ele é usado para inicializar os atributos do objeto.

Aqui está um exemplo de uma classe `Ponto` com o método `__init__`:

```python
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

Ao criar um objeto `p` da classe `Ponto`:

```python
p = Ponto(2, 3)
```

O método `__init__` é chamado automaticamente, passando os argumentos `2` e `3` para `x` e `y`, respectivamente. Isso inicializa os atributos `x` e `y` do objeto `p`.

Existem muitos outros _dunder methods_ em Python, como `__str__`, que retorna uma representação em string do objeto, `__add__` para definir a adição entre objetos, `__len__` para retornar o tamanho do objeto, entre outros. Esses métodos permitem que você personalize o comportamento dos objetos em relação às operações comuns da linguagem.

Usando _dunder methods_, você pode criar classes que se comportam de maneira semelhante aos tipos de dados embutidos em Python, como listas, strings e dicionários, permitindo uma maior flexibilidade e expressividade na programação.

> ## **Métodos úteis do dicionário**

### **OBS**

Caso em um dicionário tenha 2 ou + chaves com o mesmo valor, o último será utilizado, uma vez que o Python sobrescreve os valores anteriores.

```python
pessoa = {
  "nome": "Luiz Otávio",
  "sobrenome": "Miranda 1",
  "sobrenome": "Miranda 2",
  "sobrenome": "Miranda 3",
}

print(pessoa["sobrenome"]) # Miranda 3
```

### **Método: `len()`**

O método `len( [dicionário] )` retorna o número de itens (pares de chave-valor) no dicionário. Ele pode ser usado para determinar o tamanho do dicionário. Aqui está um exemplo:

```python
meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
tamanho = len(meu_dicionario)
print(tamanho)  # Saída: 3
```

### **Método: `dicionario.keys()`**

O método `keys()` retorna uma lista com todas as chaves presentes no dicionário. Isso pode ser útil quando você precisa iterar apenas pelas chaves do dicionário. Aqui está um exemplo:

```python
meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
chaves = meu_dicionario.keys()
print(chaves)  # Saída: dict_keys(['chave1', 'chave2', 'chave3'])
```

### **Método: `dicionario.values()`**

O método `values()` retorna uma lista com todos os valores presentes no dicionário. Isso pode ser útil quando você precisa iterar apenas pelos valores do dicionário. Aqui está um exemplo:

```python
meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
valores = meu_dicionario.values()
print(valores)  # Saída: dict_values(['valor1', 'valor2', 'valor3'])
```

### **Método: `dicionario.items()`**

O método `items()` retorna uma lista de tuplas, em que cada tupla contém uma chave e seu respectivo valor. Isso pode ser útil quando você precisa iterar tanto pelas chaves quanto pelos valores do dicionário. Aqui está um exemplo:

```python
meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
itens = meu_dicionario.items()
print(itens)  # Saída: dict_items([('chave1', 'valor1'), ('chave2', 'valor2'), ('chave3', 'valor3')])
```

### **Método: `dicionario.setdefault()`**

O método `setdefault( [chave], [valor_padrao] )` retorna o valor associado à chave especificada. Se a chave não estiver presente no dicionário, o método insere a chave com o valor padrão fornecido e retorna esse valor. Isso pode ser útil quando você precisa definir um valor padrão para uma chave que ainda não existe. Aqui está um exemplo:

```python
meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
valor = meu_dicionario.setdefault('chave3', 'valor_padrao')
print(valor)  # Saída: valor_padrao
print(meu_dicionario)  # Saída: {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor_padrao'}
```
