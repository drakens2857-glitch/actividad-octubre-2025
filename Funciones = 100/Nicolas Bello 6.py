matriz = [[i + j for j in range(4)] for i in range(4)]
suma = 0
for i in range(4):
    suma += matriz[i][i]
print(suma)
