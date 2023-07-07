# `__new__` de uma metaclass cria e retorna a classe em si

Em Python, as metaclasses são classes especiais que permitem controlar o comportamento da criação de outras classes. Duas funções especiais que podem ser definidas em uma _metaclass_ são `__new__` e `__call__`.

A função `__new__` é chamada quando uma nova classe está sendo criada pela _metaclass_. Ela recebe vários argumentos, incluindo o nome da classe, uma tupla contendo as classes base, um dicionário contendo os atributos da classe e outros argumentos opcionais. A função `__new__` é responsável por criar e retornar a classe em si.

A função `__call__` é chamada quando a classe criada pela _metaclass_ é instanciada. Ela recebe a instância da classe, juntamente com quaisquer argumentos passados para a instanciação da classe. A função `__call__` permite personalizar o comportamento da instanciação da classe.

Aqui está um exemplo que demonstra o uso de `__new__` e `__call__` em uma _metaclass_ que cria uma classe personalizada e controla sua instanciação:

```python
class MinhaMetaclass(type):
    def __new__(cls, nome, bases, attrs):
        # Criar a classe
        nova_classe = super().__new__(cls, nome, bases, attrs)
        # Adicionar um novo atributo à classe
        nova_classe.novo_atributo = 42
        # Retornar a classe criada
        return nova_classe

    def __call__(cls, *args, **kwargs):
        # Instanciar a classe
        instancia = super().__call__(*args, **kwargs)
        # Realizar algum processamento adicional na instância
        instancia.processado = True
        # Retornar a instância
        return instancia


class MinhaClasse(metaclass=MinhaMetaclass):
    def __init__(self, valor):
        self.valor = valor


objeto = MinhaClasse(10)
print(objeto.valor)  # Saída: 10
print(objeto.novo_atributo)  # Saída: 42
print(objeto.processado)  # Saída: True
```

Nesse exemplo, a classe `MinhaMetaclass` é definida como uma _metaclass_ que personaliza a criação da classe `MinhaClasse`. No método `__new__`, um novo atributo chamado `novo_atributo` é adicionado à classe. No método `__call__`, a instância da classe é processada e um novo atributo chamado `processado` é adicionado à instância.

Ao criar uma instância da classe `MinhaClasse`, os métodos `__new__` e `__call__` da _metaclass_ são chamados automaticamente. O objeto resultante possui o atributo `valor` definido no construtor, o atributo `novo_atributo` adicionado pela _metaclass_ e o atributo `processado` adicionado durante a instanciação.
