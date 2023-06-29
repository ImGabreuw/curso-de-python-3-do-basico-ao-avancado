# @property + @setter - getter e setter no modo Pythônico

Em Python, o decorador `@property` também pode ser usado para criar métodos setter, permitindo que você defina lógica personalizada para a atribuição de valores a um atributo de uma classe.

Para criar um setter usando o decorador `@property`, você precisa definir um método com o mesmo nome do atributo desejado, seguido do decorador `@atributo.setter`. Esse método setter será chamado automaticamente sempre que você atribuir um valor a esse atributo.

> Por convenção, usa-se 1 ou 2 underline para indicar que um propriedade é privada, ou seja, só pode ser acessada por dentro da classe a qual foi declarada.

Aqui está um exemplo de como usar o decorador `@property` para criar um setter:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        else:
            raise ValueError("A idade deve ser um valor positivo.")
```

Neste exemplo, a classe `Pessoa` possui dois atributos privados, `_nome` e `_idade`. Os métodos `nome` e `idade` são getters correspondentes para esses atributos. Em seguida, temos os métodos setters `nome` e `idade`, decorados com `@nome.setter` e `@idade.setter`, respectivamente.

Agora, podemos atribuir valores aos atributos usando os setters personalizados:

```python
pessoa = Pessoa("João", 30)

pessoa.nome = "Maria"
pessoa.idade = 25

print(pessoa.nome)    # Saída: Maria
print(pessoa.idade)   # Saída: 25
```

Observe que, ao atribuir um novo valor ao atributo `nome` ou `idade`, o método setter correspondente é chamado automaticamente. Nesse exemplo, o método setter da idade verifica se o valor fornecido é um número positivo. Se não for, uma exceção `ValueError` é lançada.

O uso do decorador `@property` para criar setters personalizados oferece uma maneira conveniente de controlar a atribuição de valores a atributos, permitindo que você adicione lógica adicional para validação ou manipulação antes de definir o valor real. Isso ajuda a manter a consistência e a integridade dos dados em sua classe.