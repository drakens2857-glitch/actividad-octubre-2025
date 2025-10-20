class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("La cantidad a depositar debe ser positiva.")
        self.__balance += amount
        return f"Depósito exitoso. Nuevo saldo: {self.__balance:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if amount > self.__balance:
            raise ValueError("Fondos insuficientes.")
        self.__balance -= amount
        return f"Retiro exitoso. Nuevo saldo: {self.__balance:.2f}"

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Cuenta Bancaria con saldo: {self.__balance:.2f}"


try:
    my_account = BankAccount(100)
    print(my_account)
    print(my_account.deposit(50))
    print(my_account.withdraw(30))
    print(f"Saldo actual: {my_account.get_balance():.2f}")
    print(f"Acceso 'interno' al atributo: {my_account._BankAccount__balance:.2f}")

    another_account = BankAccount()
    print(another_account.deposit(500))

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
