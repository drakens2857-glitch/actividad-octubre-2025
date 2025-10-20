class ClubLectura:
    def __init__(self, nombre):
        self.nombre = nombre
        self.reuniones = []

    def agendar_reunion(self, fecha, libro):
        self.reuniones.append({'fecha': fecha, 'libro': libro})

    def proximas_reuniones(self):
        return sorted(self.reuniones, key=lambda r: r['fecha'])
