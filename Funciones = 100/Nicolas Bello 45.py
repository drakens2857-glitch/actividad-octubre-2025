estados = ["verde", "amarillo", "rojo"]
i = 0
while True:
    print(f"Estado: {estados[i]}")
    i = (i + 1) % len(estados)
    if i == 0:
        break
