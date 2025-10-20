class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= 0:
            return "Cantidad inválida para vender."
        if cantidad > self.stock:
            return f"No hay suficiente stock para vender {cantidad} unidades."
        self.stock -= cantidad
        total = cantidad * self.precio
        return f"Venta realizada: {cantidad} unidades de {self.nombre}. Total: ${total}. Stock restante: {self.stock}"

    def reponer(self, cantidad):
        if cantidad <= 0:
            return "Cantidad inválida para reponer."
        self.stock += cantidad
        return f"Stock actualizado: {self.stock} unidades de {self.nombre}"

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio}, Stock: {self.stock}"
