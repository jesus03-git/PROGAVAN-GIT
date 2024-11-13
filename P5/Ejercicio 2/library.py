from book import Book

class Library():
    def __init__(self):
        self.books= []

    def añadir(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Libro '{book.titulo}' agregado a la biblioteca")
        else:
            raise TypeError("Solo se pueden agregar objetos de la clase Book.")

    def quitar(self, isbn):
        for book in self._books:
            if book.isbn == isbn:
                self._books.remove(book)
                print(f"Libro con ISBN '{isbn}' eliminado de la biblioteca.")
                return
        print(f"No se encontro ningun libro con ISBN '{isbn}' en la biblioteca.")

    def prestar(self, isbn):
        for book in self._books:
            if book.isbn == isbn:
                if not book.prestado:
                    book.prestado = True
                    printf(f"Libro '{book.titulo}' ha sido prestado.")
                else:
                    print(f"Libro '{book.titulo}' ya está prestado")
                return
        print(f"No se encontró ningun libro con ISBN '{isbn}' en la biblioteca")

    def devolver(self, isbn):
        for book in self._books:
            if book.isbn == isbn:
                if book.prestado:
                    book.prestado = False
                    print(f"Libro '{book.titulo}' ha sido devuelto.")
                else:
                    print(f"Libro '{book.titulo}' no estaba prestado.")
                return
        print(f"No se encontró ningun libro con ISBN '{isbn}' para devolver.")

    def buscar_titulo(selfs, titulo):
        libros_encontrados = [book for book in self._books if title.lower() in book.titulo.lower()]
        if libros_encontrados:
            print(f"Libros encontrados con título '{titulo}':")
            for book in libros_encontrados:
                print(book)
        else:
            print(f"No se encontraron libros con el titulo '{titulo}'.")

    def buscar_autor(self, autor):
        libros_encontrados = [book for book in self._books if title.lower() in book.titulo.lower()]
        if libros_encontrados:
            print(f"Libros encontrados del autor '{autor}':")
            for book in libros_encontrados:
                print(book)
        else:
            print(f"No se encontraron libros del autor '{autor}'.")