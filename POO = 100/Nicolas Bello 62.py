class Calculadora:
    def __init__(self):
        self.resultado = 0
        self.historial = []

    def sumar(self, a, b):
        self.resultado = a + b
        self._registrar_operacion(f"{a} + {b} = {self.resultado}")
        return self.resultado

    def restar(self, a, b):
        self.resultado = a - b
        self._registrar_operacion(f"{a} - {b} = {self.resultado}")
        return self.resultado

    def multiplicar(self, a, b):
        self.resultado = a * b
        self._registrar_operacion(f"{a} × {b} = {self.resultado}")
        return self.resultado

    def dividir(self, a, b):
        if b == 0:
            operacion = f"{a} ÷ {b} = Error (división por cero)"
            self._registrar_operacion(operacion)
            return "Error: división por cero"
        self.resultado = a / b
        self._registrar_operacion(f"{a} ÷ {b} = {self.resultado}")
        return self.resultado

    def _registrar_operacion(self, descripcion):
        self.historial.append(descripcion)

    def ver_historial(self):
        return self.historial
