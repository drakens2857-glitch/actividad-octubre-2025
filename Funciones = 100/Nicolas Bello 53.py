valores = [5, 10, 15, 20, 25]
limite = 40
suma = 0
for v in valores:
    if suma + v > limite:
        break
    suma += v
print(suma)
