# user.py

class User:
    def __init__(self, nombre, user_id):
        self._nombre = nombre
        self._user_id = user_id
        self._libros_prestados = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def user_id(self):
        return self._user_id

    @property
    def libros_prestados(self):
        return self._libros_prestados

    def prestar_libro(self, libro):
        self._libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self._libros_prestados:
            self._libros_prestados.remove(libro)

    def __str__(self):
        libros = ', '.join(libro.titulo for libro in self._libros_prestados) if self._libros_prestados else "Ninguno"
        return f"Nombre: {self._nombre}\nID: {self._user_id}\nLibros prestados: {libros}"
