lista = [1, 2, 3, 2, 4, 1, 5, 3]
repetidos = set()
vistos = set()
for x in lista:
    if x in vistos:
        repetidos.add(x)
    vistos.add(x)
print(len(repetidos))
