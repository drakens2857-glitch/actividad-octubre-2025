class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito de {cantidad} realizado. Nuevo saldo: {self.saldo}"
        else:
            return "La cantidad a depositar debe ser positiva."

    def retirar(self, cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                return f"Retiro de {cantidad} realizado. Nuevo saldo: {self.saldo}"
            else:
                return "Saldo insuficiente."
        else:
            return "La cantidad a retirar debe ser positiva."

    def consultar_saldo(self):
        return f"Saldo actual: {self.saldo}"


cuenta = CuentaBancaria(1000)
print(cuenta.consultar_saldo())
print(cuenta.depositar(500))
print(cuenta.retirar(200))
print(cuenta.retirar(1500))
print(cuenta.consultar_saldo())
print(cuenta.depositar(-100))
