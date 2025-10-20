lista = [1, 2, 2, 3, 4, 4, 5]
unicos = []
for x in lista:
    if lista.count(x) == 1:
        unicos.append(x)
print(unicos)
