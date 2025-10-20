class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Un animal hace un sonido."

    def moverse(self):
        return f"{self.nombre} se está moviendo."


class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau, guau!"

    def ladrar(self):
        return f"{self.nombre} está ladrando."


class Gato(Animal):
    def __init__(self, nombre, color_pelaje):
        super().__init__(nombre)
        self.color_pelaje = color_pelaje

    def hacer_sonido(self):
        return "Miau, miau."

    def maullar(self):
        return f"{self.nombre} está maullando."


animal_generico = Animal("Bicho")
print(animal_generico.hacer_sonido())
print(animal_generico.moverse())

perro1 = Perro("Fido", "Golden Retriever")
print(perro1.hacer_sonido())
print(perro1.moverse())
print(perro1.ladrar())

gato1 = Gato("Garfield", "Naranja")
print(gato1.hacer_sonido())
print(gato1.moverse())
print(gato1.maullar())
