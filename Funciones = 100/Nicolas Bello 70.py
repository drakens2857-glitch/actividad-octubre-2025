lista = [1, 2, 2, 3, 4, 4, 5]
frecuencia = {}
for x in lista:
    frecuencia[x] = frecuencia.get(x, 0) + 1
unicos = [k for k, v in frecuencia.items() if v == 1]
print(unicos)
