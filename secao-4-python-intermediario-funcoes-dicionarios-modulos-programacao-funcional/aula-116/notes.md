# Closure e funções que retornam outras funções

> ## **Definição**

Em Python, uma _closure_ é uma função que mantém a referência a uma ou mais variáveis definidas em seu escopo externo, mesmo após a conclusão desse escopo. Em outras palavras, a função "lembra" das variáveis em seu ambiente de definição, mesmo quando é chamada fora desse ambiente.

Uma _closure_ é criada quando uma função interna faz referência a uma ou mais variáveis de uma função externa e retorna a função interna. A função interna, juntamente com as variáveis que ela captura do escopo externo, forma a _closure_.

> ## **Exemplo**

```python
def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar

falar_bom_dia = criar_saudacao("Boa dia")
falar_boa_noite = criar_saudacao("Boa noite")

print(falar_bom_dia("Luiz"))
print(falar_boa_noite("Luiz"))

# Boa dia, Luiz!
# Boa noite, Luiz!
```