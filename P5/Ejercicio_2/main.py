from library import Library
from book import Book
from user import User
import utils

def main():
    biblioteca = Library()
    usuarios = {}

    while True:
        opcion = utils.crear_menu([
            "Añadir libro",
            "Eliminar libro",
            "Registrar usuario",
            "Realizar préstamo",
            "Realizar devolución",
            "Mostrar todos los libros",
            "Salir"
        ])

        if opcion == 1:
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            biblioteca.añadir(Book(titulo, autor, isbn))

        elif opcion == 2:
            isbn = input("Ingrese el ISBN del libro a eliminar: ")
            biblioteca.quitar(isbn)

        elif opcion == 3:
            nombre = input("Ingrese el nombre del usuario: ")
            user_id = utils.generar_id_unico()
            usuarios[user_id] = User(nombre, user_id)
            print(f"Usuario '{nombre}' registrado con ID: {user_id}")

        elif opcion == 4:
            user_id = input("Ingrese el ID del usuario: ")
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            if user_id in usuarios:
                biblioteca.lend_book(isbn)
            else:
                print("Usuario no encontrado.")

        elif opcion == 5:
            user_id = input("Ingrese el ID del usuario: ")
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            if user_id in usuarios:
                biblioteca.return_book(isbn)
            else:
                print("Usuario no encontrado.")

        elif opcion == 6:
            for book in biblioteca._books:
                print(book)

        elif opcion == 7:
            break

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
