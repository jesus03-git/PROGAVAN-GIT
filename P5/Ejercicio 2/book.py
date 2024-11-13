class Book:
    def __init__(self, titulo, autor, ISBN, prestado):
        self._titulo=titulo
        self._autor=autor
        self._isbn=ISBN
        self._prestado=prestado

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def autor(self, autor):
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, valor):
        self._isbn = valor

    @property
    def prestado(self):
        return self._prestado

    @prestado.setter
    def prestado(self, estado):
        self._prestado = estado

    def __str__(self):
        estado = "Prestado" if self._prestado else "Disponible"
        return f"Título: {self._titulo}\nAutor: {self._autor}\nISBN: {self._isbn}\nEstado: {estado}"