# secrets gera números aleatórios seguros

O módulo `secrets` do Python fornece funções para gerar números aleatórios seguros. Ao contrário do módulo `random`, que gera números pseudoaleatórios, o `secrets` é projetado para gerar números aleatórios que são adequados para aplicações que exigem alta segurança, como geração de senhas, tokens de autenticação, chaves criptográficas, entre outros.

Esse módulo utiliza fontes criptograficamente seguras para gerar números aleatórios, o que o torna adequado para aplicações sensíveis à segurança. No entanto, é importante lembrar que o `secrets` é mais lento do que o `random`, devido aos requisitos de segurança mais rigorosos. Portanto, é recomendado usá-lo somente quando a segurança é uma preocupação primordial.

### `secrets.randbelow(n)`

A função `randbelow()` retorna um número aleatório entre 0 e n-1 (exclusivo). É semelhante à função `randrange()` do módulo `random`, mas é projetada para gerar números aleatórios seguros. Aqui está um exemplo:

```python
import secrets

numero = secrets.randbelow(10)
print(numero)
```

A saída será um número aleatório seguro entre 0 e 9.

### `secrets.choice(sequence)`

A função `choice()` retorna um elemento aleatório de uma sequência. Ela é semelhante à função `choice()` do módulo `random`, mas é projetada para trabalhar com números aleatórios seguros. Aqui está um exemplo:

```python
import secrets

lista = [1, 2, 3, 4, 5]
escolha = secrets.choice(lista)
print(escolha)
```

A saída será um elemento aleatório seguro da lista.

### `secrets.token_bytes(n)`

A função `token_bytes()` retorna uma sequência de n bytes aleatórios seguros. É útil para gerar chaves criptográficas e outros valores que requerem alta entropia. Aqui está um exemplo:

```python
import secrets

bytes_aleatorios = secrets.token_bytes(16)
print(bytes_aleatorios)
```

A saída será uma sequência de 16 bytes aleatórios seguros.

### `secrets.token_hex(n)`

A função `token_hex()` retorna uma string hexadecimal de n bytes aleatórios seguros. É útil para gerar identificadores únicos e outros valores criptograficamente seguros em formato legível. Aqui está um exemplo:

```python
import secrets

hex_aleatorio = secrets.token_hex(8)
print(hex_aleatorio)
```

A saída será uma string hexadecimal de 16 caracteres (8 bytes) aleatórios seguros.

### `secrets.SystemRandom()`

A classe `secrets.SystemRandom()` usa um gerador de números aleatórios fornecido pelo sistema operacional como fonte de entropia. Essa classe é especialmente útil quando é necessário gerar números aleatórios seguros em sistemas operacionais que fornecem geradores de números aleatórios de alta qualidade.

Ao usar `secrets.SystemRandom()`, você está aproveitando a funcionalidade de geração de números aleatórios seguros do sistema operacional subjacente, que geralmente é fornecido por geradores criptograficamente seguros.

Aqui está um exemplo que demonstra o uso da classe `secrets.SystemRandom()` para gerar um número aleatório:

```python
import secrets

gerador = secrets.SystemRandom()

gerador.seed(10) # Não afeta a aleatoriedade dos números

numero = gerador.randint(1, 10)
print(numero)
```

Nesse exemplo, criamos um objeto `gerador` da classe `secrets.SystemRandom()`. Em seguida, chamamos o método `randint()` do objeto `gerador` para gerar um número inteiro aleatório entre 1 e 10 (inclusive). A saída será um número aleatório seguro.

Ao utilizar `secrets.SystemRandom()`, você pode ter mais confiança na segurança dos números gerados, pois eles são provenientes de uma fonte confiável do sistema operacional. Isso é especialmente útil em cenários que exigem alta segurança, como criptografia, autenticação e geração de senhas.

É importante ressaltar que o uso de `secrets.SystemRandom()` pode ser um pouco mais lento do que o uso do `random` ou do `secrets` padrão, pois a geração de números aleatórios seguros envolve operações criptográficas mais intensivas. Portanto, é recomendado usar `secrets.SystemRandom()` apenas quando a segurança é uma preocupação primordial.