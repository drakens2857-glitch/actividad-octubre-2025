import time
import functools
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('retry_app')


def retry_with_exponential_backoff(max_retries, initial_delay=1, exponent=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            delay = initial_delay
            for i in range(1, max_retries + 1):
                try:
                    logger.info(f"Intento {i}/{max_retries} para '{func.__name__}'...")
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.warning(f"Fallo en intento {i} para '{func.__name__}': {e}")
                    if i < max_retries:
                        sleep_time = delay + random.uniform(0, 0.5 * delay)
                        logger.info(f"Reintentando en {sleep_time:.2f} segundos...")
                        time.sleep(sleep_time)
                        delay *= exponent
                    else:
                        logger.error(f"Todos los {max_retries} intentos fallaron para '{func.__name__}'.")
                        raise
        return wrapper
    return decorator


class ServicioSimulado:
    def __init__(self, fail_probability=0.7):
        self.fail_probability = fail_probability
        self.call_count = 0

    @retry_with_exponential_backoff(max_retries=5, initial_delay=0.5, exponent=2)
    def realizar_llamada_api(self, endpoint):
        self.call_count += 1
        if random.random() < self.fail_probability:
            if self.call_count < 4:
                raise ConnectionError(f"Fallo temporal de red al {endpoint}")
        logger.info(f"Llamada API a {endpoint} exitosa en el intento {self.call_count}!")
        self.call_count = 0
        return f"Datos de {endpoint}"


print("\n--- Demostrando Retry con Backoff Exponencial ---")

servicio = ServicioSimulado(fail_probability=0.7)
print("\n--- Escenario 1: Operación que eventualmente tiene éxito ---")
try:
    data = servicio.realizar_llamada_api("/users")
    print(f"Éxito: {data}")
except Exception as e:
    print(f"Fallo total: {e}")

servicio_persistente = ServicioSimulado(fail_probability=0.95)
print("\n--- Escenario 2: Operación que falla persistentemente ---")
try:
    data = servicio_persistente.realizar_llamada_api("/products")
    print(f"Éxito: {data}")
except Exception as e:
    print(f"Fallo total: {e}")

print("\n--- Fin de la demostración de reintentos ---")
