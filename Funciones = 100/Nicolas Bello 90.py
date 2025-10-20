lista = [1, 2, 2, 3, 4, 4, 5]
unicos = [x for x in lista if lista.count(x) == 1]
print(unicos)
