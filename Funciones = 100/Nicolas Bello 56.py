lista = [1, 2, 3, 4, 5]
n = 2
for _ in range(n):
    lista = [lista[-1]] + lista[:-1]
print(lista)
