# Operadores relacionais (de comparação) em Python

Todos os operadores relacionais retornam um valor booleano (`True` ou `False`).

| Operador |  Significado   | Exemplo (`True`) | Exemplo (`False`) |
| :------: | :------------: | :--------------: | :---------------: |
|   `>`    |     maior      |     `2 > 1`      |      `2 > 3`      |
|   `>=`   | maior ou igual |     `2 >= 2`     |     `2 >= 3`      |
|   `<`    |     menor      |     `1 < 2`      |      `2 < 1`      |
|   `<=`   | menor ou igual |     `1 <= 1`     |     `3 <= 2`      |
|   `==`   |     igual      |   `"a" == "a"`   |   `"a" == "A"`    |
|   `!=`   |   diferente    |   `"a" != "b"`   |   `"a" != "a"`    |

> ## **Executar um módulo no modo interativo**

Como foi visto anteriormente, todo arquivo `.py` é tratado como um módulo. Desse modo, para executar um módulo com o Shell interativo, basta utilizar o seguinte comando:

### **Sintaxe**

```bash
$ python -i <arquivo .py>
```

### **Exemplo**

```bash
$ python -i main.py
>>> # comando Python
```

**OBS**: caso o arquivo `main.py` seja alterado é necessário executar novamente esse comando.
