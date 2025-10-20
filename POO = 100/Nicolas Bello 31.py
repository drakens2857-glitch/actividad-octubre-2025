import threading

class Configuracion:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Configuracion, cls).__new__(cls)
                    cls._instance.ajustes = {
                        "idioma": "es",
                        "tema": "oscuro",
                        "nivel_log": "INFO"
                    }
                    print("Instancia de Configuración creada.")
        return cls._instance

    def obtener_ajuste(self, clave):
        return self.ajustes.get(clave, "Ajuste no encontrado")

    def establecer_ajuste(self, clave, valor):
        self.ajustes[clave] = valor
        print(f"Ajuste '{clave}' establecido a '{valor}'.")


def usar_configuracion(nombre_hilo):
    config = Configuracion()
    print(f"[{nombre_hilo}] Idioma actual: {config.obtener_ajuste('idioma')}")
    if nombre_hilo == "Hilo Principal":
        config.establecer_ajuste("idioma", "en")
        config.establecer_ajuste("nivel_log", "DEBUG")
        print(f"[{nombre_hilo}] Configuración actual: {config.ajustes}")


print("--- Demostrando Patrón Singleton ---")
config1 = Configuracion()
config1.establecer_ajuste("tema", "claro")
config2 = Configuracion()
print(f"¿Son config1 y config2 la misma instancia? {config1 is config2}")
print(f"Idioma de config1: {config1.obtener_ajuste('idioma')}")
print(f"Tema de config2: {config2.obtener_ajuste('tema')}")

print("\n--- Demostrando Singleton en Multihilo ---")
hilo1 = threading.Thread(target=usar_configuracion, args=("Hilo 1",))
hilo2 = threading.Thread(target=usar_configuracion, args=("Hilo 2",))
hilo_principal = threading.Thread(target=usar_configuracion, args=("Hilo Principal",))
hilo1.start()
hilo2.start()
hilo_principal.start()
hilo1.join()
hilo2.join()
hilo_principal.join()

print("\nConfiguración final de la aplicación:")
final_config = Configuracion()
print(final_config.ajustes)
