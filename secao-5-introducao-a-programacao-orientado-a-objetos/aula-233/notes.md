# Criando Exceptions em Python Orientado a Objetos (Exceções)

É interessante a criação de erros customizados caso for necessário comunicar outros desenvolvedores sobre uma possível exceção que pode acontecer durante a execução do programa.

No Python, para criar exceções customizadas é preciso herdar de alguma exceção da linguagem, entretanto é recomendado herdar de _Exception_ e caso você adote isso é uma boa prática adicionar o sufixo `Error` no nome da exceção.

> **OBS**: a convenção do sufixo `Error` é da própria linguagem e todas subclasses de `Exception` carregam no final do nome o sufixo `Error`, como é possível ver na [documentação do Python](https://docs.python.org/3/library/exceptions.html)

Veja o exemplo abaixo sobre uma exceção personalizada:

```python
class MyError(Exception):
  ...
```