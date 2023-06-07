# while e break - Estrutura de repetição (Parte 1)

> ## **Definição**

A estrutura de repetição `while` executa um bloco de código enquanto uma condição for verdadeira.

**ATENÇÃO**: loop infinito é quando uma estrutura de repetição é executada infinitamente uma vez que a condição nunca é alterada para `False` para assim interromper esse loop. Por exemplo:

```python
while True:
  print("Hello world!")

# Hello world!
# Hello world!
# Hello world!
# ...
```

Entretanto, é possível **interromper um loop** sem alterar a condição do `while` e para isso utiliza-se a palavra reservada `break`.

```python
while True:
  print("Hello world!")
  break

# Hello world!
```

> **OBS**: `break` interromperá a execução da **estrutura de repetição mais próxima** dele.

> ## **Exemplo**

```python
while True:
  nome = input("Qual é o seu nome? ")

  if nome == "sair":
    break

  print(f"Seu nome é {nome}.")
```