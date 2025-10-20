from abc import ABC, abstractmethod

class Cafe(ABC):
    @abstractmethod
    def obtener_costo(self):
        pass

    @abstractmethod
    def obtener_descripcion(self):
        pass


class CafeSimple(Cafe):
    def obtener_costo(self):
        return 2.0

    def obtener_descripcion(self):
        return "Café simple"


class DecoradorCafe(Cafe, ABC):
    def __init__(self, cafe: Cafe):
        self._cafe = cafe

    @abstractmethod
    def obtener_costo(self):
        pass

    @abstractmethod
    def obtener_descripcion(self):
        pass


class Leche(DecoradorCafe):
    def __init__(self, cafe: Cafe):
        super().__init__(cafe)

    def obtener_costo(self):
        return self._cafe.obtener_costo() + 0.5

    def obtener_descripcion(self):
        return self._cafe.obtener_descripcion() + ", con leche"


class Azucar(DecoradorCafe):
    def __init__(self, cafe: Cafe):
        super().__init__(cafe)

    def obtener_costo(self):
        return self._cafe.obtener_costo() + 0.2

    def obtener_descripcion(self):
        return self._cafe.obtener_descripcion() + ", con azúcar"


class Caramelo(DecoradorCafe):
    def __init__(self, cafe: Cafe):
        super().__init__(cafe)

    def obtener_costo(self):
        return self._cafe.obtener_costo() + 1.0

    def obtener_descripcion(self):
        return self._cafe.obtener_descripcion() + ", con caramelo"


print("--- Demostrando Patrón Decorator ---")
cafe1 = CafeSimple()
print(f"Pedido 1: {cafe1.obtener_descripcion()} - Costo: {cafe1.obtener_costo():.2f}€")

cafe2 = Leche(CafeSimple())
print(f"Pedido 2: {cafe2.obtener_descripcion()} - Costo: {cafe2.obtener_costo():.2f}€")

cafe3 = Azucar(Leche(CafeSimple()))
print(f"Pedido 3: {cafe3.obtener_descripcion()} - Costo: {cafe3.obtener_costo():.2f}€")

cafe4 = Caramelo(Azucar(Leche(CafeSimple())))
print(f"Pedido 4: {cafe4.obtener_descripcion()} - Costo: {cafe4.obtener_costo():.2f}€")

cafe5 = Caramelo(CafeSimple())
print(f"Pedido 5: {cafe5.obtener_descripcion()} - Costo: {cafe5.obtener_costo():.2f}€")
print("--- Fin de la demostración ---")