contador = 0
for i in range(100, 1000):
    s = str(i)
    if s[0] >= s[1] >= s[2]:
        contador += 1
print(contador)
