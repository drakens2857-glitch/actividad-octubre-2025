from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del transporte no puede estar vacío.")
        self.nombre = nombre

    @abstractmethod
    def mover(self):
        pass

    def describir(self):
        return f"Este es un {self.nombre}."


class Coche(Transporte):
    def __init__(self, marca, modelo):
        super().__init__(f"Coche {marca} {modelo}")
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        return f"El {self.nombre} se mueve por carretera usando gasolina."


class Bicicleta(Transporte):
    def __init__(self, tipo):
        super().__init__(f"Bicicleta de {tipo}")
        self.tipo = tipo

    def mover(self):
        return f"La {self.nombre} se mueve pedaleando, propulsada por energía humana."


class Barco(Transporte):
    def __init__(self, nombre_barco):
        super().__init__(f"Barco {nombre_barco}")
        self.nombre_barco = nombre_barco

    def mover(self):
        return f"El {self.nombre} navega por el agua."


def hacer_mover(transporte):
    print(f"{transporte.describir()} y {transporte.mover()}")


mi_coche = Coche("Toyota", "Corolla")
mi_bicicleta = Bicicleta("montaña")
mi_barco = Barco("Perla Negra")

hacer_mover(mi_coche)
hacer_mover(mi_bicicleta)
hacer_mover(mi_barco)

flota = [
    Coche("Ford", "Fiesta"),
    Bicicleta("carretera"),
    Barco("Titanic")
]

print("\nLa flota comienza a moverse:")
for vehiculo in flota:
    hacer_mover(vehiculo)
