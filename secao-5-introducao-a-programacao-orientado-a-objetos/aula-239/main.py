class A:
  def __init__(self):
    print(f"Inicializando {type(self).__name__}...")
  
  def __repr__(self):
    return f"{type(self).__name__}()"

a = object.__new__(A)
a.__init__()

print(a)