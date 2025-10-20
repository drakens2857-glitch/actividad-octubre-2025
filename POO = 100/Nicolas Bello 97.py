class PrestamoInterbibliotecario:
    def __init__(self, libro, origen, destino, fecha_envio):
        self.libro = libro
        self.origen = origen
        self.destino = destino
        self.fecha_envio = fecha_envio
        self.recibido = False

    def marcar_recibido(self):
        self.recibido = True
