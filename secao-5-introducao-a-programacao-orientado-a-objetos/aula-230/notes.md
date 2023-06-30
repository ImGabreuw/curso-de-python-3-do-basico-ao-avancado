# abstractmethod para qualquer método já decorado (property e setter)

O decorador `abstractmethod` em Python é comumente usado para marcar métodos abstratos em classes abstratas, como mencionado anteriormente. No entanto, ele também pode ser usado em métodos decorados como `property` e `setter`, mas para que isso funcione é necessário usar `@abstractmethod` como o decorador mais interno.

Vamos considerar um exemplo no mundo real usando uma classe `Shape` abstrata com métodos decorados `property` e `setter` para calcular e modificar propriedades geométricas de diferentes formas. Neste exemplo, vamos implementar as classes `Rectangle` e `Circle` que herdam de `Shape`.

```python
from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    @perimeter.setter
    @abstractmethod
    def perimeter(self, value):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

    @perimeter.setter
    def perimeter(self, value):
        self._width = value / 2
        self._height = value / 2

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius * self._radius

    @property
    def perimeter(self):
        return 2 * 3.14 * self._radius

    @perimeter.setter
    def perimeter(self, value):
        self._radius = value / (2 * 3.14)

# Tentando instanciar a classe abstrata Shape
# shape = Shape()  # Isso resultará em um TypeError

# Criando instâncias das subclasses Rectangle e Circle
rectangle = Rectangle(4, 5)
circle = Circle(3)

print(rectangle.area)      # Saída: 20
print(rectangle.perimeter) # Saída: 18

print(circle.area)         # Saída: 28.26
print(circle.perimeter)    # Saída: 18.84

rectangle.perimeter = 12
print(rectangle.area)      # Saída: 36
print(rectangle.perimeter) # Saída: 12

circle.perimeter = 12
print(circle.area)         # Saída: 113.04
print(circle.perimeter)    # Saída: 12
```

Neste exemplo, a classe `Shape` é uma classe abstrata que define propriedades geométricas com os métodos decorados `property`. A propriedade `area` calcula a área da forma e a propriedade `perimeter` calcula o perímetro.

As subclasses `Rectangle` e `Circle` herdam da classe `Shape` e implementam as propriedades `area` e `perimeter` conforme necessário para retângulos e círculos. O método decorado `@property` permite acessar essas propriedades como se fossem atributos da classe.

Além disso, a classe `Rectangle` implementa um método `perimeter.setter` para modificar a largura e a altura do retângulo com base no perímetro fornecido.

O mesmo é feito na classe `Circle`, onde o método `perimeter.setter` permite modificar o raio do círculo com base no perímetro fornecido.

Observe que a classe abstrata `Shape` não pode ser instanciada diretamente. Tentar criar uma instância resultará em um `TypeError`. No entanto, é possível criar instâncias das subclasses `Rectangle` e `Circle` e acessar suas propriedades `area` e `perimeter` normalmente.

Esse exemplo demonstra como é possível usar o decorador `abstractmethod` em métodos decorados como `property` e `setter` para garantir que eles sejam implementados corretamente nas subclasses. Isso proporciona uma estrutura consistente e flexível para a manipulação de propriedades geométricas em diferentes formas.
