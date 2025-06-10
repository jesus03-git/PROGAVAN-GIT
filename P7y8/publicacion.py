class Publicacion:
    def __init__(self, titulo: str, autor: str, anio: int):
        if not titulo or not autor or anio <= 0:
            raise ValueError("Datos inválidos para la publicación")
        self._titulo = titulo
        self._autor = autor
        self._anio = anio

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def anio(self):
        return self._anio

    def descripcion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}"


class Libro(Publicacion):
    def __init__(self, titulo, autor, anio, genero):
        super().__init__(titulo, autor, anio)
        if not genero:
            raise ValueError("El género no puede estar vacío")
        self._genero = genero

    @property
    def genero(self):
        return self._genero

    def descripcion(self):
        return f"[Libro] {super().descripcion()}, Género: {self.genero}"


class Revista(Publicacion):
    def __init__(self, titulo, autor, anio, num_edicion):
        super().__init__(titulo, autor, anio)
        if num_edicion <= 0:
            raise ValueError("Número de edición inválido")
        self._num_edicion = num_edicion

    @property
    def num_edicion(self):
        return self._num_edicion

    def descripcion(self):
        return f"[Revista] {super().descripcion()}, Nº Edición: {self.num_edicion}"
