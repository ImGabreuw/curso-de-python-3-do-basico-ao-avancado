# with open (context manager) e métodos úteis do TextIOWrapper

### **Método: `write()`**

O método `write()` é usado para escrever dados em um arquivo. Ele aceita uma string como argumento e escreve essa string no arquivo.

Exemplo:

```python
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Esta é uma linha de exemplo.\n")
```

Neste exemplo, usamos o modo "w" para abrir o arquivo em modo de escrita. As chamadas `write()` gravam as strings no arquivo.

### **Método: `read()`**

O método `read()` é usado para ler o conteúdo de um arquivo. Ele retorna uma string contendo o conteúdo lido.

Exemplo:

```python
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

Neste exemplo, usamos o modo "r" para abrir o arquivo em modo de leitura. A chamada `read()` lê todo o conteúdo do arquivo e armazena na variável `conteudo`, que é então impressa.

### **Método: `seek()`**

O método `seek()` é usado para mover o "ponteiro" do arquivo para uma posição específica. Ele aceita um argumento numérico que representa a nova posição do ponteiro.

Exemplo:

```python
with open("exemplo.txt", "w+") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")

    arquivo.seek(0, 0)

    conteudo = arquivo.read()
    print(conteudo)
```

Neste exemplo, a chamada `seek(0, 0)` move o ponteiro para o topo do arquivo e no começo da linha. A chamada subsequente `read()` lê o conteúdo do arquivo a partir dessa posição.

### **Método: `readline()`**

O método `readline()` é usado para ler uma linha do arquivo. Ele retorna uma string contendo a linha atual e move o ponteiro para a próxima linha.

Exemplo:

```python
with open("exemplo.txt", "r") as arquivo:
    linha1 = arquivo.readline()
    linha2 = arquivo.readline()
    print(linha1)
    print(linha2)
```

Neste exemplo, as chamadas `readline()` lêem as duas primeiras linhas do arquivo e armazenam nas variáveis `linha1` e `linha2`. As linhas são então impressas na saída.

### **Método: `readlines()`**

O método `readlines()` é usado para ler todas as linhas de um arquivo como uma lista de strings. Cada string representa uma linha do arquivo.

Exemplo:

```python
with open("exemplo.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha, end="")
        # OU
        # print(linha.strip())
```

Neste exemplo, a chamada `readlines()` lê todas as linhas do arquivo e as armazena na lista `linhas`. Em seguida, usamos um loop para imprimir cada linha individualmente e para remover a quebra de linha 2 vezes (uma do `\n` contida em `linha` e a outra do `print()`), você pode especificar o `end` como uma string vazia ou utilizar o `strip()`, uma vez que a quebra de linha (`\n`) é interpretado como espaço em branco.

### **Método: `writelines()`**

O método `writelines()` é usado para escrever várias linhas em um arquivo. Ele aceita uma lista de strings, onde cada string representa uma linha.

Exemplo:

```python
linhas = ["Primeira linha\n", "Segunda linha\n", "Terceira linha\n"]
with open("exemplo.txt", "w") as arquivo:
    arquivo.writelines(linhas)
```

Neste exemplo, usamos a lista `linhas` para escrever várias linhas no arquivo usando o método `writelines()`.
