# TEORIA: subprocess para executando programas e comandos externos

O módulo `subprocess` do Python serve par executar processos e comandos externos no seu código.

A forma mais simples de atingir tal objetivo é a partir da função `run()`. Abaixo estão listados os principais argumentos dessa função:

- `stdout`: redirecionamento da saída

- `stdin`: redirecionamento da entrada

- `stderr`: redirecionamento de erros

- `capture_output`: captura a saída ou erros para serem utilizados posteriormente

- `text`: se for `True`, as entradas e saídas serão tradadas como texto e automaticamente codificadas ou decodificadas com o conjunto de caracteres padrão do sistema operacional (geralmente é UTF-8)

  > Por padrão, ao capturar a saída da execução do subprocesso, a função `run` retorna no formato de bytes.

- `shell`: Se for `True`, será concedido o acesso ao shell do sistema operacional para o seu programa. Caso essa opção seja habilitada, é recomendado enviar o comando e os argumentos juntos.

- `executable`: pode ser usado para especificar o caminho do executável que iniciará o subprocesso.

Os retornos esperados são:

- `stdout`: saída do comando executado

- `stderr`: erro (caso for lançado)

- `returncode`: código `0` indica sucesso e os demais códigos representam erro

- `args`: os argumentos utilizados na execução do comando

> **IMPORTANTE**: a codificação de caracteres do Windows pode ser diferente de UTF-8, então é recomendado usar _CP1252_, _CP852_, _CP850_. Já em sistemas Linux e Mac, é preferível utilizar `uft_8`

Aqui está um exemplo utilizando a função `subprocess.run()` para executar o comando `ping`:

```python
import subprocess
import sys

cmd = ['ping', '127.0.0.1', "-c", "4"]
encoding = 'utf_8'
system = sys.platform

if system == "win32":
    cmd = ['ping', '127.0.0.1']
    encoding = 'cp850'


proc = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding=encoding,
    shell=True,
)

print()
print(proc.stdout)
```

Como pode ver, o comando no Windows é apenas `ping 127.0.0.1`, pois por padrão o limite de pings é definido como 4 a partir da opção `-c`.