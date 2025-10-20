contador = 0
for i in range(100, 200):
    if len(set(str(i))) < len(str(i)):
        contador += 1
print(contador)
