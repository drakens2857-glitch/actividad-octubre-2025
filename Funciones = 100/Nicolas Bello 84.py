n = 5
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(1 if j <= i else 0)
    print(fila)
