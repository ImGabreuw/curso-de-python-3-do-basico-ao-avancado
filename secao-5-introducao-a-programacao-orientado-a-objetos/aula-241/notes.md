# Exceptions em context manager com classes

Em Python, é possível lidar com exceções dentro de um gerenciador de contexto, definindo a lógica de tratamento de exceções no método `__exit__` da classe do gerenciador de contexto. Isso permite capturar e tratar erros que ocorrem dentro do bloco `with` de maneira adequada.

Aqui está um exemplo de como lidar com exceções em um gerenciador de contexto:

```python
class ArquivoTexto:
    def __init__(self, nome_arquivo, modo):
        self.nome_arquivo = nome_arquivo
        self.modo = modo
        self.arquivo = None

    def __enter__(self):
        self.arquivo = open(self.nome_arquivo, self.modo)
        return self.arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        self.arquivo.close()
        if class_exception is not None:
            print(f'Ocorreu uma exceção: {class_exception}, {exception_}')
        return True

# Exemplo de uso do gerenciador de contexto com tratamento de exceções
with ArquivoTexto('meuarquivo.txt', 'w') as arquivo:
    arquivo.write('Olá, mundo!')
    raise ValueError('Erro intencional')
```

Neste exemplo, o bloco `with` é usado para abrir um arquivo de texto e escrever a mensagem `"Olá, mundo!"` nele. Em seguida, uma exceção do tipo `ValueError` é intencionalmente levantada.

Dentro do método `__exit__` do gerenciador de contexto, é verificado se algum tipo de exceção foi passado como argumento. Se `class_exception` não for `None`, significa que ocorreu uma exceção dentro do bloco `with`. Nesse caso, a mensagem de exceção é impressa na tela.

No exemplo acima, a exceção `ValueError` é levantada intencionalmente. Quando a exceção é capturada no `__exit__`, a mensagem `"Ocorreu uma exceção: <class 'ValueError'>, Erro intencional" é exibida.`

O tratamento de exceções em gerenciadores de contexto permite que você tenha um controle mais preciso sobre possíveis erros e tome ações apropriadas, como limpar recursos, fazer log de erros ou notificar o usuário. Isso garante que as operações de limpeza e encerramento sejam executadas mesmo em caso de exceções.