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


fib = Fibonacci()
print(fib[10])
print(fib[5:15])
print(8 in fib)
print(len(fib))
