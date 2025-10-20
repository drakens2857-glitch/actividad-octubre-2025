import math

class Figura:
    def __init__(self, nombre="Figura Genérica"):
        self.nombre = nombre

    def calcular_area(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases.")

    def calcular_perimetro(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases.")

    def mostrar_info(self):
        return f"Soy una {self.nombre}."


class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        if radio <= 0:
            raise ValueError("El radio debe ser positivo.")
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def mostrar_info(self):
        return f"{super().mostrar_info()} con radio {self.radio}."


class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        if lado <= 0:
            raise ValueError("El lado debe ser positivo.")
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

    def mostrar_info(self):
        return f"{super().mostrar_info()} con lado {self.lado}."


try:
    figura_generica = Figura()
    print(figura_generica.mostrar_info())

    circulo1 = Circulo(5)
    print(circulo1.mostrar_info())
    print(f"Área del {circulo1.nombre}: {circulo1.calcular_area():.2f}")
    print(f"Perímetro del {circulo1.nombre}: {circulo1.calcular_perimetro():.2f}")

    cuadrado1 = Cuadrado(4)
    print(cuadrado1.mostrar_info())
    print(f"Área del {cuadrado1.nombre}: {cuadrado1.calcular_area():.2f}")
    print(f"Perímetro del {cuadrado1.nombre}: {cuadrado1.calcular_perimetro():.2f}")

except ValueError as e:
    print(f"Error al crear figura: {e}")
except NotImplementedError as e:
    print(f"Error de implementación: {e}")
