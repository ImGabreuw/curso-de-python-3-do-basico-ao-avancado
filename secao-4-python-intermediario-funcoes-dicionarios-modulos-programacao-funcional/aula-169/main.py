# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(list1, list2):
    smaller, bigger = (list1, list2) if len(list1) <= len(list2) else (list2, list1)
    result = []

    for index, element in enumerate(smaller):
        result.append((element, bigger[index]))

    return result


print(
    zipper(
        ['Salvador', 'Ubatuba', 'Belo Horizonte'],
        ['BA', 'SP', 'MG', 'RJ']
    )
)

    