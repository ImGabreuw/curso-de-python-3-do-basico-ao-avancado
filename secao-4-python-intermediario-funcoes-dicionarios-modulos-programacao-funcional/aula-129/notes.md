# Operadores importantes para o tipo set (conjuntos)

1. União (`conjunto1.union(conjunto2)` ou `conjunto1 | conjunto2`):

   A operação de união retorna um novo conjunto que contém todos os elementos presentes em ambos os conjuntos originais, sem duplicatas. Pode ser realizado usando o método `union()` ou o operador `|`. Aqui está um exemplo:

   ```python
   conjunto1 = {1, 2, 3}
   conjunto2 = {3, 4, 5}
   uniao = conjunto1.union(conjunto2)
   # ou uniao = conjunto1 | conjunto2
   print(uniao)  # Saída: {1, 2, 3, 4, 5}
   ```

2. Intersecção (`conjunto1.intersection(conjunto2)` ou `conjunto1 & conjunto2`):

   A operação de intersecção retorna um novo conjunto que contém apenas os elementos que estão presentes em ambos os conjuntos originais. Pode ser realizado usando o método `intersection()` ou o operador `&`. Aqui está um exemplo:

   ```python
   conjunto1 = {1, 2, 3}
   conjunto2 = {3, 4, 5}
   intersecao = conjunto1.intersection(conjunto2)
   # ou intersecao = conjunto1 & conjunto2
   print(intersecao)  # Saída: {3}
   ```

3. Diferença (`conjunto1.difference(conjunto2)` ou `conjunto1 - conjunto2`):

   A operação de diferença retorna um novo conjunto que contém os elementos presentes no primeiro conjunto, mas não no segundo. Pode ser realizado usando o método `difference()` ou o operador `-`. Aqui está um exemplo:

   ```python
   conjunto1 = {1, 2, 3}
   conjunto2 = {3, 4, 5}
   diferenca = conjunto1.difference(conjunto2)
   # ou diferenca = conjunto1 - conjunto2
   print(diferenca)  # Saída: {1, 2}
   ```

4. Diferença Simétrica (`conjunto1.symmetric_difference(conjunto2)` ou `conjunto1 ^ conjunto2`):

   A operação de diferença simétrica retorna um novo conjunto que contém os elementos que estão presentes em apenas um dos conjuntos originais. Pode ser realizado usando o método `symmetric_difference()` ou o operador `^`. Aqui está um exemplo:

   ```python
   conjunto1 = {1, 2, 3}
   conjunto2 = {3, 4, 5}
   dif_simetrica = conjunto1.symmetric_difference(conjunto2)
   # ou dif_simetrica = conjunto1 ^ conjunto2
   print(dif_simetrica)  # Saída: {1, 2, 4, 5}
   ```
