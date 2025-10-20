lista = [3, 1, 2, 5, 4]
n = 5
completo = True
for i in range(1, n + 1):
    if i not in lista:
        completo = False
        break
print(completo)
