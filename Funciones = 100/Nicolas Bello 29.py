lista = [5, 10, 20, 15, 30]
umbral = 40
suma = 0
for x in lista:
    suma += x
    if suma > umbral:
        break
print(suma)
