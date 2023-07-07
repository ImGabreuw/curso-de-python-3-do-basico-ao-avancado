# DocStrings em funções (Documentação)

A documentação de funções no Python pode ser feita de várias formas, dentre elas iremos abordar a documentação com DocStrings e _Type Hinting_.

```python
def multiplica(
    x: int | float,
    y: int | float,
    z: int | float | None = None
) -> int | float:
    """Multiplica x, y e/ou z
    Multiplica x e y. Se z for enviado, multiplica x, y, z.
    """
    if z is None:
        return x * y
    return x * y * z
```

Entretanto, nas versões mais antigas utilizava-se a seguinte forma de documentação de funções:

```python
def soma(x, y):
  """Soma x e y
  Este módulo contém funções e exemplos de documentação de funções.
  A função soma você já conhece bastante.
  :param x: Número 1
  :type x: int or float
  :param y: Número 2
  :type y: int or float
  :return: A soma entre x e y
  :rtype: int or float
  """
  return x + y
```
