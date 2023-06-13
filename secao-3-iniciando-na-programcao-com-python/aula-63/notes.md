# while + while (laços internos)

O alinhamento de estruturas de repetições (como o `while`) é amplamente utilizado em manipulação de matrizes (ou arrays multidimensionais).

```python
linhas = 5
colunas = 5

linha = 1

while linha <= linhas:
    coluna = 1

    while coluna <= colunas:
      print(coluna, end=" ")
      coluna += 1

    print()
    linha += 1

# Matriz 5x5:
#
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5
```