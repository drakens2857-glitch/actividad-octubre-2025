class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            return f"Depósito exitoso. Nuevo saldo: ${self.__saldo}"
        return "Monto inválido para depósito."

    def retirar(self, monto):
        if monto <= 0:
            return "Monto inválido para retiro."
        if monto > self.__saldo:
            return "Fondos insuficientes."
        self.__saldo -= monto
        return f"Retiro exitoso. Nuevo saldo: ${self.__saldo}"

    def transferir(self, monto, otra_cuenta):
        if monto <= 0 or monto > self.__saldo:
            return "Transferencia inválida."
        self.__saldo -= monto
        otra_cuenta.__saldo += monto
        return f"Transferencia de ${monto} a {otra_cuenta.titular} realizada."

    def consultar_saldo(self):
        return f"Saldo actual: ${self.__saldo}"
