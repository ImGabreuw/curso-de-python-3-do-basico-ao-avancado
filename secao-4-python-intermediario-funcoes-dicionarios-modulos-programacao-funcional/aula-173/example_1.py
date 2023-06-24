from itertools import count

c = count()
r = range(0, 10)

print("count têm '__iter__'", hasattr(c, "__iter__"))
print("count têm '__next__'", hasattr(c, "__next__"))
print("range têm '__iter__'", hasattr(r, "__iter__"))
print("range têm '__next__'", hasattr(r, "__next__"))