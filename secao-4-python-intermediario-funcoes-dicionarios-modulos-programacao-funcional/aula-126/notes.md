# Introdução ao tipo set em Python (conjuntos)

> ## **Definição**

O conjunto em Python é uma estrutura de dados mutável que armazena valores únicos e não ordenados. No entanto, o conjunto aceita apenas tipos imutáveis como seus elementos.

É possível criar um conjunto de duas formas:

- Utilizando a notação `{}` e inserindo os valores separados por vírgula entre as chaves. Por exemplo:

```python
meu_conjunto = {1, 2, 3, 4, 5}
```

- Utilizando a classe `set()` e passando uma sequência de valores como argumento. Por exemplo:

```python
meu_conjunto = set([1, 2, 3, 4, 5])
```

Uma característica importante do conjunto é que ele não permite a duplicação de elementos. Portanto, se você adicionar um valor que já está presente no conjunto, ele será ignorado. Veja um exemplo:

```python
meu_conjunto = {1, 2, 3, 4, 5, 5}  # A duplicação do valor 5 será ignorada
print(meu_conjunto)  # Saída: {1, 2, 3, 4, 5}
```

Outra característica peculiar do `set` ocorre com tipo iteráveis o qual cada índice do conjunto armazenará o valor obtido por meio de `__next()__`, como por exemplo `str`:

```python
s = set("Luiz")

print(s) # {"z", "L", "i", "u"}
```