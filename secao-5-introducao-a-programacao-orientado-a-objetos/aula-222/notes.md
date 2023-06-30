# (Parte 2) super e a sobreposição de membros em Python Orientado a Objetos

No Python, é possível executar o mesmo método de níveis hierárquicos diferentes em um sub classe, especificando explicitamente os argumentos do constructor da classe `super`. O método `super()` recebe como 1º argumento a super classe e no 2º a instância da sub classe.

Aqui está um exemplo para representar isso:

```python
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
# Saída:
# C
# B
# A
```

Uma forma de visualizar a hierarquia das classes é a partir do método de classe `mro()`.

O exemplo acima tem a seguinte hierarquia a partir da sub classe `C`

```python
C.mro() # Saída: [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
```