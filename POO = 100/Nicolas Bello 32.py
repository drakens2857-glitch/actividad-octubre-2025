from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def arrancar(self):
        pass


class Coche(Vehiculo):
    def tipo(self):
        return "Coche"

    def arrancar(self):
        return "El coche ruge y arranca."


class Moto(Vehiculo):
    def tipo(self):
        return "Moto"

    def arrancar(self):
        return "La moto se enciende con un bramido."


class Bicicleta(Vehiculo):
    def tipo(self):
        return "Bicicleta"

    def arrancar(self):
        return "La bicicleta empieza a rodar con el pedaleo."


class FabricaVehiculos(ABC):
    @abstractmethod
    def crear_vehiculo(self):
        pass

    def operar_vehiculo(self):
        vehiculo = self.crear_vehiculo()
        resultado = f"Creando {vehiculo.tipo()} y luego... {vehiculo.arrancar()}"
        return resultado


class FabricaCoches(FabricaVehiculos):
    def crear_vehiculo(self):
        return Coche()


class FabricaMotos(FabricaVehiculos):
    def crear_vehiculo(self):
        return Moto()


class FabricaBicicletas(FabricaVehiculos):
    def crear_vehiculo(self):
        return Bicicleta()


def cliente(fabrica: FabricaVehiculos):
    print(f"Cliente: He pedido un vehículo y: {fabrica.operar_vehiculo()}")


print("--- Demostrando Patrón Factory Method ---")
print("\nSolicitando un coche:")
cliente(FabricaCoches())
print("\nSolicitando una moto:")
cliente(FabricaMotos())
print("\nSolicitando una bicicleta:")
cliente(FabricaBicicletas())
