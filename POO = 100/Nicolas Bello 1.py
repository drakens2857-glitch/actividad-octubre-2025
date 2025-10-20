class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  
        self.edad = edad      

    def saludar(self):
        # Método para saludar
        return f"Hola, mi nombre es {self.nombre}."

    def cumplir_anios(self):
        # Incrementa la edad
        self.edad += 1
        return f"¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años."


persona1 = Persona("Nicolas", 18)
print(persona1.saludar())
print(persona1.cumplir_anios())
print(persona1.saludar())

persona2 = Persona("Santiago", 18)
print(persona2.saludar())
