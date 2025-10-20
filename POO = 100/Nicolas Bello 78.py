class Turno:
    def __init__(self, usuario, prioridad=False):
        self.usuario = usuario
        self.prioridad = prioridad

class GestorTurnos:
    def __init__(self):
        self.turnos = []

    def agregar_turno(self, turno):
        self.turnos.append(turno)
        self.turnos.sort(key=lambda t: not t.prioridad)

    def siguiente(self):
        return self.turnos.pop(0) if self.turnos else None
