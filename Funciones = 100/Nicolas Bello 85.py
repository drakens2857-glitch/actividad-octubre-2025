contador = 0
for i in range(100, 200):
    if all(int(d) % 2 == 0 for d in str(i)):
        contador += 1
print(contador)
