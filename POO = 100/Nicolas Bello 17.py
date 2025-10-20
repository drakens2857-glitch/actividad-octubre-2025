class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self._nombre = valor.strip()

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("La edad debe ser un número positivo.")
        self._edad = int(valor)

    @edad.deleter
    def edad(self):
        print("Eliminando la edad.")
        del self._edad

    def __str__(self):
        return f"Persona: {self.nombre}, Edad: {self.edad} años."


try:
    person1 = Persona("Ana López", 30)
    print(person1)
    print(f"Nombre: {person1.nombre}")
    person1.edad = 31
    print(f"Nueva edad: {person1.edad}")
    person1.nombre = "Pedro García "
    print(person1)
    del person1.edad
except ValueError as e:
    print(f"Error: {e}")
except AttributeError as e:
    print(f"Error de atributo: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
