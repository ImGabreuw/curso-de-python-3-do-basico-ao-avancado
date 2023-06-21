# Peculiaridades do tipo mutável set em Python

Os conjuntos em Python possuem características peculiares que os diferenciam de outras estruturas de dados:

1. Valores Únicos:

   Os conjuntos garantem que seus elementos sejam únicos. Se você tentar adicionar um valor que já está presente no conjunto, ele será ignorado. Veja um exemplo:

   ```python
   meu_conjunto = {1, 2, 3, 4, 5, 5}  # A duplicação do valor 5 será ignorada
   print(meu_conjunto)  # Saída: {1, 2, 3, 4, 5}
   ```

2. Aceitação de Iteráveis:

   É possível criar um conjunto a partir de um iterável, como uma string, utilizando a função `set()`. Nesse caso, o conjunto conterá apenas os elementos únicos presentes no iterável. Veja um exemplo:

   ```python
   s = set("Luiz")
   print(s)  # Saída: {'z', 'L', 'i', 'u'}
   ```

3. Valores Imutáveis:

   Os conjuntos em Python aceitam apenas tipos imutáveis como elementos. Isso significa que você não pode adicionar listas, dicionários ou outros conjuntos como elementos de um conjunto.

4. Falta de Índices e Ordem:

   Os conjuntos não possuem índices para acessar elementos individuais. Além disso, a ordem dos elementos em um conjunto não é garantida. Portanto, não se pode assumir que os elementos serão recuperados na mesma ordem em que foram adicionados.

5. Iterabilidade:

   Os conjuntos são iteráveis, o que significa que você pode percorrer seus elementos usando um loop `for`. No entanto, a ordem dos elementos durante a iteração pode variar.

   ```python
   meu_conjunto = {1, 2, 3, 4}
   for elemento in meu_conjunto:
       print(elemento)
   ```

   Além disso, é possível utilizar o operador `in` e `not`, para verificar se um elemento pertence a esse conjunto:

   ```python
   meu_conjunto = {1, 2, 3, 4}

   print(1 in meu_conjunto) # True
   print(10 not in meu_conjunto) # True
   ``` 

Essas peculiaridades tornam os conjuntos úteis em várias situações, como a remoção de duplicatas de uma lista, verificação de pertinência de um elemento e realização de operações de conjunto, como união, interseção e diferença.
