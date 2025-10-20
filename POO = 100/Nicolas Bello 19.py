import hashlib

class Password:
    def __init__(self, password):
        self.set_password(password)

    def _hash_password(self, password_text):
        if not isinstance(password_text, str) or not password_text:
            raise ValueError("La contraseña debe ser una cadena no vacía.")
        return hashlib.sha256(password_text.encode('utf-8')).hexdigest()

    def set_password(self, new_password):
        self.__hashed_password = self._hash_password(new_password)
        print("Contraseña establecida correctamente.")

    def check_password(self, provided_password):
        return self._hash_password(provided_password) == self.__hashed_password

    @property
    def current_hash(self):
        return self.__hashed_password

    def __str__(self):
        return f"Objeto Password (hash: {self.__hashed_password[:10]}...)"


try:
    user_pass = Password("MiContraseñaSecreta123!")
    print(user_pass)
    print(f"Verificando 'MiContraseñaSecreta123!': {user_pass.check_password('MiContraseñaSecreta123!')}")
    print(f"Verificando 'contraseñaIncorrecta': {user_pass.check_password('contraseñaIncorrecta')}")
    user_pass.set_password("NuevaPassSegura456#")
    print(user_pass)
    print(f"Verificando 'NuevaPassSegura456#': {user_pass.check_password('NuevaPassSegura456#')}")
except ValueError as e:
    print(f"Error de contraseña: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
