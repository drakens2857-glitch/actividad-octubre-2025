from datetime import datetime, timedelta

class ReservaLibro:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_reserva = datetime.now()
        self.expira = self.fecha_reserva + timedelta(days=3)

    def esta_activa(self):
        return datetime.now() < self.expira
