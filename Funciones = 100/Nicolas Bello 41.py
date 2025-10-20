clave_correcta = "python123"
intentos = ["admin", "1234", "python123"]
for intento in intentos:
    if intento == clave_correcta:
        print("Acceso concedido")
        break
else:
    print("Acceso denegado")
