# Higher Order Functions - Funções de primeira classe

Em Python, funções de primeira classe (ou first-class functions) referem-se à capacidade de tratar funções como qualquer outra variável ou objeto. Isso significa que as funções podem ser atribuídas a variáveis, passadas como argumentos para outras funções, retornadas como valores de outras funções e armazenadas em estruturas de dados, como listas ou dicionários.

Aqui estão algumas características e exemplos que demonstram a natureza de primeira classe das funções em Python:

1. Atribuição a variáveis:
   ```python
   def saudacao():
       print("Olá!")

   minha_funcao = saudacao
   minha_funcao()  # Chamando a função através da variável
   ```

2. Passagem como argumento:
   ```python
   def saudacao(nome):
       print("Olá,", nome, "!")

   def executa_funcao(funcao, argumento):
       funcao(argumento)

   executa_funcao(saudacao, "Alice")  # Passando a função como argumento
   ```

3. Retorno de função:
   ```python
   def saudacao():
       def hello():
           return "Olá!"
       return hello

   minha_funcao = saudacao()
   print(minha_funcao())  # Chamando a função retornada
   ```

4. Armazenamento em estruturas de dados:
   ```python
   def saudacao():
       print("Olá!")

   lista_funcoes = [saudacao]
   for funcao in lista_funcoes:
       funcao()  # Chamando a função armazenada na lista
   ```

Essa capacidade de tratar funções como cidadãs de primeira classe em Python é extremamente útil para criar código flexível, modular e de alto nível. Permite a implementação de conceitos como programação funcional e callback, onde as funções podem ser passadas e executadas em diferentes contextos e situações.

### **OBS**

Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

- _Higher Order Functions_: Funções que podem receber e/ou retornar outras funções

- _First-Class Functions_: Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

> Esses termos podem ser diferentes e ainda refletir o mesmo significado.