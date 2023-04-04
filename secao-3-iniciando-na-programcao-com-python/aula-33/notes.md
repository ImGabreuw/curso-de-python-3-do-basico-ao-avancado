# Usando a função input para coletar dados do usuário

> ## **Função: `input()`**

A função `input()` serve para coletar o texto que o usuário inseriu no terminal.

Essa função aceita como argumento uma string que seria a mensagem exibida na tela do terminal antes do usuário inserir o texto.

```python
nome = input("Qual é o seu nome? ")
```

```bash
$ Qual é o seu nome? João
```

> ## **Formatação de strings**

Há um atalho do Python para inserir o nome da variável e o seu valor utilizando o `f-strings`:

```python
nome = input("Qual é o seu nome? ")
print(f"O seu nome é {nome=}")
```

Ao invés de utilizar:

```python
nome = input("Qual é o seu nome? ")
print(f"O seu nome é nome={nome}")
```

```bash
$ Qual é o seu nome? João
> O seu nome é nome=João
```
