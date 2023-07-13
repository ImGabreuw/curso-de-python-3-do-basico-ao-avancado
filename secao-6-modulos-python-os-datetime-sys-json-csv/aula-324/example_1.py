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
