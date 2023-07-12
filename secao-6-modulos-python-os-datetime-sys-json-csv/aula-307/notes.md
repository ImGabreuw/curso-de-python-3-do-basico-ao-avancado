# argparse.ArgumentParser para argumentos mais complexos

A classe `ArgumentParser` do módulo `argparse` é recomendado para programas de linha de comando, pois eles requerem um tratamento mais refinado dos argumentos passados ao executar um arquivo Python.

```python
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-b")
args = parser.parse_args()

if args.b is None:
  print("Você não passou o valor de 'b'.")
else:
  print(args.b)
```

Ao executar o arquivo acima:

```console
$ python example_1.py -b 123
```

Temos a seguinte saída:

```
123
```

Além disso, você pode configurar as opções (_flags_) do seu comando:

- `help`: descrição sobre a função dessa opção

- `type`: o tipo Python do valor dessa opção

- `metavar`: o tipo exibido para o usuário

- `default`: definir o valor padrão

- `required`: forçar o usuário a passar um valor

```python
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
  "-b", "--basic",
  help="Mostra 'Olá mundo' na tela",
  type=str,
  metavar="STRING",
  default="Olá mundo",
  # required=True
)
args = parser.parse_args()

print(args.basic)
```

```console
$ python example_2.py
> Olá mundo
```

```console
$ python example_2.py -b "123"
> 123
```

```console
$ python example_2.py --basic "123"
> 123
```

> **OBS**: `--basic` é a forma verbosa (_verbose_) da opção `-b` e é uma boa prática defini-la, pois deixa o código mais legível ao obter o valor dessa opção com `args = parser.parse_args()`.

Outra coisa que é possível fazer com essa classe é adicionar listas de valores para uma opção do comando:

```python
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
  "-b", "--basic",
  help="Mostra 'Olá mundo' na tela",
  type=str,
  metavar="STRING",
  default="Olá mundo",
  nargs="+"
)
args = parser.parse_args()

print(args.basic)
```

```console
$ python example_3.py -b "Olá" "Mundo"
> ['Olá', 'Mundo']
```

Ou caso você prefira concatenar os valores das mesmas opções, pode usar o argumento nomeado `action="append"`:

```python
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
  "-b", "--basic",
  help="Mostra 'Olá mundo' na tela",
  metavar="STRING",
  action="append"
)
args = parser.parse_args()

print(args.basic)
```

```console
$ python example_4.py -b "Olá" -b "Mundo"
> ['Olá', 'Mundo']
```

Já para ter uma opções com o comportamento de `true` ou `false`, você pode usar o argumento nomeado `action="store_true"`:

```python
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
  "-b", "--basic",
  help="comportamento de switch",
  action="store_true"
)
args = parser.parse_args()

print(args.basic)
```

```console
$ python example_5.py
> False
```

```console
$ python example_5.py -b
> True
```
