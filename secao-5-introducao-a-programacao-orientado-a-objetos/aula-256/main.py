from abc import ABC, abstractmethod
from typing import List


class Conta(ABC):
    def __init__(self, agencia: int, numero: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def exibir_extrato(self) -> None:
        print(f"Saldo da conta {self.numero}: R${self.saldo:,.2f}")

    @abstractmethod
    def sacar(self, valor: float) -> None:
        pass


class ContaCorrente(Conta):
    def init(self, agencia: int, numero: int, saldo: float = 0,
             limite: float = 0) -> None:
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> None:
        if (self.saldo - valor) < self.limite:
            print(f"Não é possível sacar o dinheiro, pois você atigiu o seu \
                  limite de R${-self.limite:,.2f}.")
            return

        self.saldo -= valor
        print(f"Saque de R${valor:,.2f} realizado com sucesso.")
        self.exibir_extrato()


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> None:
        if (self.saldo - valor) < 0:
            print("Saldo insuficiente.")
            return

        self.saldo -= valor
        print(f"Saque de R${valor:,.2f} realizado com sucesso.")
        self.exibir_extrato()


class Pessoa(ABC):
    def __init__(self, nome: str, idade: int) -> None:
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome) -> None:
        self.__nome = nome

    @property
    def idade(self) -> int:
        return self.__idade

    @idade.setter
    def idade(self, idade) -> None:
        self.__idade = idade


class Cliente(Pessoa):
    def __init__(self, conta: Conta) -> None:
        self.__conta = conta

    @property
    def conta(self) -> Conta:
        return self.__conta

    @conta.setter
    def conta(self, conta: Conta) -> None:
        self.__conta = conta


class Banco:
    contas: List[Conta] = []
    clientes: List[Conta] = []
    agencia = 100

    def autenticar(self, cliente: Cliente):
        conta = cliente.conta
        if conta.agencia != self.agencia \
            or cliente not in self.clientes \
                or conta not in self.contas:
            print("Não possível autenticar com essas informações")
            return False

        return True
