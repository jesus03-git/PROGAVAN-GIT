from publicacion import Libro, Revista
from excepciones import ErrorBiblioteca, ErrorArchivo
from utils import leer_cadena, leer_int, crear_menu, guardar_publicaciones, cargar_publicaciones

publicaciones = []

while True:
    opcion = crear_menu([
        "Añadir publicaciones",
        "Mostrar publicaciones",
        "Guardar publicaciones en un fichero",
        "Cargar publicaciones desde un fichero",
        "Salir"
    ])

    if opcion == 1:
        tipo = crear_menu(["Libro", "Revista"])
        try:
            titulo = leer_cadena("Título: ")
            autor = leer_cadena("Autor: ")
            anio = leer_int("Año de publicación: ")

            if tipo == 1:
                genero = leer_cadena("Género: ")
                publicaciones.append(Libro(titulo, autor, anio, genero))
            else:
                edicion = leer_int("Número de edición: ")
                publicaciones.append(Revista(titulo, autor, anio, edicion))

            print("Publicación añadida correctamente.")
        except (ValueError, ErrorBiblioteca) as e:
            print(f"Error al añadir la publicación: {e}")

    elif opcion == 2:
        if publicaciones:
            for pub in publicaciones:
                print(pub.descripcion())
        else:
            print("No hay publicaciones registradas.")

    elif opcion == 3:
        ruta = leer_cadena("Nombre del fichero para guardar (ej. datos.json): ")
        try:
            guardar_publicaciones(ruta, publicaciones)
            print("Publicaciones guardadas correctamente.")
        except ErrorArchivo as e:
            print(e)

    elif opcion == 4:
        ruta = leer_cadena("Nombre del fichero para cargar (ej. datos.json): ")
        try:
            publicaciones = cargar_publicaciones(ruta)
            print("Publicaciones cargadas correctamente.")
        except ErrorArchivo as e:
            print(e)

    elif opcion == 5:
        print("Programa finalizado.")
        break
