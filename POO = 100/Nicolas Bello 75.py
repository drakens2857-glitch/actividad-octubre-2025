class UsuarioBiblioteca:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.historial = []
        self.sanciones = 0

    def registrar_prestamo(self, libro):
        self.historial.append(libro)

    def aplicar_sancion(self):
        self.sanciones += 1

    def nivel_actividad(self):
        return "Activo" if len(self.historial) > 5 else "Bajo"
