lista = [1, 2, 2, 3, 4, 4, 4, 5]
for i in range(1, len(lista)):
    if lista[i] == lista[i - 1]:
        print(f"Duplicado consecutivo: {lista[i]}")
