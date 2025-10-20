contador = 0
for i in range(100, 200):
    if sum(int(d) for d in str(i)) % 3 == 0:
        contador += 1
print(contador)
