import sqlite3

conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER
)
''')
conn.commit()

cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Bob", 24))
conn.commit()

print("Usuarios en la base de datos:")
cursor.execute("SELECT * FROM usuarios")
for fila in cursor.fetchall():
    print(fila)

cursor.execute("UPDATE usuarios SET edad = ? WHERE nombre = ?", (31, "Alice"))
conn.commit()

cursor.execute("DELETE FROM usuarios WHERE nombre = ?", ("Bob",))
conn.commit()

print("\nUsuarios después de la actualización y eliminación:")
cursor.execute("SELECT * FROM usuarios")
for fila in cursor.fetchall():
    print(fila)

conn.close()
print("\nConexión a la base de datos cerrada.")
