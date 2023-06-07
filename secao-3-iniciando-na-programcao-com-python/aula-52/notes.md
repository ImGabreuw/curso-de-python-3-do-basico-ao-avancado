# id - A identidade do valor que está na memória

Todo valor de uma variável é armazenado em memória. Dessa forma, o Python possui um mecanismo interno para fazer o alocamento de memória da forma mais otimizado possível.

Para isso, cada valor tem uma **identidade** (ID) que faz referência a esse valor na memória.

É possível obter o ID do valor de uma variável a partir da função `id()`:

```python
v1 = "a"
v2 = "a"

print(id(v1)) # 139916617267568
print(id(v2)) # 139916617267568
```

As **strings são imutáveis** (tipo `Literal`), ou seja, o seu valor nunca é alterado após sua criação. Dessa forma, para otimizar o alocamento de memória, o Python atribui a **mesma referência (ID)** para variáveis que armazenam **string com o mesmo conteúdo**.

> **OBS**: o comportamento citado acima varia de acordo com a versão do Python, interpretador, etc.