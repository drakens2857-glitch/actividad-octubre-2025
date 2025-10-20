import json
import pickle

print("--- Serialización con JSON ---")

datos_json = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudades': ['Madrid', 'Barcelona'],
    'activo': True
}

cadena_json = json.dumps(datos_json, indent=4)
print("Objeto serializado a cadena JSON:\n", cadena_json)

with open('datos.json', 'w') as f:
    json.dump(datos_json, f, indent=4)
print("\nObjeto guardado en 'datos.json'.")

objeto_deserializado_json = json.loads(cadena_json)
print("Cadena JSON deserializada a objeto Python:", objeto_deserializado_json)

with open('datos.json', 'r') as f:
    objeto_desde_archivo_json = json.load(f)
print("Objeto cargado desde 'datos.json':", objeto_desde_archivo_json)

print("\n--- Serialización con Pickle ---")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"

personas_pickle = [Persona('Ana', 25), Persona('Carlos', 40)]

bytes_pickle = pickle.dumps(personas_pickle)
print("Objeto serializado a bytes con Pickle:", bytes_pickle)

with open('datos.pkl', 'wb') as f:
    pickle.dump(personas_pickle, f)
print("\nObjeto guardado en 'datos.pkl'.")

objeto_deserializado_pickle = pickle.loads(bytes_pickle)
print("Bytes Pickle deserializados a objeto Python:", objeto_deserializado_pickle)

with open('datos.pkl', 'rb') as f:
    objeto_desde_archivo_pickle = pickle.load(f)
print("Objeto cargado desde 'datos.pkl':", objeto_desde_archivo_pickle)
