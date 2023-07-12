from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
  "-b", "--basic",
  help="comportamento de switch",
  action="store_true"
)
args = parser.parse_args()

print(args.basic)