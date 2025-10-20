inventario = {"manzanas": 10, "bananos": 5}
movimientos = [("manzanas", -3), ("bananos", 2), ("manzanas", 4)]
for producto, cambio in movimientos:
    inventario[producto] += cambio
print(inventario)
