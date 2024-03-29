# Formatação de strings com o método format

> ## **Método: `format()`**

A string é um objeto no Python, logo ela possui atributos e métodos, como por exemplo o método `format()`.

O método `format()` é responsável por substituir a expressão `{}` por um valor passado no argumento dele. Em caso de ter vários argumentos, a substituição é feito na ordem que os os argumentos são definidos.

```python
a = "A"
b = "B"
c = "C"

formato = "a={} b={} c={}".format(a, b, c)

print(formato) # a=A b=B c=C
```

É possível formatar casas decimais de um número com esse método a partir da seguinte notação:

```python
n = 3.1415

formato = "número={:.2f}".format(n)

print(formato)
# número=3.14
```

> **OBS**: `2` indica o número de casas decimais desejadas na formatação e `f` representa a formatação de um `float`

Há outras formas de referenciar os valores na formatação, além da ordem dos argumentos:

- **Índices**: por padrão a contagem dos índices no Python é iniciada no 0

  ```python
  a = "A"
  b = "B"
  c = "C"

  formato = "a={0} b={1} c={2}".format(a, b, c)

  print(formato) # a=A b=B c=C
  ```

- **Parâmetro nomeado**: atribuir um rótulo para cada valor definido no argumento do método

  ```python
  a = "A"
  b = "B"
  c = "C"

  formato = "a={0} b={valor2} c={valor3}".format(
    a,
    valor2=b,
    valor3=c
    )

  print(formato) # a=A b=B c=C
  ```

  **OBS**: na utilização de parâmetros nomeados, é obrigatório utilizar esse padrão para os parâmetros posteriores

  ```python
  a = "A"
  b = "B"
  c = "C"

  formato = "a={valor1} b={valor2} c={2}".format(
    valor1=a,
    valor2=b,
    c
    )

  print(formato) # Error
  ```
