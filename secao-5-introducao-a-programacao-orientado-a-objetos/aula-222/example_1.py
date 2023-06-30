class A:
  atributo_a = "Valor A"

  def metodo(self):
    print("A")

class B(A):
  atributo_b = "Valor B"

  def metodo(self):
    print("B")

class C(B):
  atributo_c = "Valor C"

  def metodo(self):
    print("C")
    super().metodo() # Equivalente à "super(B, self)"
    super(B, self).metodo()

c = C()
c.metodo()
print(C.mro())