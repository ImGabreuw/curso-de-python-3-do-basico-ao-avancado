# python Special Methods, Magic Methods ou Dunder Methods

Em Python, os "Dunder Methods" (também conhecidos como "Magic Methods" ou "Special Methods") são métodos especiais que começam e terminam com duplo sublinhado (_dunder_). Eles permitem que você personalize o comportamento de objetos em relação a operações internas, como atribuição, comparação, chamadas de função, iteração, entre outros. Esses métodos são chamados automaticamente quando certas operações são executadas em objetos e, ao implementá-los, você pode controlar o comportamento dessas operações para seus próprios tipos de dados personalizados.

> Para mais informações sobre os dunder methods do Python, acesse o seguinte [artigo](https://rszalski.github.io/magicmethods/)

Aqui estão alguns exemplos de special methods mais comuns:

1. `__init__(self, ...)` - O construtor da classe, chamado automaticamente quando um novo objeto é criado.

2. `__str__(self)` - Retorna uma representação em string do objeto, usada quando você chama a função `str(obj)`.

3. `__repr__(self)` - Retorna uma representação em string "oficial" do objeto, usada quando você chama a função `repr(obj)`.

4. `__add__(self, other)` - Define o comportamento da adição do objeto com outro objeto (`self + other`).

5. `__sub__(self, other)` - Define o comportamento da subtração do objeto com outro objeto (`self - other`).

6. `__eq__(self, other)` - Define o comportamento de igualdade do objeto com outro objeto (`self == other`).

7. `__lt__(self, other)` - Define o comportamento de menor que do objeto em relação a outro objeto (`self < other`).

8. `__len__(self)` - Retorna o tamanho do objeto, usado quando você chama a função `len(obj)`.

9. `__call__(self, ...)` - Permite que o objeto seja chamado como uma função (`obj(...)`).

Exemplo:

```python
class MyNumber:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyNumber({self.value})"

    def __repr__(self):
        return f"MyNumber({self.value})"

    def __add__(self, other):
        return MyNumber(self.value + other.value)

    def __eq__(self, other):
        return self.value == other.value


num1 = MyNumber(5)
num2 = MyNumber(10)

# Usando __str__ e __repr__
print(str(num1))   # Saída: MyNumber(5)
print(repr(num1))  # Saída: MyNumber(5)

# Usando __add__
result = num1 + num2
print(result)  # Saída: MyNumber(15)

# Usando __eq__
print(num1 == num2)  # Saída: False

# Usando __len__ (gera TypeError, pois o método não está implementado)
# print(len(num1))
```

Neste exemplo, temos uma classe `MyNumber` que implementa alguns special methods. O método `__str__` é usado para fornecer uma representação legível em string do objeto, enquanto `__repr__` é usado para fornecer uma representação oficial em string. O método `__add__` é usado para definir o comportamento da adição entre objetos `MyNumber`. O método `__eq__` é usado para definir o comportamento de igualdade entre objetos `MyNumber`.

Os special methods permitem que você torne suas classes mais poderosas e integradas

com a sintaxe e as operações internas do Python. Eles desempenham um papel fundamental na criação de classes personalizadas que se comportam como tipos de dados nativos e podem ser usadas de forma intuitiva em expressões e operações comuns.
