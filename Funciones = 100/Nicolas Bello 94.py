n = 5
matriz = [[1 if j == n - i - 1 else 0 for j in range(n)] for i in range(n)]
for fila in matriz:
    print(fila)
