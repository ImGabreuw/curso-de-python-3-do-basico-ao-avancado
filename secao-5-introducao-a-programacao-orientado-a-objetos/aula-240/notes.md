# Context Manager com classes - Criando e Usando gerenciadores de contexto

Em Python, um gerenciador de contexto (context manager) é um objeto que define o comportamento a ser executado antes e depois de um bloco de código específico. Ele permite que você defina ações de inicialização e encerramento que devem ocorrer automaticamente antes e depois que o bloco de código é executado, independentemente do que acontece dentro dele. Isso é especialmente útil quando você precisa garantir a execução de determinadas operações, como a abertura e fechamento de arquivos, conexões de banco de dados ou bloqueios de recursos.

Uma maneira comum de criar um gerenciador de contexto em Python é implementando um objeto como uma classe e definindo os métodos `__enter__` e `__exit__`. O método `__enter__` é executado no início do bloco de código e o método `__exit__` é executado no final, independentemente de ocorrerem exceções.

Aqui está um exemplo de como criar e usar um gerenciador de contexto em Python:

```python
class ArquivoTexto:
    def __init__(self, nome_arquivo, modo):
        self.nome_arquivo = nome_arquivo
        self.modo = modo
        self.arquivo = None

    def __enter__(self):
        self.arquivo = open(self.nome_arquivo, self.modo, encoding="utf8")
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.arquivo.close()

# Exemplo de uso do gerenciador de contexto
with ArquivoTexto('meuarquivo.txt', 'w') as arquivo:
    arquivo.write('Olá, mundo!')
```

Nesse exemplo, a classe `ArquivoTexto` é um gerenciador de contexto que permite abrir e fechar um arquivo de texto. No método `__enter__`, o arquivo é aberto e retornado, permitindo seu uso dentro do bloco `with`. No método `__exit__`, o arquivo é fechado, garantindo que ele seja encerrado corretamente, mesmo se ocorrerem exceções dentro do bloco.

O uso do gerenciador de contexto é feito com a construção `with`. Isso garante que as operações de inicialização e encerramento do contexto sejam executadas corretamente, independentemente do que aconteça dentro do bloco. No exemplo, o arquivo é aberto dentro do bloco `with` e o texto `"Olá, mundo!"` é escrito nele. Ao final do bloco, o arquivo é automaticamente fechado, mesmo se ocorrerem exceções.

Duck Typing, por sua vez, é um conceito em Python onde o tipo de um objeto é determinado pela presença dos métodos e atributos necessários em vez de uma classe específica. Em outras palavras, se um objeto "caminha como um pato e grasna como um pato", ele pode ser tratado como um pato, independentemente do tipo real do objeto.

No exemplo do gerenciador de contexto acima, o objeto `ArquivoTexto` é tratado como um gerenciador de contexto, pois ele implementa os métodos `__enter__` e `__exit__` exigidos. Não importa se a classe herda de alguma classe específica ou implementa uma interface específica, desde que ela forneça os métodos necessários, ela pode ser usada como um gerenciador de contexto.

Isso exemplifica o conceito de Duck Typing em Python, onde o tipo de um objeto é determinado pelas operações que ele suporta em vez do seu tipo.
