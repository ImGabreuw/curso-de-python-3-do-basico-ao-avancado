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