# sys.argv - Executando arquivos com argumentos no sistema

O variável `argv` do módulo `sys` do Python, retorna uma lista contendo os argumentos ao executar módulo Python, mas o 1º argumento sempre será o caminho do script. Veja o exemplo abaixo:

```python
# main.py
import sys

argumentos = sys.argv

print(f"Você passou os argumentos: {argumentos[1:]}")
```

```console
$ python main.py "argumento1" "argumento2"
```

Saída contendo os argumentos no sistema:

```
Você passou os argumentos: ["main.py", "argumento1", "argumento2"]
```
