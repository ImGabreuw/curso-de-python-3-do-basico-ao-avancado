# Tipo tuple (tuplas)

> ## **Definição**

São listas imutáveis, ou seja, não é possível alterar o seus valores uma vez atribuídos. Além disso, não pode adicionar ou remover elementos.

Existem algumas formas de criar uma tupla:

- Com vírgulas:

  ```python
  nomes = "Luiz", "João", "Maria"
  ```

  ```python
  nomes = "Luiz",
  ```

  > No caso acima, para indicar ao Python uma tupla com apenas um elemento utilizando a notação `,`, deve-se colocar uma vírgula após o elemento.

- Com parênteses:

  ```python
  nomes = ("Luiz", "João", "Maria")
  ```

- Função `tuple`:
  ```python
  nomes = tuple("Luiz", "João", "Maria")
  ```