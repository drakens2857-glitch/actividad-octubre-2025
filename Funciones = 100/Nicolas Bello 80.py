from collections import Counter
lista = [1, 2, 2, 3, 4, 4, 5]
frecuencia = Counter(lista)
unicos = [k for k, v in frecuencia.items() if v == 1]
print(unicos)
