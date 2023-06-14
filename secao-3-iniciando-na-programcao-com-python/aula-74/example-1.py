texto = "Luiz"

print(texto.__iter__())
print(iter(texto))

texto = texto.__iter__()

print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())