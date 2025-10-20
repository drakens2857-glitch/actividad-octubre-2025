clave = "python"
intentos = ["admin", "1234", "python"]
for i, intento in enumerate(intentos, 1):
    if intento == clave:
        print(f"Acceso concedido en intento {i}")
        break
else:
    print("Acceso denegado")
