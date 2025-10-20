class Rectangulo:
    def __init__(self, largo, ancho):
        if largo > 0 and ancho > 0:
            self.largo = largo
            self.ancho = ancho
        else:
            raise ValueError("El largo y el ancho deben ser valores positivos.")

    def calcular_area(self):
        return self.largo * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.largo + self.ancho)

    def mostrar_dimensiones(self):
        return f"Rectángulo con Largo: {self.largo} unidades, Ancho: {self.ancho} unidades."


try:
    rectangulo1 = Rectangulo(10, 5)
    print(rectangulo1.mostrar_dimensiones())
    print(f"Área: {rectangulo1.calcular_area()} unidades cuadradas.")
    print(f"Perímetro: {rectangulo1.calcular_perimetro()} unidades.")

    rectangulo2 = Rectangulo(7.5, 3)
    print(rectangulo2.mostrar_dimensiones())
    print(f"Área: {rectangulo2.calcular_area()} unidades cuadradas.")
    print(f"Perímetro: {rectangulo2.calcular_perimetro()} unidades.")

    rectangulo_invalido = Rectangulo(-5, 2)
except ValueError as e:
    print(f"Error al crear rectángulo: {e}")
