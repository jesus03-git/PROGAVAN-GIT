from typing import List, Dict
import uuid
import json
from excepciones import ErrorArchivo

# Funciones originales
def leer_int(mensaje="Introduce un número entero: ") -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")

def leer_float(mensaje="Introduce un número decimal: ") -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Por favor, introduce un número decimal válido.")

def leer_cadena(mensaje="Introduce un mensaje: ") -> str:
    while True:
        cadena = input(mensaje).strip()
        if cadena:
            return cadena
        print("Error: La cadena no puede estar vacía. Inténtalo de nuevo.")

def crear_menu(opciones_menu: List[str]) -> int:
    while True:
        print("\nMenú:")
        for i, opcion in enumerate(opciones_menu, 1):
            print(f"{i}. {opcion}")

        opcion = leer_int("Selecciona una opción: ")

        if 1 <= opcion <= len(opciones_menu):
            return opcion
        else:
            print("Error: Selecciona una opción válida.")

def generar_id_unico() -> str:
    return str(uuid.uuid4())[:8]

def guardar_publicaciones(ruta: str, publicaciones: list):
    try:
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump([
                {"tipo": p.__class__.__name__, **p.__dict__}
                for p in publicaciones
            ], f, indent=4)
    except Exception as e:
        raise ErrorArchivo(f"No se pudo guardar el archivo: {e}")

def cargar_publicaciones(ruta: str) -> list:
    from publicacion import Libro, Revista
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            data = json.load(f)
            publicaciones = []
            for item in data:
                tipo = item.pop("tipo", "")
                if tipo == "Libro":
                    publicaciones.append(Libro(**item))
                elif tipo == "Revista":
                    publicaciones.append(Revista(**item))
            return publicaciones
    except Exception as e:
        raise ErrorArchivo(f"No se pudo cargar el archivo: {e}")
