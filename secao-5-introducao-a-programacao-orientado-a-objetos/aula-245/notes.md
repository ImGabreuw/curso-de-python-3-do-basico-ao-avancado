# Método especial `__call__`

O _dunder method_ `__call__`, em classes (exceto meta classes) faz a instância de uma classe **callable**.

_Callable_ e algo que pode ser executado com parênteses, por exemplo:

```python
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 2134


call1 = CallMe('23945876545')
retorno = call1('Luiz Otávio')
print(retorno)

# Saída: 
# Luiz Otávio está chamando 23945876545
# 213
```
