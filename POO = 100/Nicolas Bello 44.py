import time
import functools
import logging
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('DecoradorAvanzado')

def medir_tiempo(log_time=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            t_inicio = time.perf_counter()
            resultado = func(*args, **kwargs)
            t_fin = time.perf_counter()
            tiempo_ejecucion = t_fin - t_inicio
            if log_time:
                logger.info(f"'{func.__name__}' ejecutada en {tiempo_ejecucion:.4f} segundos.")
            else:
                print(f"'{func.__name__}' ejecutada en {tiempo_ejecucion:.4f} segundos (no loggeado).")
            return resultado
        return wrapper
    return decorator

def reintentar(max_intentos=3, retardo=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for intento in range(1, max_intentos + 1):
                try:
                    logger.info(f"Intento {intento}/{max_intentos} para '{func.__name__}'...")
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.warning(f"Fallo en el intento {intento} para '{func.__name__}': {e}")
                    if intento < max_intentos:
                        sleep_time = retardo + random.uniform(0, retardo / 2)
                        logger.info(f"Reintentando en {sleep_time:.2f} segundos...")
                        time.sleep(sleep_time)
                    else:
                        logger.error(f"Todos los {max_intentos} intentos fallaron para '{func.__name__}'.")
                        raise
        return wrapper
    return decorator

@medir_tiempo(log_time=False)
def tarea_lenta(segundos):
    print(f"Iniciando tarea lenta de {segundos} segundos...")
    time.sleep(segundos)
    print("Tarea lenta finalizada.")
    return f"Tarea lenta completada en {segundos}s"

@medir_tiempo(log_time=True)
def calcular_complejo(a, b):
    print(f"Calculando {a} * {b}...")
    time.sleep(0.1)
    return a * b

@reintentar(max_intentos=5, retardo=2)
def llamada_api_inestable(endpoint):
    if random.random() < 0.6:
        raise ConnectionError(f"Fallo de conexión al endpoint: {endpoint}")
    print(f"Llamada API a '{endpoint}' exitosa!")
    return {"data": "datos_del_api", "endpoint": endpoint}

print("\n--- Demostrando 'medir_tiempo' ---")
resultado_lenta = tarea_lenta(0.5)
print(resultado_lenta)

resultado_calculo = calcular_complejo(10, 20)
print(f"Resultado del cálculo: {resultado_calculo}")

print("\n--- Demostrando 'reintentar' ---")
try:
    api_response = llamada_api_inestable("/users/1")
    print(f"Respuesta de la API: {api_response}")
except Exception as e:
    print(f"Falló la operación API después de varios reintentos: {e}")

print("--- Fin de la demostración de Decoradores Avanzados ---")
