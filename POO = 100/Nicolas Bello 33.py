from abc import ABC, abstractmethod

class Sujeto(ABC):
    def __init__(self):
        self._observadores = []

    def adjuntar(self, observador):
        self._observadores.append(observador)

    def desadjuntar(self, observador):
        self._observadores.remove(observador)

    def notificar(self, mensaje):
        for observador in self._observadores:
            observador.actualizar(mensaje)


class Observador(ABC):
    @abstractmethod
    def actualizar(self, mensaje):
        pass


class Tienda(Sujeto):
    def __init__(self, nombre):
        super().__init__()
        self._nombre = nombre
        self._ultimas_noticias = ""

    def nueva_noticia(self, noticia):
        self._ultimas_noticias = f"[{self._nombre}] Nueva noticia: {noticia}"
        print(f"\n--- {self._ultimas_noticias} ---")
        self.notificar(self._ultimas_noticias)


class UsuarioEmail(Observador):
    def __init__(self, nombre, email):
        self._nombre = nombre
        self._email = email

    def actualizar(self, mensaje):
        print(f"Email a {self._nombre} ({self._email}): {mensaje}")


class UsuarioSMS(Observador):
    def __init__(self, nombre, telefono):
        self._nombre = nombre
        self._telefono = telefono

    def actualizar(self, mensaje):
        print(f"SMS a {self._nombre} ({self._telefono}): {mensaje}")


class PanelAdmin(Observador):
    def __init__(self):
        self._logs = []

    def actualizar(self, mensaje):
        self._logs.append(f"LOG: {mensaje}")
        print(f"Panel Admin ha registrado: {mensaje}")

    def mostrar_logs(self):
        print("\n--- Logs del Panel Admin ---")
        for log in self._logs:
            print(log)


print("--- Demostrando Patrón Observer ---")
mi_tienda = Tienda("SuperOfertas Online")
usuario1 = UsuarioEmail("Ana", "ana@ejemplo.com")
usuario2 = UsuarioSMS("Pedro", "654321098")
panel_admin = PanelAdmin()
usuario3 = UsuarioEmail("Marta", "marta@ejemplo.com")

mi_tienda.adjuntar(usuario1)
mi_tienda.adjuntar(usuario2)
mi_tienda.adjuntar(panel_admin)

mi_tienda.nueva_noticia("¡Grandes descuentos en electrónica este fin de semana!")
mi_tienda.adjuntar(usuario3)
mi_tienda.nueva_noticia("¡Nuevos productos de moda disponibles!")
mi_tienda.desadjuntar(usuario2)
print("\nPedro (SMS) ha sido desaduntado.")
mi_tienda.nueva_noticia("¡Liquidación total por cambio de temporada!")
panel_admin.mostrar_logs()
