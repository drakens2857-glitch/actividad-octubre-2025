import logging
import sys

logger = logging.getLogger('mi_aplicacion')
logger.setLevel(logging.DEBUG)

formatter_full = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter_simple = logging.Formatter('%(levelname)s: %(message)s')

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
ch.setFormatter(formatter_simple)

fh = logging.FileHandler('aplicacion.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter_full)

logger.addHandler(ch)
logger.addHandler(fh)


print("--- Demostrando Sistema de Logging Avanzado ---")

def realizar_operacion(valor):
    logger.debug(f"DEBUG: Intentando realizar operación con valor: {valor}")
    try:
        resultado = 100 / valor
        logger.info(f"INFO: Operación exitosa. Resultado: {resultado}")
        if resultado > 50:
            logger.warning(f"WARNING: El resultado {resultado} es inusualmente alto.")
    except ZeroDivisionError:
        logger.error("ERROR: Intento de división por cero.")
        raise
    except Exception as e:
        logger.critical(f"CRITICAL: Ha ocurrido un error inesperado: {e}", exc_info=True)
    return True


print("\n--- Ejecutando operaciones ---")
try:
    realizar_operacion(20)
    realizar_operacion(1)
    realizar_operacion(0)
except ZeroDivisionError:
    print("Capturada división por cero en el programa principal.")

realizar_operacion(50)

try:
    realizar_operacion("texto")
except Exception:
    print("Capturada excepción inesperada en el programa principal.")
    logger.info("INFO: Fin de la demostración de logging.")
