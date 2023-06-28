# Mantendo estados dentro da classe

Em Python, é possível manter estados dentro de classes usando atributos de instância. Os atributos de instância são variáveis que estão associadas a cada objeto criado a partir da classe e armazenam informações específicas desse objeto.

Ao criar uma classe, você pode definir atributos de instância para representar o estado do objeto. Esses atributos podem ser inicializados no construtor (`__init__`) da classe ou em outros métodos, conforme necessário. Os atributos de instância podem ser acessados e modificados pelos métodos da classe, permitindo que você mantenha e manipule o estado do objeto ao longo do tempo.

Vamos criar um exemplo com a classe "Contador" para ilustrar como manter estados dentro de classes em Python:

```python
class Contador:
    def __init__(self):
        self.valor = 0
    
    def incrementar(self):
        self.valor += 1
    
    def decrementar(self):
        self.valor -= 1
    
    def exibir_valor(self):
        print("Valor:", self.valor)
```

Nesse exemplo, a classe "Contador" possui um único atributo de instância chamado `valor`, que armazena o valor atual do contador.

O método `__init__` é o construtor da classe, e ele é responsável por inicializar o atributo `valor` com o valor inicial desejado, nesse caso, zero.

Os métodos `incrementar` e `decrementar` são responsáveis por modificar o estado do contador, aumentando ou diminuindo o valor do atributo `valor` em 1, respectivamente.

O método `exibir_valor` é responsável por exibir o valor atual do contador na tela.

Agora, vamos criar um objeto da classe "Contador" e chamar seus métodos:

```python
contador = Contador()
contador.exibir_valor()
contador.incrementar()
contador.exibir_valor()
contador.decrementar()
contador.exibir_valor()
```

Nesse exemplo, criamos um objeto chamado `contador` da classe "Contador" e chamamos o método `exibir_valor` para exibir o valor inicial do contador, que é zero. Em seguida, chamamos o método `incrementar` para aumentar o valor do contador em 1 e chamamos novamente o método `exibir_valor` para verificar o novo valor. Por fim, chamamos o método `decrementar` para diminuir o valor do contador em 1 e exibimos novamente o valor atual.

A saída esperada será:

```
Valor: 0
Valor: 1
Valor: 0
```

Nesse exemplo, o atributo de instância `valor` mantém o estado do contador. Cada objeto da classe "Contador" possui seu próprio valor de `valor`, permitindo que você mantenha vários contadores independentes uns dos outros.

Manter estados dentro de classes em Python é útil para armazenar informações específicas de cada objeto e permite que os métodos da classe manipulem essas informações de forma adequada. Dessa forma, você pode criar objetos que são capazes de manter seu próprio estado interno e realizar operações específicas com base nesse estado.