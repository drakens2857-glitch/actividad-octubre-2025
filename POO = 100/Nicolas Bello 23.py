class Vehiculo:
    def acelerar(self):
        raise NotImplementedError("Las subclases deben implementar el método 'acelerar()'")


class Coche(Vehiculo):
    def acelerar(self):
        return "El coche ruge y acelera rápidamente."


class Bicicleta(Vehiculo):
    def acelerar(self):
        return "La bicicleta se mueve más rápido con el esfuerzo del ciclista."


class Avion(Vehiculo):
    def acelerar(self):
        return "El avión enciende sus turbinas y toma velocidad en la pista."


def probar_aceleracion(vehiculo):
    print(f"Resultado de acelerar: {vehiculo.acelerar()}")


coche = Coche()
bicicleta = Bicicleta()
avion = Avion()

probar_aceleracion(coche)
probar_aceleracion(bicicleta)
probar_aceleracion(avion)

parque_vehicular = [Coche(), Bicicleta(), Avion(), Coche()]
print("\nProbando la aceleración de todos los vehículos del parque:")
for v in parque_vehicular:
    probar_aceleracion(v)
