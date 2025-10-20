class Estanteria:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_por_genero(self, genero):
        return [l for l in self.libros if l.genero == genero]

    def disponibles(self):
        return [l for l in self.libros if l.disponible]
