from typing import List, Dict
import uuid

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

