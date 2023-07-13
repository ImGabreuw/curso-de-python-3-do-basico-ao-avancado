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