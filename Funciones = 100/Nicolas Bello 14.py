cola = ["Ana", "Luis", "Carlos", "Marta"]
while cola:
    actual = cola.pop(0)
    print(f"Atendiendo a: {actual}")
    if actual == "Luis":
        print("Luis ha llegado tarde, se le vuelve a poner al final de la cola.")
        cola.append(actual)