# (Parte 1) Threads - Executando processamentos em paralelo

Por padrão o Python executa o código de forma linear pela _main thread_, ou seja, a próxima linha só é executado caso a linha atual seja executada com sucesso. Entretanto é possível mudar essa abordagem para processamento assíncrono (ou paralelo) com o módulo `threading`, mais especificamente com a classe `Thread`.

Para executar um bloco de código em paralelo, é necessário implementar o método `run` da classe `Thread`, por exemplo:

```python
from threading import Thread
from time import sleep


class Worker(Thread):
    def __init__(self, texto: str, tempo: int):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


worker1 = Worker('Worker 1', 5)
worker1.start()

worker2 = Worker('Worker 2', 3)
worker2.start()

worker3 = Worker('Worker 3', 2)
worker3.start()

for i in range(10):
    print(i)
    sleep(1)
```

Saída:

```console
0
1
Worker 3
2
Worker 2
3
4
5
Worker 1
6
7
8
9
```

Outra forma de executar um código de forma assíncrona é utilizando a própria classe `Thread`. Veja o exemplo abaixo:

```python
from threading import Thread
from time import sleep


def worker(texto: str, tempo: int):
    sleep(tempo)
    print(texto)


worker1 = Thread(target=worker, args=('Olá mundo 1!', 3))
worker1.start()

worker2 = Thread(target=worker, args=('Olá mundo 2!', 1))
worker2.start()

worker3 = Thread(target=worker, args=('Olá mundo 3!', 2))
worker3.start()

for i in range(10):
    print(i)
    sleep(.5)
```

Saída:

```console
0
1
Olá mundo 2!
2
3
Olá mundo 3!
4
5
Olá mundo 1!
6
7
8
9
```

O parâmetro nomeado `target` é a função que será executado em paralelo, já `args` são os argumentos necessários para a execução da função no formato de tupla.

O método `is_alive()` verifica se uma _thread_ está em execução retornando `True`, caso contrário `False`.

```python
from threading import Thread
from time import sleep


def worker(texto: str, tempo: int):
    sleep(tempo)
    print(texto)


worker1 = Thread(target=worker, args=('Olá mundo 1!', 10))
worker1.start()

while worker1.is_alive():
    print("Esperando a thread")
    sleep(2)

print("thread acabou")
```

Saída:

```console
Esperando a thread
Esperando a thread
Esperando a thread
Esperando a thread
Esperando a thread
Esperando a thread
Olá mundo 1!
thread acabou
```

O método `join()` serve para unir a execução da thread em paralelo na thread principal, tornando assim o código bloqueante.

```python
from threading import Thread
from time import sleep


def worker(texto: str, tempo: int):
    sleep(tempo)
    print(texto)


worker1 = Thread(target=worker, args=('Olá mundo 1!', 10))
worker1.start()
worker1.join()

print("thread acabou")
```

Saída:

```console
... Após 10 segundos ...

Olá mundo 1!
thread acabou
```