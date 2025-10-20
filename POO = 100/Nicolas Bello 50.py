import redis
import time

try:
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.ping()
    print("Conectado a Redis.")
except redis.exceptions.ConnectionError as e:
    print(f"No se pudo conectar a Redis: {e}")
    print("Por favor, asegúrate de que el servidor Redis esté en ejecución.")
    exit()

print("\n--- Caché con Redis ---")

cache_key = "datos_producto_123"
data_to_cache = "{'nombre': 'Teclado Mecánico', 'precio': 85}"
expiration_time_seconds = 10

r.setex(cache_key, expiration_time_seconds, data_to_cache)
print(f"Datos '{data_to_cache}' almacenados en caché bajo '{cache_key}' con {expiration_time_seconds}s de expiración.")

cached_data = r.get(cache_key)
if cached_data:
    print(f"Datos recuperados de caché: {cached_data.decode('utf-8')}")
else:
    print("Datos no encontrados en caché (o ya expirados).")

print(f"Esperando {expiration_time_seconds} segundos para la expiración...")
time.sleep(expiration_time_seconds + 1)

cached_data_after_expiration = r.get(cache_key)
if cached_data_after_expiration:
    print(f"Datos recuperados de caché después de expiración: {cached_data_after_expiration.decode('utf-8')}")
else:
    print("Datos no encontrados en caché después de expiración (como se esperaba).")

print("\n--- Sesiones con Redis ---")

session_id = "user_session_abcde"
user_data = {'username': 'coder_master', 'last_login': '2023-10-26 10:00:00'}

r.hmset(session_id, user_data)
r.expire(session_id, 300)
print(f"Datos de sesión para '{session_id}' almacenados: {user_data}")

retrieved_session_data = r.hgetall(session_id)
if retrieved_session_data:
    decoded_session_data = {k.decode('utf-8'): v.decode('utf-8') for k, v in retrieved_session_data.items()}
    print(f"Datos de sesión recuperados: {decoded_session_data}")

r.hset(session_id, 'last_login', '2023-10-26 10:30:00')
retrieved_session_data_updated = r.hgetall(session_id)
decoded_session_data_updated = {k.decode('utf-8'): v.decode('utf-8') for k, v in retrieved_session_data_updated.items()}
print(f"Datos de sesión actualizados: {decoded_session_data_updated}")

r.delete(session_id)
print(f"Sesión '{session_id}' eliminada.")

retrieved_session_data_deleted = r.hgetall(session_id)
if not retrieved_session_data_deleted:
    print(f"Verificado: la sesión '{session_id}' ya no existe.")
