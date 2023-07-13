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