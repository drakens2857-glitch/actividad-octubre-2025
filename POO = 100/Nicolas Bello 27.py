from abc import ABC, abstractmethod

class ProcesadorPagos(ABC):
    def __init__(self, nombre_procesador):
        if not isinstance(nombre_procesador, str) or not nombre_procesador.strip():
            raise ValueError("El nombre del procesador de pagos no puede estar vacío.")
        self.nombre = nombre_procesador

    @abstractmethod
    def procesar_pago(self, monto, divisa):
        pass

    @abstractmethod
    def reembolsar(self, monto, id_transaccion):
        pass

    def obtener_info(self):
        return f"Procesador: {self.nombre}"


class ProcesadorTarjetaCredito(ProcesadorPagos):
    def __init__(self, nombre_banco):
        super().__init__(f"Tarjeta de Crédito ({nombre_banco})")
        self.banco = nombre_banco

    def procesar_pago(self, monto, divisa):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo.")
        print(f"[{self.nombre}] Procesando {monto:.2f} {divisa} con tarjeta de {self.banco}.")
        return f"TRX_CC_{hash(self)}"

    def reembolsar(self, monto, id_transaccion):
        if monto <= 0:
            raise ValueError("El monto de reembolso debe ser positivo.")
        print(f"[{self.nombre}] Reembolsando {monto:.2f} para transacción {id_transaccion} en tarjeta de {self.banco}.")
        return True


class ProcesadorPayPal(ProcesadorPagos):
    def __init__(self, cuenta_vendedor):
        super().__init__("PayPal")
        self.cuenta = cuenta_vendedor

    def procesar_pago(self, monto, divisa):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo.")
        print(f"[{self.nombre}] Procesando {monto:.2f} {divisa} a la cuenta {self.cuenta} vía PayPal.")
        return f"TRX_PP_{hash(self)}"

    def reembolsar(self, monto, id_transaccion):
        if monto <= 0:
            raise ValueError("El monto de reembolso debe ser positivo.")
        print(f"[{self.nombre}] Reembolsando {monto:.2f} para transacción {id_transaccion} vía PayPal.")
        return True


def gestionar_pago(procesador, monto, divisa):
    print(f"\nUsando {procesador.obtener_info()}")
    try:
        id_transaccion = procesador.procesar_pago(monto, divisa)
        print(f"Pago exitoso. ID de transacción: {id_transaccion}")
        return id_transaccion
    except ValueError as e:
        print(f"Error al procesar pago: {e}")
        return None


def gestionar_reembolso(procesador, monto, id_transaccion):
    print(f"\nUsando {procesador.obtener_info()}")
    try:
        if procesador.reembolsar(monto, id_transaccion):
            print(f"Reembolso exitoso para la transacción: {id_transaccion}")
        else:
            print(f"Reembolso fallido para la transacción: {id_transaccion}")
    except ValueError as e:
        print(f"Error al reembolsar: {e}")


visa_processor = ProcesadorTarjetaCredito("Banco Universal")
paypal_processor = ProcesadorPayPal("ventas@ejemplo.com")

id1 = gestionar_pago(visa_processor, 150.75, "USD")
if id1:
    gestionar_reembolso(visa_processor, 50.00, id1)

id2 = gestionar_pago(paypal_processor, 299.99, "EUR")
if id2:
    gestionar_reembolso(paypal_processor, 299.99, id2)

gestionar_pago(visa_processor, -10, "USD")
