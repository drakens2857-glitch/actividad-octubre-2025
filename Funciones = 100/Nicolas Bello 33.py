clave = "backend"
intentos = ["admin", "1234", "backend"]
for intento in intentos:
    if intento == clave:
        print("Acceso permitido")
        break
else:
    print("Acceso denegado")
