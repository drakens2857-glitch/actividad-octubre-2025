acciones = [10, -5, 15, -20, 25]
total = 0
for a in acciones:
    if a < 0 and total + a < 0:
        continue
    total += a
print(total)
