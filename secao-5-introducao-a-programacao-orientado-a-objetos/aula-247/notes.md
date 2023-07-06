# Teoria: metaclasses são o tipo das classes

Metaclasses em Python são classes cujas instâncias são classes. Em outras palavras, uma metaclasse é uma classe que define o comportamento e a estrutura de outras classes. É possível pensar nas metaclasses como "classes de classes".

As metaclasses são usadas principalmente para controlar o comportamento da criação de classes, permitindo adicionar lógica personalizada ao processo de criação e definição de classes. Isso inclui a capacidade de modificar atributos, adicionar métodos extras, restringir herança e muito mais.

Vejamos um exemplo para entender melhor como as metaclasses funcionam:

```python
class MetaClasseExemplo(type):
    def __new__(cls, name, bases, attrs):
        # Adiciona um prefixo aos atributos da classe
        prefixed_attrs = {}
        for attr_name, attr_value in attrs.items():
            prefixed_attrs[f"prefixed_{attr_name}"] = attr_value

        return super().__new__(cls, name, bases, prefixed_attrs)

class MinhaClasse(metaclass=MetaClasseExemplo):
    def __init__(self, valor):
        self.valor = valor

    def imprime_valor(self):
        print(self.valor)

objeto = MinhaClasse(42)
objeto.imprime_valor()
```

Neste exemplo, criamos uma metaclasse chamada `MetaClasseExemplo`. Essa metaclasse herda da classe `type`, que é a metaclasse base do Python. Em seguida, definimos o método `__new__` na metaclasse, que é chamado durante a criação de uma nova classe.

Dentro do método `__new__`, adicionamos um prefixo "prefixed\_" a todos os atributos da classe que está sendo criada. Em seguida, chamamos o método `__new__` da classe base usando `super()` para criar a classe.

A classe `MinhaClasse` é definida com a opção `metaclass=MetaClasseExemplo`, o que significa que a classe `MetaClasseExemplo` é usada como a metaclasse para criar a classe `MinhaClasse`.

Quando criamos uma instância de `MinhaClasse`, o método `__init__` é chamado e o valor é atribuído ao atributo `self.valor`. Em seguida, chamamos o método `imprime_valor`, que simplesmente imprime o valor.

A saída do exemplo será:

```
42
```

Como podemos ver, a metaclasse `MetaClasseExemplo` modificou o processo de criação da classe `MinhaClasse`, adicionando um prefixo "prefixed\_" aos seus atributos. Isso ilustra como as metaclasses podem ser usadas para controlar o comportamento da criação de classes e adicionar funcionalidades personalizadas.

O exemplo anterior usando uma metaclasse pode ser reproduzido usando a função embutida `type` do Python para criar a classe dinamicamente. A função `type` pode ser usada tanto para criar instâncias de classes como para criar classes em si.

Aqui está o exemplo anterior reescrito usando `type` para criar a classe `MinhaClasse`:

```python
def init(self, valor):
    self.valor = valor

def imprime_valor(self):
    print(self.valor)

MinhaClasse = type('MinhaClasse', (), {
    '__init__': init,
    'imprime_valor': imprime_valor
})

objeto = MinhaClasse(42)
objeto.imprime_valor()
```

Neste exemplo, em vez de definir a classe `MinhaClasse` usando a sintaxe de classe convencional, usamos a função `type` para criá-la. A função `type` recebe três argumentos:

1. O nome da classe: 'MinhaClasse'

2. Uma tupla de classes base (herança), no nosso caso, deixamos vazio com `()`

3. Um dicionário contendo os atributos e métodos da classe

No exemplo, definimos duas funções externas `init` e `imprime_valor`, que serão usadas como métodos da classe. Em seguida, chamamos a função `type` para criar a classe `MinhaClasse`. O resultado é atribuído à variável `MinhaClasse`.

Podemos então instanciar a classe `MinhaClasse`, assim como fizemos no exemplo anterior, e chamar o método `imprime_valor`. A saída será novamente:

```
42
```

Esse exemplo ilustra como a função `type` pode ser usada para criar classes dinamicamente em Python, sem a necessidade de usar uma metaclasse separada. A função `type` é poderosa e oferece flexibilidade para criar classes programaticamente. No entanto, o uso de metaclasse ainda pode ser útil em casos mais complexos, onde é necessário um controle mais avançado sobre o processo de criação de classes.

É importante mencionar que o uso de metaclasses é avançado e geralmente não é necessário em situações comuns. Elas são úteis em casos específicos onde você precisa de um controle granular sobre a criação de classes e deseja aplicar lógica personalizada durante esse processo.
