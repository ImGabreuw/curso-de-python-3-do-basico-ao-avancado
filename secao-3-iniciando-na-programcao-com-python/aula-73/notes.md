# range + for para usar intervalos de números

> ## **Definição**

A função `range` é um iterável que retorna um intervalo de valores respeitando as regras definidas a partir do seus parâmetros (`start`, `stop`, `end`).

Cada parâmetro tem um significado:

- `start` (valor padrão `0`): representa o valor de início do intervalo (inclusivo).

- `stop`: representa o valor de término do intervalo (exclusivo)

- `step` (valor padrão `1`): representa o espaçamento entre os elementos do intervalo. Aceita valores negativos, ou seja, pega os valores da direita para a esquerda na reta numérica dos números inteiros.

> ## **Exemplo**

```python
for i in range(1, 11):
  print(i, end=" ")

# 1 2 3 4 5 6 7 8 9 10
```

```python
for i in range(10, 0, -1):
  print(i, end=" ")

# 10 9 8 7 6 5 4 3 2 1
```

A utilização do `step` é muito conveniente em situações o qual é necessário obter os múltiplos de um número dentro de um intervalo de valores.

```python
for i in range(0, 100, 8):
  print(i, end=" ")

# Múltiplos de 8: 0 8 16 24 32 40 48 56 64 72 80 88 96
```