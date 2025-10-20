class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Las subclases deben implementar el método 'hacer_sonido()'")


class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau! ¡Guau!"


class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau! ¡Miau!"


class Vaca(Animal):
    def hacer_sonido(self):
        return "¡Muuuu! ¡Muuuu!"


def escuchar_animal(animal):
    print(f"El animal hace: {animal.hacer_sonido()}")


perro = Perro()
gato = Gato()
vaca = Vaca()

escuchar_animal(perro)
escuchar_animal(gato)
escuchar_animal(vaca)

animales_en_granja = [Perro(), Gato(), Vaca(), Perro(), Gato()]
print("\nLos animales de la granja hacen sus sonidos:")
for animal in animales_en_granja:
    escuchar_animal(animal)
