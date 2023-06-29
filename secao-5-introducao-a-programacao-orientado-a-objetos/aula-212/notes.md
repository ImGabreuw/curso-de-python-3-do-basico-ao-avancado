# @property - um getter no modo Pythônico

Em Python, o decorador `@property` é usado para criar métodos getter, ou seja, métodos que permitem acessar o valor de um atributo de uma classe como se fosse um atributo, mas com a possibilidade de realizar operações adicionais ou aplicar lógica específica antes de retornar o valor.

O decorador `@property` é usado para transformar um método em um atributo somente leitura. Quando você acessa o atributo com a sintaxe de leitura (`objeto.atributo`), o método decorado pelo `@property` é chamado automaticamente.

Aqui está um exemplo de como usar o decorador `@property` para criar um getter:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome_completo(self):
        return self.nome + " Sobrenome"

    @property
    def idade_em_meses(self):
        return self.idade * 12
```

Neste exemplo, a classe `Pessoa` possui dois métodos decorados com `@property`. O método `nome_completo` retorna o nome completo da pessoa, adicionando a string "Sobrenome" ao final do nome. O método `idade_em_meses` retorna a idade da pessoa em meses.

Você pode acessar esses atributos de forma transparente, como se fossem atributos públicos da classe:

```python
pessoa = Pessoa("João", 30)

print(pessoa.nome_completo)    # Saída: João Sobrenome
print(pessoa.idade_em_meses)   # Saída: 360
```

Observe que você não precisa chamar os métodos como funções (`pessoa.nome_completo()`), mas sim como se fossem atributos (`pessoa.nome_completo`). O decorador `@property` permite que você defina métodos que se comportam como atributos, fornecendo uma interface mais intuitiva para acessar e manipular dados dentro de uma classe.

O uso do `@property` é útil quando você deseja fornecer uma interface mais simples para acessar e manipular atributos, encapsulando a lógica adicional dentro dos métodos getter. Além disso, você também pode definir métodos setters e deleters correspondentes usando o decorador `@atributo.setter` e `@atributo.deleter`, respectivamente, permitindo um controle mais preciso sobre a atribuição e exclusão de valores.