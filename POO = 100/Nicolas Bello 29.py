from abc import ABC, abstractmethod

class Juego(ABC):
    def __init__(self, titulo):
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("El título del juego no puede estar vacío.")
        self.titulo = titulo
        self.esta_jugando = False

    @abstractmethod
    def iniciar_juego(self):
        pass

    @abstractmethod
    def jugar_turno(self):
        pass

    @abstractmethod
    def finalizar_juego(self):
        pass

    def obtener_estado(self):
        return f"El juego '{self.titulo}' está {'en curso' if self.esta_jugando else 'inactivo'}."


class JuegoMesa(Juego):
    def __init__(self, titulo, num_jugadores):
        super().__init__(titulo)
        if not isinstance(num_jugadores, int) or num_jugadores < 1:
            raise ValueError("El número de jugadores debe ser un entero positivo.")
        self.num_jugadores = num_jugadores
        self.turno_actual = 0

    def iniciar_juego(self):
        print(f"Iniciando el juego de mesa '{self.titulo}' para {self.num_jugadores} jugadores.")
        self.esta_jugando = True
        self.turno_actual = 1

    def jugar_turno(self):
        if self.esta_jugando:
            print(f"'{self.titulo}' - Turno {self.turno_actual}: El jugador {self.turno_actual % self.num_jugadores + 1} mueve sus piezas.")
            self.turno_actual += 1
            if self.turno_actual > 3:
                self.finalizar_juego()
        else:
            print(f"El juego '{self.titulo}' no ha sido iniciado.")

    def finalizar_juego(self):
        print(f"El juego de mesa '{self.titulo}' ha terminado. ¡Gracias por jugar!")
        self.esta_jugando = False
        self.turno_actual = 0


class Videojuego(Juego):
    def __init__(self, titulo, plataforma):
        super().__init__(titulo)
        if not isinstance(plataforma, str) or not plataforma.strip():
            raise ValueError("La plataforma del videojuego no puede estar vacía.")
        self.plataforma = plataforma
        self.nivel_actual = 0

    def iniciar_juego(self):
        print(f"Cargando videojuego '{self.titulo}' en {self.plataforma}. ¡Prepárate para la acción!")
        self.esta_jugando = True
        self.nivel_actual = 1

    def jugar_turno(self):
        if self.esta_jugando:
            print(f"'{self.titulo}' - Jugando nivel {self.nivel_actual}. Derrotando enemigos...")
            self.nivel_actual += 1
            if self.nivel_actual > 5:
                self.finalizar_juego()
        else:
            print(f"El videojuego '{self.titulo}' no ha sido iniciado.")

    def finalizar_juego(self):
        print(f"El videojuego '{self.titulo}' ha sido completado. ¡Victoria!")
        self.esta_jugando = False
        self.nivel_actual = 0


def gestionar_juego(juego):
    print(f"\n--- Gestionando {juego.titulo} ---")
    print(juego.obtener_estado())
    juego.iniciar_juego()
    print(juego.obtener_estado())
    for _ in range(4):
        juego.jugar_turno()
    print(juego.obtener_estado())


ajedrez = JuegoMesa("Ajedrez", 2)
zelda = Videojuego("The Legend of Zelda", "Nintendo Switch")

gestionar_juego(ajedrez)
gestionar_juego(zelda)
