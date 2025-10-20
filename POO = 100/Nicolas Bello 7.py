class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar_libro(self):
        if self.disponible:
            self.disponible = False
            return f"'{self.titulo}' ha sido prestado."
        else:
            return f"'{self.titulo}' no está disponible para préstamo en este momento."

    def devolver_libro(self):
        if not self.disponible:
            self.disponible = True
            return f"'{self.titulo}' ha sido devuelto."
        else:
            return f"'{self.titulo}' ya está en la biblioteca."

    def mostrar_estado(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Libro: '{self.titulo}' de {self.autor} | Estado: {estado}"


libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
print(libro1.mostrar_estado())
print(libro1.prestar_libro())
print(libro1.mostrar_estado())
print(libro1.prestar_libro())
print(libro1.devolver_libro())
print(libro1.mostrar_estado())
print(libro1.devolver_libro())

libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")
print(libro2.mostrar_estado())
print(libro2.prestar_libro())
print(libro2.mostrar_estado())
