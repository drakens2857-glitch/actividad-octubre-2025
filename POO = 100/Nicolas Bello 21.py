import math

class Forma:
    def area(self):
        raise NotImplementedError("Las subclases deben implementar el método 'area()'")


class Circulo(Forma):
    def __init__(self, radio):
        if not isinstance(radio, (int, float)) or radio <= 0:
            raise ValueError("El radio debe ser un número positivo.")
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Rectangulo(Forma):
    def __init__(self, base, altura):
        if not isinstance(base, (int, float)) or base <= 0:
            raise ValueError("La base debe ser un número positivo.")
        if not isinstance(altura, (int, float)) or altura <= 0:
            raise ValueError("La altura debe ser un número positivo.")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Triangulo(Forma):
    def __init__(self, base, altura):
        if not isinstance(base, (int, float)) or base <= 0:
            raise ValueError("La base debe ser un número positivo.")
        if not isinstance(altura, (int, float)) or altura <= 0:
            raise ValueError("La altura debe ser un número positivo.")
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


def imprimir_area(forma):
    print(f"El área de la forma es: {forma.area():.2f}")


circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)
triangulo = Triangulo(3, 8)

imprimir_area(circulo)
imprimir_area(rectangulo)
imprimir_area(triangulo)

formas = [Circulo(7), Rectangulo(10, 5), Triangulo(6, 4)]
print("\nCalculando áreas desde una lista de formas:")
for f in formas:
    imprimir_area(f)
