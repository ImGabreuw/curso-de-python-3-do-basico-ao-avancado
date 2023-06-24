# O ponto de vista do __main__ pode te confundir em módulos e pacotes Python

Em em cenário com um pacote contendo os módulos `modulo_a.py` e `modulo_b.py`:

```
meu_pacote\
  modulo_a.py
  modulo_b.py
main.py
```

As importações entre o `modulo_a.py` e `modulo_b.py` devem ser relativas ao ponto de entrada do programa.

Caso o ponto de entrada for o `modulo_b.py`, o exemplo abaixo funcionará normalmente.

```python
# modulo_a.py

def funcao():
  print("Função")

# modulo_b.py
from modulo_a import funcao 

def outra_funcao():
  funcao()

outra_funcao()
# Saída: Função
```

Entretanto, se o ponto de entrada for alterada para `main.py`, então o código acima não funcionará mais.

```python
# modulo_a.py

def funcao():
  print("Função")

# modulo_b.py
from modulo_a import funcao 

def outra_funcao():
  funcao()


# main.py
from meu_pacote.modulo_b import outra_funcao

outra_funcao()
# Saída: ModuleNotFoundError: No module named "modulo_a"
```

O erro `ModuleNotFoundError` foi lançado, pois o Python, por padrão, não verifica a existência de módulos Python nos níveis acima da hierarquia de arquivos em relação ao ponto de entrada (`main.py`).

Dessa forma, é necessário realizar os `import`s sempre tendo como base o ponto de entrada.

```python
# modulo_a.py

def funcao():
  print("Função")

# modulo_b.py
from meu_pacote.modulo_a import funcao 

def outra_funcao():
  funcao()


# main.py
from meu_pacote.modulo_b import outra_funcao

outra_funcao()
# Saída: "Função"
```