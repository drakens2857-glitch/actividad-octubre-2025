nodos = 4
matriz = [[0]*nodos for _ in range(nodos)]
aristas = [(0,1), (1,2), (2,3)]
for a, b in aristas:
    matriz[a][b] = 1
    matriz[b][a] = 1
for fila in matriz:
    print(fila)
