# Recarregando módulos, importlib e singleton

Em Python, o módulo `importlib` é uma biblioteca padrão que fornece várias funções para recarregar módulos dinamicamente durante a execução do programa. Isso significa que você pode importar um módulo, fazer alterações no código-fonte desse módulo e, em seguida, recarregá-lo para usar as alterações atualizadas, sem precisar reiniciar o programa.

A função principal que você usará é `importlib.reload()`. Essa função permite recarregar um módulo específico. Aqui está um exemplo que ilustra como usá-la:

> **OBS**: ao realizar o `import` o Python cria uma única instância dessa biblioteca (padrão _singleton_)

Suponha que você tenha um módulo chamado `meu_modulo.py` com o seguinte código:

```python
# meu_modulo.py
def saudacao():
    print("Olá, mundo!")

mensagem = "Esta é uma mensagem de teste"
```

Em seu programa principal, você pode importar e usar esse módulo:

```python
import meu_modulo

meu_modulo.saudacao()  # Saída: Olá, mundo!
print(meu_modulo.mensagem)  # Saída: Esta é uma mensagem de teste
```

Agora, se você fizer alterações no código-fonte do `meu_modulo.py`, pode recarregá-lo usando `importlib.reload()`:

```python
import importlib
import meu_modulo

meu_modulo.saudacao()  # Saída: Olá, mundo!

# Faça alterações no código-fonte do meu_modulo.py

importlib.reload(meu_modulo)
meu_modulo.saudacao()  # Saída atualizada após as alterações
print(meu_modulo.mensagem)  # Saída atualizada após as alterações
```

Observe que para recarregar o módulo, você precisa importar novamente o módulo antes de usar `importlib.reload()`. Isso garantirá que as alterações sejam aplicadas corretamente.

Tenha em mente que o recarregamento de módulos não é muito utilizado devido ao possível alto custo, ao importar bibliotecas com várias sub bibliotecas. Entretanto, isso pode ser usado por exemplo quando você está no modo iterativo do Console Python (`python -i [módulo]`) e após a alteração de um módulo, você pode utilizar a função `importlib.reload()` para aplicar essa mudança na seção atual do Console Python, se precisar executar esse comando novamente.