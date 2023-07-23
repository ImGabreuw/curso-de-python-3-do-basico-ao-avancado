# Type annotations - Tipagem de dados no Python 3.10

> ## **Introdução**

_Type annotation_ é uma funcionalidade do Python que permite especificar o tipo de dados que uma variável, parâmetro ou retorno de função deve ter. Isso pode ser útil para melhorar a legibilidade do código, documentar a intenção do programador e também para ferramentas de análise estática e IDEs realizarem verificações de tipos.

As _type annotation_ são definidas utilizando a sintaxe de anotação de tipo, que consiste em adicionar os tipos de dados após os parâmetros ou variáveis, separados por dois pontos (`:`). Para especificar o tipo de retorno de uma função, você pode utilizar a seta (`->`) seguida pelo tipo de retorno.

A partir do Python 3.5, a PEP 484 introduziu a possibilidade de utilizar _type annotation_. A partir do Python 3.7, a PEP 563 permite que as _type annotation_ sejam usadas de forma opcional, usando a sintaxe de comentários. Isso significa que as _type annotation_ podem ser utilizadas de forma mais flexível em versões mais recentes do Python.

Exemplos:

1. Anotação de tipo em variáveis:

   ```python
   nome: str = "João"
   idade: int = 30
   altura: float = 1.75
   ```

2. Anotação de tipo em parâmetros de função:

   ```python
   def soma(a: int, b: int):
       return a + b
   ```

3. Anotação de tipo em retorno de função:

   ```python
   def dividir(a: float, b: float) -> float:
       return a / b
   ```

   > **OBS**: o tipo `float` é um subtipo de `int`, logo é possível retornar um `float` mesmo que o tipo especificado no retorno da função seja `int`.

4. Anotação de tipo em listas e dicionários:

   ```python
   # Lista de inteiros
   numeros: List[int] = [1, 2, 3, 4]

   # Dicionário com chave string e valor inteiro
   idades: Dict[str, int] = {"João": 30, "Maria": 25, "Pedro": 28}
   ```

5. Anotação de tipo em funções como argumentos:

   ```python
   from typing import Callable

   def aplicar_operacao(a: int, b: int, operacao: Callable[[int, int], int]) -> int:
       return operacao(a, b)

   def soma(a: int, b: int) -> int:
       return a + b

   def multiplicacao(a: int, b: int) -> int:
       return a * b

   resultado_soma = aplicar_operacao(3, 5, soma)           # Resultado: 8
   resultado_multiplicacao = aplicar_operacao(3, 5, multiplicacao)  # Resultado: 15
   ```

Lembre-se de que as _type annotation_ são apenas uma ferramenta para documentar os tipos de dados esperados, e o Python continua sendo uma linguagem dinamicamente tipada. As _type annotation_ não têm impacto em tempo de execução e não afetam o comportamento do programa, mas podem ser verificadas por ferramentas de análise estática e IDEs para fornecer sugestões e detecção de erros relacionados a tipos.

> ## **Type Alias**

_Type alias_ é uma forma de criar um nome alternativo para um tipo de dado existente no Python. Ele permite definir um nome mais descritivo e legível para um tipo complexo ou composto, tornando o código mais claro e expressivo.

A declaração de type alias é realizada usando o `typing.TypeAlias` (Python 3.9+) ou usando o `typing.NewType` (Python 3.6+). Com a PEP 585 (Python 3.9), `TypeAlias` foi introduzido como uma maneira recomendada de criar _aliases_ de tipo. Mas se você estiver usando uma versão anterior do Python, ainda pode usar `NewType` para esse propósito.

Exemplo usando `TypeAlias`:

```python
from typing import List, TypeAlias

# Criando um alias para o tipo List[str]
Nomes = TypeAlias(List[str])

# Utilizando o alias
nomes: Nomes = ['João', 'Maria', 'Pedro']
```

Exemplo usando `NewType`:

```python
from typing import List, NewType

# Criando um alias para o tipo List[str]
Nomes = NewType('Nomes', List[str])

# Utilizando o alias
nomes: Nomes = ['João', 'Maria', 'Pedro']
```

> **OBS**: `TypeAlias` é uma forma mais recomendada para criar _aliases_ de tipo em versões mais recentes do Python. No entanto, `NewType` ainda é amplamente utilizado em versões anteriores do Python.

É importante destacar que os type _aliases_ não criam novos tipos ou validações em tempo de execução. Eles são apenas uma maneira de fornecer nomes mais descritivos para tipos existentes, facilitando a legibilidade e a manutenção do código.

> ## **Type Union**

Em Python, `Type Union` (também conhecido como `Union`) é uma funcionalidade do módulo `typing` que permite especificar que um determinado valor ou parâmetro pode ter mais de um tipo aceitável. Isso é útil quando você deseja que uma função ou variável possa lidar com diferentes tipos de dados de entrada.

A sintaxe para utilizar `Union` é simples. Você pode usar o operador de barra vertical `|` para combinar os tipos desejados. A declaração `Union` informa que a variável ou parâmetro pode ser de qualquer um dos tipos especificados.

Exemplo de uso do `Union`:

```python
from typing import Union

def calcular_area(shape: Union[int, float], side: Union[int, float]) -> Union[int, float]:
    return shape * side

area1 = calcular_area(5, 5)        # Retorna 25 (int * int)
area2 = calcular_area(4.5, 3.2)    # Retorna 14.399999999999999 (float * float)
area3 = calcular_area(3, 2.5)      # Retorna 7.5 (int * float)
```

Neste exemplo, criamos uma função `calcular_area` que calcula a área de uma forma geométrica com base na forma (shape) e no lado (side) fornecidos. Os parâmetros `shape` e `side` foram anotados como `Union[int, float]`, o que significa que eles podem ser de tipo `int` ou `float`.

A função pode ser chamada com argumentos de diferentes tipos. Por exemplo, `calcular_area(5, 5)` retorna 25 (int * int), `calcular_area(4.5, 3.2)` retorna 14.399999999999999 (float * float) e `calcular_area(3, 2.5)` retorna 7.5 (int * float). O retorno também foi anotado com `Union[int, float]`, indicando que a função pode retornar um valor de tipo `int` ou `float`.

`Union` é útil para situações em que a função ou variável pode operar de forma genérica, aceitando diferentes tipos de dados sem precisar usar verificações de tipo adicionais. Isso torna o código mais flexível e legível. Entretanto, é importante usá-lo com parcimônia, pois em alguns casos pode ser preferível fazer uso do polimorfismo nativo do Python, que permite a criação de funções sobrecarregadas para tipos específicos, tornando o código mais explícito e mais fácil de entender.

> ## **Optional Types**

Em Python, `Optional` é uma funcionalidade do módulo `typing` que permite especificar que um determinado valor ou parâmetro pode ser de um tipo específico ou ser nulo (`None`). Isso é útil quando você deseja indicar que um valor pode ser opcional em uma função ou variável.

A sintaxe para utilizar `Optional` é simples. Você pode usá-lo combinado com outro tipo, utilizando o operador de barra vertical `|` entre os tipos. A declaração `Optional` indica que o valor pode ser de um dos tipos especificados ou ser `None`.

Exemplo de uso do `Optional`:

```python
from typing import Optional

def buscar_usuario(usuario_id: Optional[int]) -> Optional[str]:
    if usuario_id is None:
        return None

    # Simulando a busca do nome do usuário a partir do ID
    # Neste exemplo, retorna uma string com o nome do usuário
    return "João da Silva"

nome_usuario = buscar_usuario(123)       # Retorna "João da Silva"
nome_usuario_nulo = buscar_usuario(None) # Retorna None
```

Neste exemplo, criamos uma função `buscar_usuario` que recebe um `usuario_id` como parâmetro e retorna o nome do usuário associado a esse ID. O parâmetro `usuario_id` foi anotado como `Optional[int]`, o que significa que ele pode ser do tipo `int` ou `None`.

Dentro da função, verificamos se o `usuario_id` é `None`. Se for, retornamos `None`, indicando que não foi encontrado um usuário com o ID especificado. Caso contrário, retornamos um nome de usuário fictício para fins de ilustração.

Ao chamar a função com um valor inteiro (`buscar_usuario(123)`), ela retorna o nome do usuário associado ao ID 123. Já quando chamamos a função com `None` (`buscar_usuario(None)`), ela retorna `None`, indicando que o usuário não foi encontrado.

`Optional` é útil quando você quer indicar explicitamente que um valor pode ser nulo ou de um determinado tipo. Isso pode ajudar a evitar erros e deixar o código mais legível, mostrando de forma clara que o valor é opcional.

> ## **TypeVar**

Em Python, `TypeVar` é uma funcionalidade do módulo `typing` que permite criar um tipo genérico (variável de tipo) que pode ser usado em anotações de tipo para indicar que um determinado valor pode ser de um tipo específico, mas sem especificar qual esse tipo é. Isso é útil quando você deseja criar funções ou classes que sejam genéricas o suficiente para trabalhar com diferentes tipos de dados sem especificar o tipo exato em seu código.

A sintaxe para criar um `TypeVar` é simples. Você pode usar a função `TypeVar` do módulo `typing` para criar uma variável de tipo. Geralmente, você passa um nome como argumento para o `TypeVar`, mas é opcional.

Exemplo de uso do `TypeVar`:

```python
from typing import TypeVar, List

T = TypeVar('T')  # Criação da variável de tipo

def imprimir_elementos(lista: List[T]) -> None:
    for elemento in lista:
        print(elemento)

# Exemplo de uso da função imprimir_elementos
lista_inteiros = [1, 2, 3, 4, 5]
lista_strings = ['a', 'b', 'c', 'd', 'e']

imprimir_elementos(lista_inteiros)  # Imprime 1 2 3 4 5
imprimir_elementos(lista_strings)   # Imprime a b c d e
```

Neste exemplo, criamos uma variável de tipo `T` usando `TypeVar`. Essa variável de tipo pode ser qualquer tipo específico, mas não é especificada no momento da criação.

Em seguida, definimos uma função `imprimir_elementos` que recebe uma lista de elementos de tipo `T` e imprime cada um dos elementos usando um loop `for`. Note que a função não se preocupa com o tipo específico da lista, pois `T` é um tipo genérico que representa qualquer tipo de dados.

Quando chamamos a função `imprimir_elementos`, podemos passar uma lista de inteiros ou uma lista de strings, pois a função é genérica o suficiente para trabalhar com diferentes tipos de dados.

O `TypeVar` é útil quando você quer escrever funções ou classes que possam lidar com tipos variados sem ter que especificar o tipo exato em seu código. Isso permite maior reutilização de código e torna as suas funções e classes mais flexíveis e genéricas.