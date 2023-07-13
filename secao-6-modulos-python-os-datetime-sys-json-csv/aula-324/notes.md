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

Exemplo de saída do código acima:

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