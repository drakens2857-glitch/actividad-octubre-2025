class ErrorValidacion(Exception):
    pass


class EmailInvalidoError(ErrorValidacion):
    def __init__(self, email):
        self.email = email
        super().__init__(f"El email '{email}' no es válido.")


class ContrasenaDebilError(ErrorValidacion):
    def __init__(self, razon):
        self.razon = razon
        super().__init__(f"Contraseña débil: {razon}.")


class Usuario:
    def __init__(self, nombre_usuario, email, contrasena):
        self.nombre_usuario = nombre_usuario
        self._validar_email(email)
        self._validar_contrasena(contrasena)
        self.email = email
        self.contrasena_hash = self._hashear_contrasena(contrasena)

    def _validar_email(self, email):
        if "@" not in email or "." not in email:
            raise EmailInvalidoError(email)

    def _validar_contrasena(self, contrasena):
        if len(contrasena) < 8:
            raise ContrasenaDebilError("demasiado corta (mínimo 8 caracteres)")
        if not any(char.isdigit() for char in contrasena):
            raise ContrasenaDebilError("debe contener al menos un número")
        if not any(char.isupper() for char in contrasena):
            raise ContrasenaDebilError("debe contener al menos una letra mayúscula")

    def _hashear_contrasena(self, contrasena):
        return f"HASH_{contrasena}"

    def __str__(self):
        return f"Usuario: {self.nombre_usuario}, Email: {self.email}"


print("--- Demostrando Excepciones Personalizadas ---")
usuarios_a_crear = [
    ("alice", "alice@ejemplo.com", "ContrasenaSegura123"),
    ("bob", "bob_ejemplo.com", "pass1"),
    ("charlie", "charlie@dominio.com", "corta"),
    ("david", "david@web.org", "sinmayusculas123"),
    ("eve", "eve@otra.net", "SinNumeros"),
]

for nombre, email, contrasena in usuarios_a_crear:
    try:
        print(f"\nIntentando crear usuario: {nombre}")
        nuevo_usuario = Usuario(nombre, email, contrasena)
        print(f"Éxito: {nuevo_usuario}")
    except EmailInvalidoError as e:
        print(f"Error de validación de email para {nombre}: {e}")
    except ContrasenaDebilError as e:
        print(f"Error de validación de contraseña para {nombre}: {e}")
    except ErrorValidacion as e:
        print(f"Error general de validación para {nombre}: {e}")
    except Exception as e:
        print(f"Error inesperado al crear usuario {nombre}: {e}")
