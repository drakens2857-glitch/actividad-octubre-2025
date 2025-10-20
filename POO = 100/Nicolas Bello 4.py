class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, incremento):
        if incremento > 0:
            self.velocidad += incremento
            return f"El {self.marca} {self.modelo} aceleró a {self.velocidad} km/h."
        else:
            return "El incremento de velocidad debe ser positivo."

    def frenar(self, decremento):
        if decremento > 0:
            self.velocidad = max(0, self.velocidad - decremento)
            return f"El {self.marca} {self.modelo} frenó a {self.velocidad} km/h."
        else:
            return "El decremento de velocidad debe ser positivo."

    def obtener_velocidad(self):
        return f"Velocidad actual: {self.velocidad} km/h."


coche = Vehiculo("Toyota", "Corolla")
print(coche.acelerar(50))
print(coche.acelerar(30))
print(coche.obtener_velocidad())
print(coche.frenar(40))
print(coche.frenar(100))
print(coche.obtener_velocidad())
