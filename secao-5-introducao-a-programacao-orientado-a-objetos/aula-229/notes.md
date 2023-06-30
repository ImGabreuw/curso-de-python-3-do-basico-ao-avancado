# Classes abstratas - Abstract Base Class (abc) - Python Orientado a Objetos

Classes abstratas são classes que não podem ser instanciadas diretamente, mas servem como uma base para outras classes que as herdam. Em Python, a biblioteca `abc` (Abstract Base Classes) fornece duas maneira de definir classes abstratas:

1. Usando a metaclasse `ABCMeta`

  ```python
  from abc import ABCMeta, abstractmethod

  class Animal(metaclass=ABCMeta):
    @abstractmethod
    def sound(self):
        pass
  ```

2. Herdar da classe `ABC`.

  ```python
  from abc import ABC, abstractmethod

  class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
  ```

> **IMPORTANTE**: para o Python reconhecer um classe como abstrata, é necessário herdar de `ABC` e ter pelo menos 1 método abstrato, ou seja, decorado com `@abstractmethod`

Para criar uma classe abstrata com `abc`, você precisa importar a biblioteca `abc` e usar a função `abstractmethod` para marcar os métodos que devem ser implementados pelas subclasses. Vejamos um exemplo:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

    def move(self):
        return "Running"

class Cat(Animal):
    def sound(self):
        return "Meow!"

    def move(self):
        return "Jumping"

# Não é possível instanciar a classe abstrata Animal
# animal = Animal()  # Isso resultará em um TypeError

# Podemos criar instâncias das subclasses
dog = Dog()
cat = Cat()

print(dog.sound())  # Saída: Woof!
print(dog.move())   # Saída: Running

print(cat.sound())  # Saída: Meow!
print(cat.move())   # Saída: Jumping
```

Nesse exemplo, temos a classe abstrata `Animal`, que define dois métodos abstratos: `sound()` e `move()`. Esses métodos são marcados como abstratos usando o decorador `abstractmethod`. As subclasses `Dog` e `Cat` herdam da classe `Animal` e implementam os métodos abstratos.

Ao tentar instanciar a classe abstrata `Animal`, um `TypeError` será gerado, pois não é possível criar instâncias de classes abstratas. No entanto, podemos criar instâncias das subclasses `Dog` e `Cat`, e elas implementarão os métodos abstratos conforme necessário.

O uso de classes abstratas e `abc` em Python permite definir uma estrutura comum para várias classes relacionadas, garantindo que métodos específicos sejam implementados nas subclasses. Isso ajuda a estabelecer um contrato entre a classe abstrata e suas subclasses, tornando o código mais previsível e robusto.