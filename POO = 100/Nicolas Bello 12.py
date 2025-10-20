class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento
        return f"{self.marca} {self.modelo} acelera a {self.velocidad} km/h."

    def frenar(self, decremento):
        self.velocidad = max(0, self.velocidad - decremento)
        return f"{self.marca} {self.modelo} frena a {self.velocidad} km/h."

    def mostrar_info(self):
        return f"Vehículo: {self.marca} {self.modelo}, Velocidad actual: {self.velocidad} km/h."


class Auto(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas

    def abrir_puertas(self):
        return f"El {self.marca} {self.modelo} abre sus {self.num_puertas} puertas."

    def acelerar(self, incremento):
        self.velocidad += incremento * 1.2
        return f"El Auto {self.marca} {self.modelo} rugió y aceleró a {self.velocidad} km/h."


class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo_manillar):
        super().__init__(marca, modelo)
        self.tipo_manillar = tipo_manillar

    def hacer_caballito(self):
        return f"La Moto {self.marca} {self.modelo} está haciendo un caballito!"

    def acelerar(self, incremento):
        self.velocidad += incremento * 1.5
        return f"La Moto {self.marca} {self.modelo} se lanzó a {self.velocidad} km/h."


vehiculo_generico = Vehiculo("Generica", "ModeloX")
print(vehiculo_generico.mostrar_info())
print(vehiculo_generico.acelerar(20))
print(vehiculo_generico.frenar(10))

auto1 = Auto("Toyota", "Corolla", 4)
print(auto1.mostrar_info())
print(auto1.abrir_puertas())
print(auto1.acelerar(30))
print(auto1.frenar(15))

moto1 = Moto("Honda", "CBR500R", "Deportivo")
print(moto1.mostrar_info())
print(moto1.hacer_caballito())
print(moto1.acelerar(40))
print(moto1.frenar(20))
