class DificultadLectura:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, dificultad):
        self.libros.append({'titulo': titulo, 'dificultad': dificultad})

    def libros_por_nivel(self, nivel):
        return [l['titulo'] for l in self.libros if l['dificultad'] == nivel]
