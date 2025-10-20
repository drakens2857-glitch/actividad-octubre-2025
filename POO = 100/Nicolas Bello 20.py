class Inventario:
    def __init__(self):
        self._items = {}

    def add_item(self, product_name, quantity):
        if not isinstance(product_name, str) or not product_name.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("La cantidad a añadir debe ser un número entero positivo.")
        product_name = product_name.strip().lower()
        self._items[product_name] = self._items.get(product_name, 0) + quantity
        return f"Añadidos {quantity} de '{product_name}'. Total: {self._items[product_name]}."

    def remove_item(self, product_name, quantity):
        if not isinstance(product_name, str) or not product_name.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("La cantidad a eliminar debe ser un número entero positivo.")
        product_name = product_name.strip().lower()
        if product_name not in self._items:
            raise ValueError(f"El producto '{product_name}' no existe en el inventario.")
        if self._items[product_name] < quantity:
            raise ValueError(f"Solo hay {self._items[product_name]} de '{product_name}'. No se pueden eliminar {quantity}.")
        self._items[product_name] -= quantity
        if self._items[product_name] == 0:
            del self._items[product_name]
            return f"Eliminados {quantity} de '{product_name}'. Producto agotado y removido."
        else:
            return f"Eliminados {quantity} de '{product_name}'. Restantes: {self._items[product_name]}."

    def get_quantity(self, product_name):
        if not isinstance(product_name, str) or not product_name.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        product_name = product_name.strip().lower()
        return self._items.get(product_name, 0)

    def list_items(self):
        if not self._items:
            return "El inventario está vacío."
        items_list = "\n".join([f"- {prod.capitalize()}: {qty}" for prod, qty in self._items.items()])
        return f"Inventario actual:\n{items_list}"

    def __str__(self):
        return self.list_items()


try:
    store_inventory = Inventario()
    print(store_inventory)
    print(store_inventory.add_item("Manzanas", 100))
    print(store_inventory.add_item("Leche", 50))
    print(store_inventory.add_item("manzanas", 20))
    print(store_inventory)
    print(f"Cantidad de Manzanas: {store_inventory.get_quantity('Manzanas')}")
    print(f"Cantidad de Pan: {store_inventory.get_quantity('Pan')}")
    print(store_inventory.remove_item("Leche", 20))
    print(store_inventory.remove_item("Manzanas", 120))
    print(store_inventory)
except ValueError as e:
    print(f"Error de inventario: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
