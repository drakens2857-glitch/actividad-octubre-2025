class LecturaCompartida:
    def __init__(self):
        self.sesiones = []

    def crear_sesion(self, libro, usuarios):
        self.sesiones.append({'libro': libro, 'usuarios': usuarios, 'progreso': 0})

    def avanzar_lectura(self, libro, paginas):
        for sesion in self.sesiones:
            if sesion['libro'] == libro:
                sesion['progreso'] += paginas
