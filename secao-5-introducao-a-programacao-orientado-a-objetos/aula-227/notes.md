# (Parte 3) LogFileMixin e a união de tudo até aqui

O código abaixo é um exemplo de como usar a abstração e mixins em Python para criar um sistema de log simples.

```python
from pathlib import Path

LOG_FILE = Path(__file__).parent / "log.txt"

class Log:
    def _log(self, message):
        raise NotImplementedError()
    
    def error(self, message):
        return self._log(f"Error: {message}")
    
    def sucess(self, message):
        return self._log(f"Success: {message}")
    
class LogFileMixin(Log):
    def _log(self, message):
        with open(LOG_FILE, "a") as file:
            file.write(message + "\n")

class LogPrintMixin(Log):
    def _log(self, message):
        print(message)


if __name__ == "__main__":
    log = LogFileMixin()

    log.error("Ocorreu um erro!")
    log.sucess("Sucesso!")
```

1. Abstração:
   A abstração é o processo de simplificar um sistema, permitindo que os usuários se concentrem apenas nos aspectos essenciais e ocultem os detalhes internos de implementação. No código dado, a classe `Log` é um exemplo de abstração. Ela define uma interface genérica para um logger que possui três métodos: `_log`, `error` e `sucess`. O método `_log` é marcado como `raise NotImplementedError()`, o que significa que não deve ser usado diretamente e precisa ser implementado pelas subclasses. As subclasses podem então fornecer uma implementação específica para a função `_log`.

2. Mixins:
   Mixins são classes que fornecem funcionalidades específicas que podem ser "misturadas" em outras classes por meio de herança múltipla. No código, temos dois mixins: `LogFileMixin` e `LogPrintMixin`.

- `LogFileMixin` é uma classe que herda da classe `Log`. Ela fornece uma implementação concreta para o método `_log` que grava as mensagens de log em um arquivo "log.txt" usando a biblioteca `pathlib`.

- `LogPrintMixin` é outra classe que herda da classe `Log`. Ela também fornece uma implementação concreta para o método `_log` que simplesmente imprime as mensagens de log no console.

No exemplo dado, `LogFileMixin` e `LogPrintMixin` são dois mixins que fornecem diferentes comportamentos para o mesmo sistema de log definido pela classe abstrata `Log`. Isso demonstra como os mixins podem ser úteis para adicionar funcionalidades adicionais a uma classe sem precisar modificar a sua estrutura original.

O trecho final do código cria uma instância de `LogFileMixin` chamada `log` e chama os métodos `error` e `sucess`. Como `LogFileMixin` herda da classe abstrata `Log` e fornece sua própria implementação para o método `_log`, a chamada dos métodos `error` e `sucess` resulta na escrita das mensagens de log no arquivo "log.txt".

Em resumo, a abstração permite definir uma interface comum para um sistema de log, enquanto os mixins fornecem implementações específicas que podem ser combinadas para adicionar funcionalidades extras ao sistema sem modificar sua estrutura principal. Isso torna o código mais modular, flexível e reutilizável.
