# @staticmethod (métodos estáticos) são inúteis em Python =)

Em Python, os métodos estáticos são métodos definidos em uma classe que não recebem uma referência à instância da classe (por meio do parâmetro `self`) nem à própria classe (por meio do parâmetro `cls`). Esses métodos são declarados usando o decorador `@staticmethod`.

Os métodos estáticos são semelhantes aos métodos de classe, mas não têm acesso a nenhum atributo de instância ou de classe. Eles são independentes da instância ou da classe e podem ser chamados diretamente na classe, sem a necessidade de criar uma instância. Eles são úteis para agrupar funções relacionadas à classe dentro da própria classe.

Aqui está um exemplo de como definir um método estático em Python:

```python
class MinhaClasse:
    @staticmethod
    def saudacao():
        return "Olá, mundo!"
```

Neste exemplo, a classe `MinhaClasse` possui um método estático chamado `saudacao`, que simplesmente retorna a string `"Olá, mundo!"`.

Você pode chamar esse método diretamente na classe, sem a necessidade de criar uma instância:

```python
print(MinhaClasse.saudacao())  # Saída: Olá, mundo!
```

Observe que não há necessidade de criar uma instância da classe `MinhaClasse` para chamar o método estático. O método estático não tem acesso a atributos de instância ou de classe, portanto, seu comportamento é independente de qualquer estado específico da classe.

Os métodos estáticos são úteis quando você tem uma função relacionada à classe, mas que não precisa interagir com o estado da instância ou da classe. Eles são usados principalmente para organizar e agrupar funções relevantes à classe.