# Modularização - Entendendo os seus próprios módulos e sys.path no Python

Em Python, a modularização refere-se à prática de **dividir um programa em módulos independentes e reutilizáveis**. Isso ajuda a organizar e estruturar o código, tornando-o mais legível, manutenível e promovendo a reutilização de código.

Ao criar seus próprios módulos em Python, você pode agrupar funções, classes e variáveis relacionadas em um arquivo separado e usá-lo em outros programas. Aqui está como você pode criar e usar seus próprios módulos:

1. Criando um módulo:

   - Crie um novo arquivo com uma extensão `.py`, como `meu_modulo.py`.

   - Defina funções, classes e variáveis no arquivo.

   - Salve o arquivo.

   Exemplo (meu_modulo.py):

   ```python
   def saudacao(nome):
       print(f"Olá, {nome}!")

   def calcular_quadrado(numero):
       return numero ** 2

   PI = 3.14159
   ```

2. Usando um módulo:

   - No arquivo em que deseja usar o módulo, importe-o usando a declaração `import`.

   Exemplo:

   ```python
   import meu_modulo

   meu_modulo.saudacao("Alice")  # Chamando a função saudacao do módulo
   print(meu_modulo.calcular_quadrado(5))  # Usando a função calcular_quadrado
   print(meu_modulo.PI)  # Acessando a variável PI do módulo
   ```

   Alternativamente, você pode usar a declaração `from` para importar componentes específicos do módulo.

   Exemplo:

   ```python
   from meu_modulo import saudacao, calcular_quadrado, PI

   saudacao("Bob")  # Chamando a função saudacao diretamente
   print(calcular_quadrado(7))  # Usando a função calcular_quadrado diretamente
   print(PI)  # Acessando a variável PI diretamente
   ```

   Você também pode usar a palavra-chave `as` para atribuir um nome alternativo ao módulo importado.

   Exemplo:

   ```python
   import meu_modulo as mm

   mm.saudacao("Carol")  # Chamando a função saudacao usando o alias mm
   ```

Ao criar seus próprios módulos, certifique-se de nomeá-los de forma significativa, para que seu propósito seja claro. Além disso, defina os nomes do módulos seguindo os padrões de nomenclatura de variáveis. Organize as funções e classes de forma lógica dentro do módulo e adicione comentários e documentação adequados para facilitar o uso por outras pessoas.

Lembre-se de que o **arquivo do módulo deve estar no mesmo diretório do programa (arquivo com nome `__main__`)** que o importa ou em um diretório listado no `sys.path`. Isso garante que o Python encontre o módulo durante o processo de importação.

> **OBS**: o Python só reconhece módulo adjacentes ao módulo de entrada (`__main__`) e os abaixo dele na hierarquia de arquivos.

O arquivo que é o ponto de entrada do programa, ou seja, aquele que é executado primeiro, sempre tem o nome de `__main__`. Para você descobrir isso, basta utilizar o _dunder_ `__name__` dentro do módulo.

```python
# Arquivo teste.py

print("Este módulo se chama", __name__)
```

Ao executar esse módulo:

```console
$ python teste.py
```

Saída do programa:

```console
Este módulo se chama __main__
```

> **OBS**: todo arquivo passado como argumento do comando `python [arquivo]` será considerado o ponto de entrada do programa, logo seu nome é `__main__`

Com a modularização, você pode dividir seu código em partes mais gerenciáveis e reutilizáveis, facilitando a manutenção e promovendo boas práticas de programação.
