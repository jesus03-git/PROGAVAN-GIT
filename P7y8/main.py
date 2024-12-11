from utils import leer_int, leer_cadena, crear_menu

class Publicacion:
    def __init__(self, titulo = "", autor = "", anio = 0):
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
    
    def Descripcion(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Anio: {self.anio}"
    
class Libro(Publicacion):
    def __init__(self, titulo = "", autor = "", anio = 0, genero = ""):
        super().__init__(titulo, autor, anio)
        self._genero = genero
        
    @property
    def genero(self):
        return self._genero
    
    def Descripcion(self):
        base_info = super().Descripcion()
        return f"{base_info}, Genero: {self.genero}"
    
class Revista(Publicacion):
    def __init__(self, titulo = "", autor = "", anio = 0, num_edicion = 0):
        super().__init__(titulo, autor, anio)
        self._num_edicion = num_edicion
    
    @property
    def num_edicion(self):
        return self._num_edicion
    
    def Descripcion(self):
        base_info = super().Descripcion()
        return f"{base_info}, Numero Edicion: {self.num_edicion}"
    
def main():
    while True:
        opciones = [
            "Anañdir publicaciones (libros o revistas)."
            "Mostrar publicaciones disponibles."
            "Guardar publicaciones en un fichero."
            "Cargar publicaciones desde un fichero."
            "Salir."
        ]
        
        opcion = crear_menu(opciones)
        if opcion == 1:
            pass
        
        
        elif opcion == 5:
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()