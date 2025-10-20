from functools import reduce

print("--- Demostración de Map, Filter y Reduce en Python ---")

productos = [
    {'nombre': 'Laptop', 'precio': 1200, 'cantidad': 5},
    {'nombre': 'Mouse', 'precio': 25, 'cantidad': 20},
    {'nombre': 'Teclado', 'precio': 75, 'cantidad': 10},
    {'nombre': 'Monitor', 'precio': 300, 'cantidad': 3},
    {'nombre': 'Webcam', 'precio': 50, 'cantidad': 15}
]

nombres_mayusculas = list(map(lambda p: p['nombre'].upper(), productos))
print(f"Nombres de productos en mayúsculas: {nombres_mayusculas}")

valores_totales_por_producto = list(map(lambda p: p['precio'] * p['cantidad'], productos))
print(f"Valores totales por producto: {valores_totales_por_producto}")

productos_caros = list(filter(lambda p: p['precio'] > 100, productos))
print(f"Productos caros (precio > 100): {productos_caros}")

productos_en_stock = list(filter(lambda p: p['cantidad'] > 10, productos))
print(f"Productos con más de 10 unidades en stock: {productos_en_stock}")

valor_total_inventario = reduce(lambda total, p: total + (p['precio'] * p['cantidad']), productos, 0)
print(f"Valor total del inventario: ${valor_total_inventario}")

producto_mas_barato = reduce(lambda p1, p2: p1 if p1['precio'] < p2['precio'] else p2, productos)
print(f"Producto más barato: {producto_mas_barato}")

print("--- Fin de la demostración de Map, Filter y Reduce ---")
