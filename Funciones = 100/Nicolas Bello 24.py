lista = list(range(1, 51))
contador = 0
for x in lista:
    if x % 3 == 0 or x % 5 == 0:
        contador += 1
print(contador)
