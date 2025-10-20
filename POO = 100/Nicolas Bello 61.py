class Mascota:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.hambre = 50
        self.energia = 100
        self.felicidad = 75

    def comer(self, cantidad=10):
        self.hambre = max(0, self.hambre - cantidad)
        self.energia = min(100, self.energia + cantidad // 2)
        self.felicidad = min(100, self.felicidad + 5)
        return f"¡{self.nombre} comió! Hambre: {self.hambre}, Energía: {self.energia}"

    def dormir(self, horas=8):
        recuperacion = horas * 10
        self.energia = min(100, self.energia + recuperacion)
        self.hambre = min(100, self.hambre + horas * 2)
        return f"{self.nombre} durmió {horas} horas. Energía: {self.energia}, Hambre: {self.hambre}"

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - Edad: {self.edad}, Hambre: {self.hambre}, Energía: {self.energia}, Felicidad: {self.felicidad}"
