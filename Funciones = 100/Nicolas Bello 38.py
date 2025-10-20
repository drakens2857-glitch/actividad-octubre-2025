for i in range(8):
    fila = ""
    for j in range(8):
        fila += "⬛" if (i + j) % 2 == 0 else "⬜"
    print(fila)
