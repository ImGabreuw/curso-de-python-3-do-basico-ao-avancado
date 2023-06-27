# Positional-Only Parameters (/) e Keyword-Only Arguments (\*)

Em Python, existem dois recursos relacionados a parâmetros de função: Positional-Only Parameters (parâmetros posicionais) e Keyword-Only Arguments (argumentos somente por palavra-chave). Esses recursos permitem definir a forma como os argumentos são passados para uma função.

### **Positional-Only Parameters (`/`)**

Os parâmetros posicionais definem argumentos que só podem ser passados por posição, ou seja, não podem ser especificados por nome. Isso significa que eles devem ser fornecidos na ordem correta conforme definido na assinatura da função. Para indicar que um parâmetro é posicional, você pode usar o caractere de barra (/) na lista de parâmetros.

Aqui está um exemplo de função com parâmetros posicionais:

```python
def calcular_potencia(x, y, /):
    return x ** y

print(calcular_potencia(2, 3))  # Saída: 8
```

Neste exemplo, a função `calcular_potencia` possui dois parâmetros posicionais, `x` e `y`. Você só pode passar valores para esses parâmetros na ordem correta. Tentar passar um valor por nome resultará em um erro.

### **Keyword-Only Arguments (`*`)**

Os argumentos somente por palavra-chave permitem que os argumentos sejam especificados apenas usando a sintaxe de nome de argumento (palavra-chave), ou seja, não podem ser passados por posição. Isso significa que eles devem ser fornecidos na forma `nome=valor` ao chamar a função. Para indicar que um parâmetro é somente por palavra-chave, você pode usar o caractere de asterisco (_) na lista de parâmetros.

Aqui está um exemplo de função com argumentos somente por palavra-chave:

```python
def saudar(nome, /, *, saudacao="Olá"):
    print(f"{saudacao}, {nome}!")

saudar("João")  # Saída: Olá, João!
saudar("Maria", saudacao="Oi")  # Saída: Oi, Maria!
```

Neste exemplo, a função `saudar` tem um parâmetro posicional `nome`, seguido por um parâmetro nomeado `saudacao`. O parâmetro `saudacao` só pode ser especificado usando o nome do argumento, mesmo que venha após o parâmetro posicional `nome`.

O uso de parâmetros posicionais e argumentos somente por palavra-chave pode ajudar a melhorar a clareza e a intenção do código, tornando mais explícito como os argumentos devem ser passados para uma função.

Lembre-se de que o uso desses recursos é opcional e depende do design da sua função e da necessidade de controle sobre como os argumentos são passados.
