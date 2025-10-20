import time
import sqlite3

class Temporizador:
    def __enter__(self):
        self.inicio = time.time()
        print("Temporizador iniciado...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        fin = time.time()
        duracion = fin - self.inicio
        print(f"Temporizador finalizado. Duración: {duracion:.4f} segundos.")
        return False


class ConexionBD:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        print(f"Abriendo conexión a la base de datos: {self.db_name}")
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Se detectó un error en la BD: {exc_val}. Haciendo rollback.")
            self.conn.rollback()
        else:
            print("No hubo errores en la BD. Haciendo commit.")
            self.conn.commit()
        self.conn.close()
        print(f"Conexión a la base de datos {self.db_name} cerrada.")
        return False


print("--- Demostrando Context Managers ---")
with Temporizador():
    print("Realizando una operación que consume tiempo...")
    time.sleep(1.5)
    print("Operación terminada.")

DB_FILE = "mi_base_de_datos.db"

print("\n--- Escenario 1: Operación exitosa en la BD ---")
try:
    with ConexionBD(DB_FILE) as db:
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS productos")
        cursor.execute("CREATE TABLE productos (id INTEGER PRIMARY KEY, nombre TEXT, precio REAL)")
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES ('Laptop', 1200.00)")
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES ('Ratón', 25.50)")

    with ConexionBD(DB_FILE) as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos")
        print("Productos guardados:")
        for row in cursor.fetchall():
            print(row)
except Exception as e:
    print(f"Error inesperado en escenario 1: {e}")

print("\n--- Escenario 2: Operación fallida en la BD ---")
try:
    with ConexionBD(DB_FILE) as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES ('Teclado', 75.00)")
        print("Intentando generar un error...")
        raise ValueError("Simulando un error durante la transacción")
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES ('Webcam', 50.00)")
except ValueError as e:
    print(f"Capturado el error simulado: {e}")

print("\nVerificando si 'Teclado' fue insertado (debería ser no):")
with ConexionBD(DB_FILE) as db:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM productos WHERE nombre = 'Teclado'")
    if cursor.fetchone():
        print("Error: 'Teclado' fue insertado, el rollback falló.")
    else:
        print("Correcto: 'Teclado' NO fue insertado. El rollback funcionó.")
