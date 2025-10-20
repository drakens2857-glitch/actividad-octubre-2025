class Instrumento:
    def __init__(self, tipo):
        self.tipo = tipo

    def tocar(self):
        return f"El {self.tipo} está produciendo un sonido genérico."

    def afinar(self):
        return f"Afinando el {self.tipo}."

    def mostrar_info(self):
        return f"Este es un instrumento de tipo {self.tipo}."


class Piano(Instrumento):
    def __init__(self, num_teclas, marca):
        super().__init__("Piano")
        self.num_teclas = num_teclas
        self.marca = marca

    def tocar(self):
        return f"El {self.marca} Piano con {self.num_teclas} teclas suena como una melodía armoniosa."

    def pisar_pedal(self):
        return f"El pedal del {self.marca} Piano está siendo pisado."

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Marca: {self.marca}, Teclas: {self.num_teclas}."


class Guitarra(Instrumento):
    def __init__(self, num_cuerdas, tipo_acustica):
        super().__init__("Guitarra")
        self.num_cuerdas = num_cuerdas
        self.tipo_acustica = tipo_acustica

    def tocar(self):
        return f"La Guitarra {self.tipo_acustica} de {self.num_cuerdas} cuerdas rasguea una alegre tonada."

    def cambiar_cuerda(self):
        return f"Cambiando una cuerda de la Guitarra {self.tipo_acustica}."

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Cuerdas: {self.num_cuerdas}, Tipo: {self.tipo_acustica}."


instrumento_generico = Instrumento("Genérico")
print(instrumento_generico.mostrar_info())
print(instrumento_generico.tocar())
print(instrumento_generico.afinar())

piano1 = Piano(88, "Yamaha")
print(piano1.mostrar_info())
print(piano1.tocar())
print(piano1.afinar())
print(piano1.pisar_pedal())

guitarra1 = Guitarra(6, "Acústica")
print(guitarra1.mostrar_info())
print(guitarra1.tocar())
print(guitarra1.afinar())
print(guitarra1.cambiar_cuerda())
