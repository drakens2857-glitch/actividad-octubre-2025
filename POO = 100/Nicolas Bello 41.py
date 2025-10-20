from functools import reduce

print("--- Demostración de Funciones Lambda en Python ---")

suma = lambda a, b: a + b
print(f"Suma de 5 y 3: {suma(5, 3)}")

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x * x, numeros))
print(f"Cuadrados de {numeros}: {cuadrados}")

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares de {numeros}: {numeros_pares}")

personas = [
    {'nombre': 'Alice', 'edad': 30},
    {'nombre': 'Bob', 'edad': 25},
    {'nombre': 'Charlie', 'edad': 35}
]
personas_ordenadas_por_edad = sorted(personas, key=lambda p: p['edad'])
print(f"Personas ordenadas por edad: {personas_ordenadas_por_edad}")

producto_total = reduce(lambda acumulador, elemento: acumulador * elemento, numeros)
print(f"Producto de todos los números en {numeros}: {producto_total}")

print("--- Fin de la demostración de Funciones Lambda ---")
