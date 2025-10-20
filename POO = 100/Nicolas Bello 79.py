class Bibliotecario:
    def __init__(self, nombre):
        self.nombre = nombre

    def modificar_stock(self, libro, cantidad):
        libro.stock += cantidad

    def generar_reporte(self, prestamos):
        return f"{self.nombre} generó reporte de {len(prestamos)} préstamos"
