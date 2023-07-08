from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str = "Missing"
    sobrenome: str = "Missing"
    idade: int = 100


if __name__ == "__main__":
    p = Pessoa()
    print(p)
