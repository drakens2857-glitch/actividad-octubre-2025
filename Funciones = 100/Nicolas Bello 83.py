valores = [5, 10, 15, 20, 25]
umbral = 40
suma = 0
for v in valores:
    suma += v
    if suma > umbral:
        break
print(suma)
