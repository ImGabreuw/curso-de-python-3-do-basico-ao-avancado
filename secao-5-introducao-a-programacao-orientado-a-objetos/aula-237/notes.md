# Python Dunder Methods **repr** e **str**

Em Python, os dunder methods `__repr__` e `__str__` são usados para fornecer representações em string de um objeto. Esses métodos são chamados automaticamente quando você usa as funções `repr()` e `str()` em um objeto, respectivamente. Eles permitem que você defina como um objeto deve ser representado em uma forma legível para humanos ou para uso em depuração.

O método `__repr__(self)` retorna uma representação em string "oficial" do objeto. Essa representação deve ser uma expressão Python válida que pode ser usada para recriar o objeto. É comum que o método `__repr__` seja implementado de forma que ao copiar a representação em string retornada e avaliá-la com `eval()`, o objeto original seja recriado. O objetivo do `__repr__` é fornecer uma representação precisa do objeto que possa ser usada para depuração e inspeção.

O método `__str__(self)` retorna uma representação em string mais legível para humanos do objeto. É usado para fornecer uma descrição amigável do objeto em um formato compreensível. Normalmente, `__str__` é implementado para retornar informações mais simplificadas e amigáveis, omitindo detalhes desnecessários.

Aqui está um exemplo que ilustra a diferença entre `__repr__` e `__str__`:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name!r}', {self.age!r})"

    def __str__(self):
        return f"Person: {self.name}, {self.age} years old"


person = Person("Alice", 30)

print(repr(person))  # Saída: Person('Alice', 30)
print(str(person))   # Saída: Person: Alice, 30 years old
```

> **OBS**: é recomendado forçar a representação técnica com `!r` de um valor no método `__repr__`, pois isso pode evitar ambiguidades na representação, por exemplo, de strings.

No exemplo acima, a classe `Person` implementa os métodos `__repr__` e `__str__`. O método `__repr__` retorna uma representação Python válida do objeto `Person`, permitindo sua recriação. O método `__str__` retorna uma descrição mais legível para humanos do objeto `Person`, fornecendo detalhes como o nome e a idade.

Ao usar a função `repr()` no objeto `person`, a representação retornada é `Person('Alice', 30)`. Por outro lado, a função `str()` retorna a string `Person: Alice, 30 years old`. A diferença entre as duas representações é que `repr()` fornece uma representação mais técnica e precisa, enquanto `str()` oferece uma descrição mais amigável para os usuários finais.

É importante observar que, se o método `__str__` não estiver definido, o Python usará o método `__repr__` como um _fallback_. Portanto, é comum implementar pelo menos o método `__repr__` em suas classes para garantir que haja uma representação adequada do objeto.

Os dunder methods `__repr__` e `__str__` são úteis para fornecer informações e descrições adequadas sobre seus objetos, tornando-os mais legíveis e compreensíveis. Eles são amplamente utilizados para fins de depuração, exibição de informações para usuários e em situações em que é necessário controlar a forma como o objeto é representado em string.
