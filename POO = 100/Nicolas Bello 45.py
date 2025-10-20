print("--- Demostración de Closures y Funciones de Orden Superior ---")

def aplicar_operacion(operacion):
    def ejecutar_operacion(a, b):
        return operacion(a, b)
    return ejecutar_operacion

def sumar(x, y):
    return x + y

sumador = aplicar_operacion(sumar)
print(f"Usando sumador(10, 5): {sumador(10, 5)}")

def multiplicar(x, y):
    return x * y

multiplicador = aplicar_operacion(multiplicar)
print(f"Usando multiplicador(10, 5): {multiplicador(10, 5)}")

print("\n--- Demostración de Closures ---")

def crear_saludador(prefijo_saludo):
    def saludar(nombre):
        return f"{prefijo_saludo}, {nombre}!"
    return saludar

saludar_hola = crear_saludador("Hola")
print(f"Usando saludar_hola('Alice'): {saludar_hola('Alice')}")

saludar_que_tal = crear_saludador("¿Qué tal")
print(f"Usando saludar_que_tal('Bob'): {saludar_que_tal('Bob')}")

def crear_contador():
    conteo = 0
    def incrementar():
        nonlocal conteo
        conteo += 1
        return conteo
    return incrementar

contador1 = crear_contador()
contador2 = crear_contador()

print(f"Contador 1: {contador1()}")
print(f"Contador 1: {contador1()}")
print(f"Contador 2: {contador2()}")
print(f"Contador 1: {contador1()}")
print(f"Contador 2: {contador2()}")

print("--- Fin de la demostración de Closures y Funciones de Orden Superior ---")
