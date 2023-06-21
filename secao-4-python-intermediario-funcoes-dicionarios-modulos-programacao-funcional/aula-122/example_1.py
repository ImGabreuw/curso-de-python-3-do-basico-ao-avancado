d1 = {
  "chave1": "valor1",
  "chave2": "valor2",
  "chave3": [1, 2, 3],
}
d2 = d1.copy()

d2["chave1"] = "valor2"

print(d1["chave1"]) # valor1
print(d2["chave1"]) # valor2

d2["chave3"][0] = 5

print(d1["chave3"]) # [1, 2]