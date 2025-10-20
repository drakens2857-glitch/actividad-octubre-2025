class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def acelerar(self):
        return f"{self.marca} {self.modelo} está acelerando hasta {self.velocidad_maxima} km/h."

    def __str__(self):
        return f"{self.marca} {self.modelo} - Velocidad Máxima: {self.velocidad_maxima} km/h"


class Auto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, puertas):
        super().__init__(marca, modelo, velocidad_maxima)
        self.puertas = puertas

    def abrir_maletero(self):
        return f"Maletero del {self.marca} {self.modelo} abierto."

    def __str__(self):
        return super().__str__() + f", Puertas: {self.puertas}"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, cilindrada):
        super().__init__(marca, modelo, velocidad_maxima)
        self.cilindrada = cilindrada

    def hacer_caballito(self):
        return f"{self.marca} {self.modelo} hace un caballito con {self.cilindrada}cc."

    def __str__(self):
        return super().__str__() + f", Cilindrada: {self.cilindrada}cc"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, tipo):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo = tipo

    def pedalear(self):
        return f"{self.marca} {self.modelo} ({self.tipo}) está pedaleando."

    def __str__(self):
        return super().__str__() + f", Tipo: {self.tipo}"
