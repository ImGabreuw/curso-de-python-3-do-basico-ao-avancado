# random tem geradores de números pseudoaleatórios (sample, choices, seed)

Continuando com as funcionalidades do módulo `random` do Python, vou explicar e fornecer exemplos das funções `sample()`, `choices()` e `seed()`:

Essas funções permitem a geração de números pseudoaleatórios, amostragem aleatória e controle de probabilidade de seleção.

### `shuffle(sequence)`

A função `shuffle()` é usada para embaralhar aleatoriamente uma sequência, como uma lista. Ela modifica a sequência original. Aqui está um exemplo:

```python
import random

lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(lista)
```

A saída será uma versão embaralhada da lista original, como `[3, 5, 1, 2, 4]`.

### `sample(population, k)`

A função `sample()` é usada para obter uma amostra aleatória sem substituição a partir de uma sequência de elementos. Você precisa fornecer a sequência (`population`) da qual deseja obter a amostra e o tamanho da amostra (`k`). A função retornará uma lista com os elementos selecionados aleatoriamente. Aqui está um exemplo:

```python
import random

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

amostra = random.sample(numeros, 3)
print(amostra)
```

Nesse exemplo, `numeros` é uma lista de números de 1 a 10. A função `sample()` é usada para selecionar aleatoriamente 3 números da lista sem substituição. A saída será uma lista com os 3 números selecionados aleatoriamente.

### `choices(population, weights=None, k=1)`

A função `choices()` é usada para obter uma amostra aleatória com substituição a partir de uma sequência de elementos. Ela permite atribuir pesos aos elementos para controlar a probabilidade de seleção. A função retorna uma lista com os elementos selecionados aleatoriamente. Aqui está um exemplo:

```python
import random

opcoes = ['cara', 'coroa']
pesos = [0.6, 0.4]

amostra = random.choices(opcoes, weights=pesos, k=5)
print(amostra)
```

Nesse exemplo, temos uma lista de opções contendo `'cara'` e `'coroa'`. A função `choices()` é usada para selecionar aleatoriamente 5 elementos dessa lista, levando em consideração os pesos atribuídos a cada opção. No exemplo, a opção `'cara'` tem peso 0.6, enquanto a opção `'coroa'` tem peso 0.4. A saída será uma lista com 5 elementos selecionados aleatoriamente, com base nas probabilidades definidas pelos pesos.

### `seed(a=None)`:

A função `seed()` do módulo `random` é usada para inicializar o gerador de números pseudoaleatórios. Ao chamar essa função e fornecer um valor de semente específico, você define um ponto de partida para a sequência de números gerados.

A ideia por trás dos números pseudoaleatórios é que eles são gerados por algoritmos determinísticos. Esses algoritmos são projetados para produzir uma sequência aparentemente aleatória de números com base em uma semente inicial.

No Python, a função `seed()` permite que você defina a semente manualmente. Se você fornecer a mesma semente, obterá exatamente a mesma sequência de números pseudoaleatórios. Por exemplo:

```python
import random

random.seed(42)

numero1 = random.random()
numero2 = random.random()

print(numero1)  # Saída esperada: 0.6394267984578837
print(numero2)  # Saída esperada: 0.025010755222666936
```

Neste exemplo, definimos a semente como 42 e geramos dois números pseudoaleatórios. Se executarmos o código novamente com a mesma semente, obteremos exatamente a mesma sequência de números.

A razão pela qual os números gerados são chamados de "pseudoaleatórios" é porque eles não são realmente aleatórios no sentido matemático. Eles são determinados pelo algoritmo subjacente e pela semente inicial. Uma vez que você conhece a semente, pode reproduzir a mesma sequência de números.

No entanto, esses números são suficientemente aleatórios para muitos casos de uso práticos. Para a maioria das aplicações, os números pseudoaleatórios são adequados e satisfazem as necessidades.

Os algoritmos usados para gerar números pseudoaleatórios no Python e em outras linguagens de programação são projetados para terem boas propriedades estatísticas, como distribuição uniforme e independência estatística. Isso os torna adequados para a maioria dos casos de uso, como simulações, jogos, criptografia e muito mais.

No entanto, é importante observar que os números pseudoaleatórios não devem ser usados em contextos em que a aleatoriedade verdadeira é necessária, como em aplicações criptográficas, onde a segurança depende da aleatoriedade real. Para tais casos, são usados geradores de números aleatórios criptograficamente seguros (CSPRNGs), que são projetados especificamente para fornecer aleatoriedade verdadeira.
