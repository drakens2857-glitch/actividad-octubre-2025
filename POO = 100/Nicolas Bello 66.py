class Platillo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"


class Menu:
    def __init__(self):
        self.platillos = []

    def agregar_platillo(self, platillo):
        self.platillos.append(platillo)

    def mostrar_menu(self):
        return [str(p) for p in self.platillos]


class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, platillo):
        self.items.append(platillo)

    def calcular_total(self):
        return sum(p.precio for p in self.items)

    def resumen(self):
        nombres = [p.nombre for p in self.items]
        total = self.calcular_total()
        return f"Pedido: {', '.join(nombres)} - Total: ${total}"


class Mesero:
    def __init__(self, nombre):
        self.nombre = nombre

    def tomar_pedido(self, menu, seleccion_indices):
        pedido = Pedido()
        for i in seleccion_indices:
            if 0 <= i < len(menu.platillos):
                pedido.agregar_item(menu.platillos[i])
        return pedido
