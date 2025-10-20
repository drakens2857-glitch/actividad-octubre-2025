class Calculadora:
    def __init__(self):
        pass

    def sumar(self, num1, num2):

        return num1 + num2

    def restar(self, num1, num2):

        return num1 - num2

    def multiplicar(self, num1, num2):

        return num1 * num2

    def dividir(self, num1, num2):

        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero no permitida."


calc = Calculadora()
print(f"6 + 2 = {calc.sumar(6, 2)}")
print(f"50 - 8 = {calc.restar(50, 8)}")
print(f"56 * 7 = {calc.multiplicar(56, 7)}")
print(f"84 / 29 = {calc.dividir(84, 29)}")
print(f"45 / 0 = {calc.dividir(45, 0)}")
