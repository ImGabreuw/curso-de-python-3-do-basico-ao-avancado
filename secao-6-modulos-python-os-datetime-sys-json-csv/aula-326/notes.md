# (Parte 3) Threads - Executando processamentos em paralelo

Um problema comum ao trabalhar com threads é quando mais de 1 thread tentam alterar o mesmo valor. Veja um exemplo disso:

```python
class Ingressos:
    """
    Classe que vende ingressos
    """

    def __init__(self, estoque: int):
        """ Inicializando...

        :param estoque: quantidade de ingressos em estoque
        """
        self.estoque = estoque

    def comprar(self, quantidade: int):
        """
        Compra determinada quantidade de ingressos

        :param quantidade: A quantidade de ingressos que deseja comprar
        :type quantidade: int
        :return: Nada
        :rtype: None
        """
        # Tranca o método
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            # Libera o método
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} em estoque.')

        # Libera o método
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 10):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
```

Saída:

```console
Você comprou 2 ingresso(s). Ainda temos 8 em estoque.
Você comprou 5 ingresso(s). Ainda temos 3 em estoque.
Você comprou 1 ingresso(s). Ainda temos 2 em estoque.
Você comprou 4 ingresso(s). Ainda temos -2 em estoque.
Você comprou 3 ingresso(s). Ainda temos -5 em estoque.
Você comprou 6 ingresso(s). Ainda temos -11 em estoque.
Você comprou 7 ingresso(s). Ainda temos -18 em estoque.
Você comprou 9 ingresso(s). Ainda temos -27 em estoque.
Você comprou 8 ingresso(s). Ainda temos -35 em estoque
```

Como pode-se observar, esse não era o comportamento esperado, uma vez que a validação da quantidade de ingressos no estoque aparentemente não está sendo feito (mas na verdade está).

Uma forma de resolver esse problema é utilizar a classe `Lock` do módulo `threading`:

```python
class Ingressos:
    """
    Classe que vende ingressos
    """

    def __init__(self, estoque: int):
        """ Inicializando...

        :param estoque: quantidade de ingressos em estoque
        """
        self.estoque = estoque
        # Nosso cadeado
        self.lock = Lock()

    def comprar(self, quantidade: int):
        """
        Compra determinada quantidade de ingressos

        :param quantidade: A quantidade de ingressos que deseja comprar
        :type quantidade: int
        :return: Nada
        :rtype: None
        """
        # Tranca o método
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')

            # Libera o método
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} em estoque.')

        # Libera o método
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 10):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
```

Saída:

```console
Você comprou 1 ingresso(s). Ainda temos 9 em estoque.
Você comprou 2 ingresso(s). Ainda temos 7 em estoque.
Você comprou 3 ingresso(s). Ainda temos 4 em estoque.
Você comprou 4 ingresso(s). Ainda temos 0 em estoque.
Não temos ingressos suficientes.
Não temos ingressos suficientes.
Não temos ingressos suficientes.
Não temos ingressos suficientes.
Não temos ingressos suficientes.
```

Dessa forma, utilizamos `lock.acquire()` para trancar um thread até que a anterior seja concluída. Então, após a execução de todo o trecho de código na thread secundário, liberamos a execução da próxima thread com `lock.release()`.