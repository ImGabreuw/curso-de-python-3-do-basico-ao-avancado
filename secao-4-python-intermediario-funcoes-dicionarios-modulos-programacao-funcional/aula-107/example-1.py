def soma (x, y, z = 0):
  if z:
    print(f"{x=} {y=} {z=}", x + y + z)  
  else:
    print(f"{x=} {y=}", x + y)  

soma(1, 2)
soma(1, 2, 3)