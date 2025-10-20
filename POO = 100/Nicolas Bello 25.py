class InstrumentoMusical:
    def __init__(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del instrumento no puede estar vacío.")
        self.nombre = nombre

    def tocar(self):
        raise NotImplementedError("Las subclases deben implementar el método 'tocar()'")


class Guitarra(InstrumentoMusical):
    def __init__(self):
        super().__init__("Guitarra")

    def tocar(self):
        return f"{self.nombre} suena con un rasgueo armónico."


class Piano(InstrumentoMusical):
    def __init__(self):
        super().__init__("Piano")

    def tocar(self):
        return f"{self.nombre} produce melodías al pulsar sus teclas."


class Bateria(InstrumentoMusical):
    def __init__(self):
        super().__init__("Batería")

    def tocar(self):
        return f"{self.nombre} marca el ritmo con golpes potentes."


def hacer_musica(instrumento):
    print(f"El {instrumento.nombre} está sonando: {instrumento.tocar()}")


guitarra = Guitarra()
piano = Piano()
bateria = Bateria()

hacer_musica(guitarra)
hacer_musica(piano)
hacer_musica(bateria)

orquesta = [Guitarra(), Piano(), Bateria(), Guitarra()]
print("\nLa orquesta comienza a tocar:")
for inst in orquesta:
    hacer_musica(inst)
