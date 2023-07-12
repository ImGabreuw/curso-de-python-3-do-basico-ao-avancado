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