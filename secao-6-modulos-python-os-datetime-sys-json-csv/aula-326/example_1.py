from threading import Thread
from time import sleep


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
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            return

        sleep(1)

        self.estoque -= quantidade

        print(f'Você comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} em estoque.')


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 10):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()