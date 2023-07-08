# Valores padrão, field e fields em dataclasses

Nas dataclasses é possível ter valores padrão apenas para tipos imutáveis como `int`, `float`, `str` e `bool`.

```python
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str = "Missing"
    sobrenome: str = "Missing"
    idade: int = 100


if __name__ == "__main__":
    p = Pessoa()
    print(p)

    # Saída: Pessoa(nome='Missing', sobrenome='Missing', idade=100)
```

```python
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str = "Missing"
    sobrenome: str = "Missing"
    idade: int = 100
    enderecos: list[str] = []


if __name__ == "__main__":
    p = Pessoa()
    print(p)
```

Saída:

```
Traceback (most recent call last):
  File "/home/gabriel/Projects/curso-de-python-3-do-basico-ao-avancado/secao-5-introducao-a-programacao-orientado-a-objetos/aula-270/example_2.py", line 5, in <module>
    class Pessoa:
  File "/home/gabriel/.asdf/installs/python/anaconda3-2023.03/lib/python3.10/dataclasses.py", line 1184, in dataclass
    return wrap(cls)
  File "/home/gabriel/.asdf/installs/python/anaconda3-2023.03/lib/python3.10/dataclasses.py", line 1175, in wrap
    return _process_class(cls, init, repr, eq, order, unsafe_hash,
  File "/home/gabriel/.asdf/installs/python/anaconda3-2023.03/lib/python3.10/dataclasses.py", line 955, in _process_class
    cls_fields.append(_get_field(cls, name, type, kw_only))
  File "/home/gabriel/.asdf/installs/python/anaconda3-2023.03/lib/python3.10/dataclasses.py", line 812, in _get_field
    raise ValueError(f'mutable default {type(f.default)} for field '
ValueError: mutable default <class 'list'> for field enderecos is not allowed: use default_factory
```

Para valores imutáveis não pode usar a mesma abordagem, pois como já foi visto anteriormente, valores padrão para tipos mutáveis são passados por referência, logo caso o atributo `enderecos` de `Pessoa` seja alterado em uma instância, todas as outras seriam afetadas.

Em Python, uma dataclass é uma classe que facilita a criação de classes simples de valor, fornecendo automaticamente a implementação de métodos como `__init__`, `__repr__` e outros métodos especiais. As anotações de tipo podem ser usadas nas variáveis da classe para indicar o tipo de dado esperado.

Em uma dataclass, o atributo `field` é usado para especificar como cada campo da classe deve ser tratado. O `field` é usado como um decorador que permite definir metadados e comportamentos específicos para cada campo da classe. Ele pode ser usado para definir anotações de tipo, fornecer valores padrão, especificar como os campos são serializados ou deserializados, entre outras configurações.

O atributo `fields` em uma dataclass é uma variável de classe pré-definida que contém uma lista de todas as instâncias de campo presentes na classe. Essa lista pode ser usada para acessar e manipular os campos individualmente.

Aqui está um exemplo que ilustra o uso de `field` e `fields` em uma dataclass:

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    email: str = field(default='', metadata={'required': True})

    def validate(self):
        if self.email == '':
            raise ValueError('Email is required')
```

Nesse exemplo, temos uma classe `Person` que representa informações pessoais de uma pessoa. Ela possui três campos: `name`, `age` e `email`. O campo `email` é opcional, mas possui um metadado `required` que indica que ele é obrigatório. Além disso, o campo `email` possui um valor padrão definido como uma string vazia.

A classe também possui um método `validate` que verifica se o campo `email` está preenchido. Se o campo estiver vazio, o método lança uma exceção `ValueError`.

Agora, vamos criar uma instância da classe `Person` e acessar seus campos usando `fields`:

```python
person = Person('John Doe', 25)
print(fields(person))
```

A saída será:

```
(Field(name='name',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object at 0x7f6015f8e4e0>,default_factory=<dataclasses._MISSING_TYPE object at 0x7f6015f8e4e0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({'required': True}))),
(Field(name='age',type=<class 'int'>,default=<dataclasses._MISSING_TYPE object at 0x7f6015f8e4e0>,default_factory=<dataclasses._MISSING_TYPE object at 0x7f6015f8e4e0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}))),
(Field(name='email',type=<class 'str'>,default='',default_factory=<dataclasses._MISSING_TYPE object at 0x7f6015f8e4e0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({'required': True}))))
```

A função `fields` retorna uma lista de objetos `Field` que representam cada campo da classe `Person`. Cada objeto `Field` contém informações como o nome do campo, o tipo, o valor padrão, se o campo é inicializável, se deve ser incluído na representação da classe, metadados adicionais, entre outros.

Assim, o uso de `field` e `fields` em uma dataclass oferece uma maneira flexível de definir e acessar os campos da classe, adicionando metadados e comportamentos personalizados, conforme necessário.
