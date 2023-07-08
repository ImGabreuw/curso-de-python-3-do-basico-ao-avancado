# namedtuple - tuplas imutáveis com nomes para valores

Em Python, `namedtuple` é uma função da biblioteca padrão que permite criar tuplas nomeadas. Uma tupla nomeada é semelhante a uma tupla regular, mas cada elemento possui um nome atribuído, o que facilita o acesso aos valores da tupla usando nomes em vez de índices.

As tuplas nomeadas são imutáveis, assim como as tuplas regulares, mas oferecem a vantagem de ter nomes atribuídos a cada elemento, tornando o código mais legível e autodocumentado.

> **OBS**: elas podem substituir data classes que não possuem métodos, apenas atributos.

Aqui está um exemplo para ilustrar o uso de `namedtuple`:

```python
from collections import namedtuple

# Definindo uma namedtuple para representar informações sobre uma pessoa
Person = namedtuple('Person', ['name', 'age', 'gender'])

# Criando uma instância de Person
person1 = Person('John Doe', 25, 'male')

# Acessando os valores da instância usando os nomes atribuídos
print(person1.name)   # Saída: John Doe
print(person1.age)    # Saída: 25
print(person1.gender) # Saída: male
```

Nesse exemplo, definimos uma tupla nomeada chamada `Person` usando a função `namedtuple`. Passamos o nome "Person" como primeiro argumento e, em seguida, fornecemos uma lista de strings que representam os nomes atribuídos a cada elemento da tupla.

Em seguida, criamos uma instância da tupla nomeada `Person` chamada `person1` e atribuímos valores a cada elemento. Podemos acessar os valores da tupla usando os nomes atribuídos aos elementos, como `person1.name`, `person1.age` e `person1.gender`.

Uma das principais vantagens das tuplas nomeadas é que elas podem ser mais descritivas do que as tuplas regulares, pois os nomes atribuídos a cada elemento fornecem contexto sobre o que cada valor representa. Isso torna o código mais legível e menos propenso a erros causados por confusão de índices.

As tuplas nomeadas também herdam todas as funcionalidades das tuplas regulares, como iteração, descompactação, comparação, entre outras. Além disso, elas são imutáveis, o que significa que os valores atribuídos aos elementos não podem ser alterados após a criação da tupla.

Em Python, a tupla nomeada (`namedtuple`) possui alguns atributos especiais, como `_fields` e `_defaults`, que fornecem informações sobre os campos da tupla nomeada e seus valores padrão, respectivamente.

O atributo `_fields` é uma tupla contendo os nomes dos campos da tupla nomeada. Ele permite acessar os nomes dos campos de forma programática e iterar sobre eles.

O atributo `_defaults` é um atributo opcional que armazena os valores padrão dos campos da tupla nomeada. Ele é útil quando você deseja definir valores padrão para alguns ou todos os campos, permitindo que você crie instâncias da tupla nomeada sem fornecer um valor para cada campo.

Aqui está um exemplo que mostra o uso de `_fields`, `_defaults` e como criar uma tupla nomeada com valores padrão:

```python
from collections import namedtuple

# Definindo uma tupla nomeada para representar um ponto em um plano 2D
Point = namedtuple('Point', ['x', 'y'], defaults=[0, 0])

# Criando uma instância da tupla nomeada Point sem fornecer valores
point1 = Point()

# Criando uma instância da tupla nomeada Point fornecendo apenas um valor
point2 = Point(2)

# Criando uma instância da tupla nomeada Point fornecendo valores para todos os campos
point3 = Point(3, 4)

# Acessando os valores da instância
print(point1)  # Saída: Point(x=0, y=0)
print(point2)  # Saída: Point(x=2, y=0)
print(point3)  # Saída: Point(x=3, y=4)

# Acessando os nomes dos campos
print(point1._fields)  # Saída: ('x', 'y')
print(point2._fields)  # Saída: ('x', 'y')
print(point3._fields)  # Saída: ('x', 'y')

# Acessando os valores padrão dos campos
print(point1._defaults)  # Saída: (0, 0)
print(point2._defaults)  # Saída: (0, 0)
print(point3._defaults)  # Saída: (0, 0)
```

Nesse exemplo, definimos uma tupla nomeada chamada `Point` que representa um ponto em um plano 2D. Os campos da tupla nomeada são `'x'` e `'y'`. Além disso, fornecemos `[0, 0]` como valores padrão para os campos usando o parâmetro `defaults` da função `namedtuple`.

Em seguida, criamos três instâncias da tupla nomeada `Point`. A primeira instância, `point1`, é criada sem fornecer nenhum valor, o que significa que os valores padrão são usados. A segunda instância, `point2`, é criada fornecendo apenas um valor para o campo `'x'`. A terceira instância, `point3`, é criada fornecendo valores para ambos os campos.

Podemos acessar os valores das instâncias da tupla nomeada usando a sintaxe usual, como `point1.x`, `point2.y`, etc.

Além disso, podemos acessar os nomes dos campos usando o atributo `_fields`. Isso é útil quando você precisa iterar ou trabalhar com os campos de forma programática.

O atributo `_defaults` retorna uma tupla contendo os valores padrão dos campos. No exemplo acima, todos os campos têm os mesmos valores padrão `[0, 0]`.

Dessa forma, o uso de `_fields` e `_defaults` permite criar tuplas nomeadas com valores padrão, simplificando a criação de instâncias quando alguns campos têm valores fixos.

Em Python, a classe `NamedTuple` do módulo `typing` permite criar tuplas nomeadas com valores padrão. Ela é uma alternativa tipada à `namedtuple` da biblioteca padrão e fornece suporte para anotações de tipo.

A classe `NamedTuple` é uma subclasse genérica que permite definir tuplas nomeadas com campos e tipos específicos, bem como valores padrão para esses campos.

Aqui está um exemplo do mundo real que mostra como usar `NamedTuple` com valores padrão:

```python
from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int = 0
    gender: str = 'unknown'

# Criando instâncias da tupla nomeada Person
person1 = Person('John Doe')
person2 = Person('Jane Smith', age=30)
person3 = Person('Mike Johnson', age=45, gender='male')

# Acessando os valores das instâncias
print(person1)  # Saída: Person(name='John Doe', age=0, gender='unknown')
print(person2)  # Saída: Person(name='Jane Smith', age=30, gender='unknown')
print(person3)  # Saída: Person(name='Mike Johnson', age=45, gender='male')
```

Nesse exemplo, definimos uma classe `Person` como uma subclasse de `NamedTuple`. Os campos da tupla nomeada são definidos como atributos de classe com suas anotações de tipo correspondentes.

Definimos valores padrão para os campos `age` e `gender`. O campo `age` tem um valor padrão de `0`, enquanto o campo `gender` tem um valor padrão de `'unknown'`.

Em seguida, criamos instâncias da tupla nomeada `Person` usando a sintaxe de inicialização da classe. Podemos fornecer valores apenas para os campos que desejamos e deixar os campos com valores padrão para usar seus valores predefinidos.

Podemos acessar os valores das instâncias da tupla nomeada como atributos de instância, como `person1.name`, `person2.age`, etc.

A classe `NamedTuple` fornece as mesmas funcionalidades das tuplas nomeadas da biblioteca padrão, como imutabilidade, iteração, descompactação e comparação.

Usar `NamedTuple` com valores padrão permite criar instâncias com facilidade, especificando apenas os campos necessários e deixando os campos com valores padrão para terem seus valores predefinidos. Isso simplifica a criação de instâncias, especialmente quando você precisa lidar com muitos campos opcionais ou valores predefinidos.