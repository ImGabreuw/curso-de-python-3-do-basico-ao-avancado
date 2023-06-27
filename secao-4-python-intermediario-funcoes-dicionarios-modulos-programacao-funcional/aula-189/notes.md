# os.remove, os.unlink e os.rename - apagando, renomeando e movendo arquivos

No Python, existem duas formas de remover um arquivo: usando `os.unlink()` ou `os.remove()`. Ambos os métodos recebem como argumento o caminho relativo ou absoluto do arquivo a ser removido.

Exemplo usando `os.remove()`:
```python
import os

caminho = "exemplo.txt"
os.remove(caminho)
```

Exemplo usando `os.unlink()`:
```python
import os

caminho = "exemplo.txt"
os.unlink(caminho)
```

Ambos os métodos têm o mesmo efeito de remover o arquivo especificado pelo caminho.

No caso de renomear ou mover um arquivo, você pode utilizar o método `os.rename()`, que recebe como argumento o caminho do arquivo e o novo nome (para renomear) ou o novo caminho (para mover).

Exemplo de renomeação do arquivo:
```python
import os

caminho = "exemplo.txt"
os.rename(caminho, "exemplo_1.txt")
```

Neste exemplo, o arquivo "exemplo.txt" é renomeado para "exemplo_1.txt".

Exemplo de movimentação do arquivo para um novo diretório:
```python
import os

caminho = "exemplo.txt"
os.rename(caminho, "./diretorio/exemplo.txt")
```

Neste exemplo, o arquivo "exemplo.txt" é movido para o diretório "./diretorio".

O método `os.rename()` é versátil e pode ser usado tanto para renomear quanto para mover arquivos.

Lembre-se de que, ao usar os métodos de remoção (`os.unlink()` ou `os.remove()`) ou o método `os.rename()`, é importante ter cuidado para evitar a exclusão ou renomeação acidental de arquivos importantes. Sempre confirme o caminho e os nomes dos arquivos antes de executar essas operações.