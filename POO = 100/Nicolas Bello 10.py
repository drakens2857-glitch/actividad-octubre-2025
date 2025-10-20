class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.estado_animo = "Feliz"

    def alimentar(self):
        self.estado_animo = "Satisfecho"
        return f"{self.nombre} ha sido alimentado y ahora está {self.estado_animo}."

    def jugar(self):
        self.estado_animo = "Animado"
        return f"{self.nombre} ha jugado y ahora está {self.estado_animo}."

    def dormir(self):
        self.estado_animo = "Durmiendo"
        return f"{self.nombre} se ha dormido y ahora está {self.estado_animo}."

    def mostrar_estado(self):
        return f"{self.nombre}, tu {self.especie}, está {self.estado_animo}."


mascota1 = Mascota("Max", "Perro")
print(mascota1.mostrar_estado())
print(mascota1.alimentar())
print(mascota1.mostrar_estado())
print(mascota1.jugar())
print(mascota1.mostrar_estado())
print(mascota1.dormir())
print(mascota1.mostrar_estado())
print(mascota1.alimentar())

mascota2 = Mascota("Luna", "Gato")
print(mascota2.mostrar_estado())
print(mascota2.jugar())
print(mascota2.dormir())
print(mascota2.mostrar_estado())
