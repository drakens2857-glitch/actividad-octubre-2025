class Temperatura:
    MIN_CELSIUS = -273.15

    def __init__(self, celsius=0):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("La temperatura debe ser un número.")
        if valor < self.MIN_CELSIUS:
            raise ValueError(f"La temperatura no puede ser inferior al cero absoluto ({self.MIN_CELSIUS}°C).")
        self._celsius = float(valor)

    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("La temperatura debe ser un número.")
        self.celsius = (valor - 32) * 5/9

    def __str__(self):
        return f"Temperatura: {self.celsius:.2f}°C / {self.fahrenheit:.2f}°F"


try:
    temp1 = Temperatura(25)
    print(temp1)
    print(f"Temperatura en Celsius: {temp1.celsius:.2f}°C")
    temp1.celsius = 10
    print(temp1)
    print(f"Temperatura en Fahrenheit: {temp1.fahrenheit:.2f}°F")
    temp1.fahrenheit = 212
    print(temp1)
except ValueError as e:
    print(f"Error de validación: {e}")
except TypeError as e:
    print(f"Error de tipo: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
