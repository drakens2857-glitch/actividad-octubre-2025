acciones = [10, -5, 15, -10, 20]
total = 0
penalizacion = 0
for a in acciones:
    if a < 0:
        penalizacion += abs(a) * 0.5
    total += a
print(f"Total: {total}, Penalización: {penalizacion}")
