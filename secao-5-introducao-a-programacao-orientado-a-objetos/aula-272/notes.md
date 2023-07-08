# Criando sua própria lista com Iterable, Iterator e Sequence (collections.abc)

No Python, as interfaces `Iterable`, `Iterator` e `Sequence` são definidas no módulo `collections.abc` e fornecem uma estrutura para implementar objetos iteráveis e sequências personalizadas. Essas interfaces permitem que os objetos sejam iterados, percorridos e acessados usando métodos específicos.

Aqui estão as explicações e exemplos para cada uma dessas interfaces:

1. `Iterable`:
   A interface `Iterable` define o comportamento de objetos que podem ser iterados usando um loop `for`. Um objeto que implementa essa interface deve ter um método `__iter__()` que retorna um objeto `Iterator`.

   Exemplo:
   Vamos supor que temos uma classe `Range` que representa uma sequência numérica:

   ```python
   class Range:
       def __init__(self, start, end, step=1):
           self.start = start
           self.end = end
           self.step = step

       def __iter__(self):
           current = self.start
           while current < self.end:
               yield current
               current += self.step
   ```

   Nesse exemplo, a classe `Range` implementa a interface `Iterable` ao definir o método `__iter__()`. Esse método retorna um gerador que produz os valores da sequência numérica.

   Agora podemos iterar sobre instâncias de `Range` usando um loop `for`:

   ```python
   numbers = Range(1, 10, 2)
   for num in numbers:
       print(num)
   ```

   A saída será:

   ```
   1
   3
   5
   7
   9
   ```

2. `Iterator`:
   A interface `Iterator` define o comportamento de um objeto que pode ser iterado e fornece um valor de cada vez. Um objeto que implementa essa interface deve ter os métodos `__iter__()` e `__next__()`.

   Exemplo:
   Vamos supor que temos uma classe `Squares` que gera os quadrados dos números em um intervalo:

   ```python
   class Squares:
       def __init__(self, start, end):
           self.start = start
           self.end = end

       def __iter__(self):
           return self

       def __next__(self):
           if self.start >= self.end:
               raise StopIteration
           square = self.start ** 2
           self.start += 1
           return square
   ```

   Nesse exemplo, a classe `Squares` implementa a interface `Iterator` ao definir os métodos `__iter__()` e `__next__()`. O método `__iter__()` retorna o próprio objeto, e o método `__next__()` gera o próximo valor na sequência de quadrados.

   Agora podemos iterar sobre instâncias de `Squares` usando um loop `for` ou chamando a função `next()` explicitamente:

   ```python
   squares = Squares(1, 5)
   for square in squares:
       print(square)
   ```

   A saída será:

   ```
   1
   4
   9
   16
   ```

3. `Sequence`:
   A interface `Sequence` define o comportamento de objetos que representam uma sequência de elementos ordenados. Essa interface herda de `Iterable` e define métodos adicionais para suportar a indexação, verificação de pertencimento, fatiamento e outras operações comuns.

   Exemplo:
   Vamos supor que queremos criar uma sequência personalizada chamada `Fibonacci` que gera a sequência de Fibonacci:

   ```python
   from collections.abc import Sequence

   class Fibonacci(Sequence):
       def __getitem__(self, index):
           if isinstance(index, slice):
               start = index.start or 0
               stop = index.stop or float('inf')
               step = index.step or 1
               return [self._fib(n) for n in range(start, stop, step)]
           elif isinstance(index, int):
               return self._fib(index)
           else:
               raise TypeError('Invalid index type')

       def __len__(self):
           raise NotImplementedError('Length not implemented')

       def _fib(self, n):
           if n == 0:
               return 0
           elif n == 1:
               return 1
           else:
               return self._fib(n - 1) + self._fib(n - 2)
   ```

   Nesse exemplo, a classe `Fibonacci` implementa a interface `Sequence` ao definir os métodos `__getitem__()` e `__len__()`. O método `__getitem__()` permite acessar um elemento individual ou realizar fatiamento, retornando os valores correspondentes da sequência de Fibonacci.

   Agora podemos acessar elementos ou fatias da sequência de Fibonacci usando a indexação:

   ```python
   fib = Fibonacci()
   print(fib[10])              # Saída: 55
   print(fib[5:15])            # Saída: [5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
   print(8 in fib)             # Saída: True
   print(len(fib))             # Saída: NotImplementedError: Length not implemented
   ```

   Observe que o método `__len__()` ainda não está implementado na classe `Fibonacci`, pois calcular o comprimento da sequência de Fibonacci é uma tarefa complexa. No entanto, o restante das operações da sequência, como indexação e fatiamento, está funcionando corretamente.

Implementar as interfaces `Iterable`, `Iterator` e `Sequence` permite que você crie objetos personalizados que podem ser iterados, indexados e usados em operações comuns, proporcionando uma maior flexibilidade no design de suas próprias estruturas de dados.
