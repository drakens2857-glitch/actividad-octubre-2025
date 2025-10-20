import functools
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def manejar_errores(default_return=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.error(f"Error en la función '{func.__name__}': {e}", exc_info=True)
                return default_return
        return wrapper
    return decorator


@manejar_errores(default_return="Error al procesar los datos")
def procesar_datos(data):
    if not data:
        raise ValueError("Los datos no pueden estar vacíos")
    if len(data) > 5:
        raise IndexError("Demasiados datos para procesar")
    return f"Datos procesados: {data}"


@manejar_errores(default_return=0)
def dividir(a, b):
    return a / b


@manejar_errores()
def conectar_servicio(url):
    if "error" in url:
        raise ConnectionError(f"Fallo al conectar a {url}")
    return f"Conectado exitosamente a {url}"


print("--- Demostrando Decoradores de Manejo de Errores ---")
resultado1 = procesar_datos([])
print(f"Resultado 1: {resultado1}")
resultado2 = procesar_datos([1, 2, 3, 4, 5, 6])
print(f"Resultado 2: {resultado2}")
resultado3 = dividir(10, 0)
print(f"Resultado 3: {resultado3}")
resultado4 = procesar_datos([1, 2, 3])
print(f"Resultado 4: {resultado4}")
resultado5 = conectar_servicio("http://servicio_con_error.com")
print(f"Resultado 5: {resultado5}")
resultado6 = conectar_servicio("http://servicio_ok.com")
print(f"Resultado 6: {resultado6}")
