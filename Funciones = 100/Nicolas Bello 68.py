clave = "backend"
intentos = ["admin", "1234", "backend"]
for intento in intentos:
    if intento == clave:
        print("Acceso concedido")
        break
else:
    print("Acceso denegado")
