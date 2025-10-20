from abc import ABC, abstractmethod

class EstrategiaPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass


class PagoTarjetaCredito(EstrategiaPago):
    def __init__(self, numero_tarjeta, fecha_exp, cvv):
        self.numero_tarjeta = numero_tarjeta
        self.fecha_exp = fecha_exp
        self.cvv = cvv

    def pagar(self, monto):
        print(f"Pagando {monto:.2f}€ con Tarjeta de Crédito (**** {self.numero_tarjeta[-4:]}).")
        return True


class PagoPayPal(EstrategiaPago):
    def __init__(self, email):
        self.email = email

    def pagar(self, monto):
        print(f"Pagando {monto:.2f}€ con PayPal (cuenta: {self.email}).")
        return True


class PagoTransferenciaBancaria(EstrategiaPago):
    def __init__(self, banco, cuenta):
        self.banco = banco
        self.cuenta = cuenta

    def pagar(self, monto):
        print(f"Pagando {monto:.2f}€ con Transferencia Bancaria (Banco: {self.banco}, Cuenta: {self.cuenta}).")
        return True


class CarritoCompras:
    def __init__(self):
        self.productos = []
        self._estrategia_pago = None

    def agregar_producto(self, nombre, precio):
        self.productos.append({"nombre": nombre, "precio": precio})
        print(f"'{nombre}' agregado al carrito.")

    def establecer_estrategia_pago(self, estrategia: EstrategiaPago):
        self._estrategia_pago = estrategia
        print(f"Estrategia de pago establecida: {type(estrategia).__name__}.")

    def checkout(self):
        if not self.productos:
            print("El carrito está vacío.")
            return False
        if not self._estrategia_pago:
            print("No se ha seleccionado una estrategia de pago.")
            return False

        monto_total = sum(item["precio"] for item in self.productos)
        print(f"\nProcesando pago de {monto_total:.2f}€...")
        if self._estrategia_pago.pagar(monto_total):
            print("Pago completado exitosamente.")
            self.productos = []
            return True
        else:
            print("El pago ha fallado.")
            return False


print("--- Demostrando Patrón Strategy ---")
mi_carrito = CarritoCompras()
mi_carrito.agregar_producto("Laptop", 1200.00)
mi_carrito.agregar_producto("Ratón Gaming", 50.00)

print("\nIntentando pagar con Tarjeta de Crédito:")
tarjeta = PagoTarjetaCredito("1234-5678-9012-3456", "12/25", "123")
mi_carrito.establecer_estrategia_pago(tarjeta)
mi_carrito.checkout()

mi_carrito.agregar_producto("Teclado Mecánico", 150.00)

print("\nIntentando pagar con PayPal:")
paypal = PagoPayPal("usuario@ejemplo.com")
mi_carrito.establecer_estrategia_pago(paypal)
mi_carrito.checkout()

mi_carrito.agregar_producto("Monitor 4K", 400.00)
mi_carrito.establecer_estrategia_pago(PagoTransferenciaBancaria("BBVA", "ES12345678901234567890"))
mi_carrito.checkout()
print("\nIntentando pagar con Transferencia Bancaria:")