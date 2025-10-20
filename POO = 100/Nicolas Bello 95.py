class EvaluacionLibro:
    def __init__(self):
        self.evaluaciones = {}

    def agregar_evaluacion(self, libro, usuario, puntuacion):
        if libro not in self.evaluaciones:
            self.evaluaciones[libro] = []
        self.evaluaciones[libro].append({'usuario': usuario, 'puntuacion': puntuacion})

    def promedio_libro(self, libro):
        if libro not in self.evaluaciones:
            return 0
        total = sum(e['puntuacion'] for e in self.evaluaciones[libro])
        return total / len(self.evaluaciones[libro])
