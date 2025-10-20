from abc import ABC, abstractmethod
import json
import os

class Archivo(ABC):
    def __init__(self, ruta):
        if not isinstance(ruta, str) or not ruta.strip():
            raise ValueError("La ruta del archivo no puede estar vacía.")
        self.ruta = ruta
        self.contenido = None

    @abstractmethod
    def leer(self):
        pass

    @abstractmethod
    def escribir(self, datos):
        pass

    def cerrar(self):
        print(f"Archivo '{self.ruta}' cerrado.")


class ArchivoTexto(Archivo):
    def __init__(self, ruta):
        super().__init__(ruta)

    def leer(self):
        try:
            with open(self.ruta, 'r', encoding='utf-8') as f:
                self.contenido = f.read()
                print(f"Contenido de '{self.ruta}' leído exitosamente (Texto).")
                return self.contenido
        except FileNotFoundError:
            print(f"Error: El archivo '{self.ruta}' no fue encontrado.")
            return None
        except Exception as e:
            print(f"Error al leer archivo de texto: {e}")
            return None

    def escribir(self, datos):
        if not isinstance(datos, str):
            raise TypeError("Los datos para ArchivoTexto deben ser una cadena de texto.")
        try:
            with open(self.ruta, 'w', encoding='utf-8') as f:
                f.write(datos)
                print(f"Datos escritos exitosamente en '{self.ruta}' (Texto).")
        except Exception as e:
            print(f"Error al escribir archivo de texto: {e}")


class ArchivoJSON(Archivo):
    def __init__(self, ruta):
        super().__init__(ruta)

    def leer(self):
        try:
            with open(self.ruta, 'r', encoding='utf-8') as f:
                self.contenido = json.load(f)
                print(f"Contenido de '{self.ruta}' leído exitosamente (JSON).")
                return self.contenido
        except FileNotFoundError:
            print(f"Error: El archivo '{self.ruta}' no fue encontrado.")
            return None
        except json.JSONDecodeError:
            print(f"Error: El archivo '{self.ruta}' no es un JSON válido.")
            return None
        except Exception as e:
            print(f"Error al leer archivo JSON: {e}")
            return None

    def escribir(self, datos):
        if not isinstance(datos, (dict, list)):
            raise TypeError("Los datos para ArchivoJSON deben ser un diccionario o una lista.")
        try:
            with open(self.ruta, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
                print(f"Datos escritos exitosamente en '{self.ruta}' (JSON).")
        except Exception as e:
            print(f"Error al escribir archivo JSON: {e}")


def procesar_archivo(archivo, operacion, datos=None):
    if operacion == "escribir":
        archivo.escribir(datos)
    elif operacion == "leer":
        contenido = archivo.leer()
        if contenido is not None:
            print(f"Contenido leído:\n{contenido}")
    archivo.cerrar()
