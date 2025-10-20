print("--- Demostración de Generadores y Yield en Python ---")

def generador_numeros(n):
    print("Iniciando generador_numeros...")
    i = 0
    while i < n:
        yield i
        i += 1
    print("Generador_numeros finalizado.")

mi_generador = generador_numeros(5)
print("Objeto generador creado:", mi_generador)
print("Iterando sobre el generador:")
for num in mi_generador:
    print(f"Obtenido: {num}")

print("\n--- Generador para números pares ---")

def generador_pares(limite):
    print("Iniciando generador_pares...")
    num = 0
    while num <= limite:
        if num % 2 == 0:
            yield num
        num += 1
    print("Generador_pares finalizado.")

for par in generador_pares(10):
    print(f"Par: {par}")

print("\n--- Generador para procesar un archivo grande (simulado) ---")

def leer_archivo_linea_por_linea(nombre_archivo_simulado):
    print(f"Abriendo archivo simulado: {nombre_archivo_simulado}")
    lineas_simuladas = [
        "Esta es la linea 1.",
        "La linea 2 contiene algo mas.",
        "Finalmente, la linea 3."
    ]
    for i, linea in enumerate(lineas_simuladas):
        yield f"({i+1}) {linea.strip()}"
    print(f"Cerrando archivo simulado: {nombre_archivo_simulado}")

for linea_leida in leer_archivo_linea_por_linea("datos_grandes.txt"):
    print(f"Procesando: {linea_leida}")

print("--- Fin de la demostración de Generadores y Yield ---")
