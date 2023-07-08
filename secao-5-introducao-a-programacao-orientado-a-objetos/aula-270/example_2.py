from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str = "Missing"
    sobrenome: str = "Missing"
    idade: int = 100
    enderecos: list[str] = []


if __name__ == "__main__":
    p = Pessoa()
    print(p)
