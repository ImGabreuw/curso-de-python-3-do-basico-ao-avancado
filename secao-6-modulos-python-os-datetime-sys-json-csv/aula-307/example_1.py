from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-b")
args = parser.parse_args()

if args.b is None:
  print("Você não passou o valor de 'b'.")
else:
  print(args.b)