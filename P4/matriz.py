import numpy as np

class CMatFloat:
    def __init__(self):
        self.Matriz = None
        self.m_nFilas = 0
        self.m_nColumnas = 0

    def CrearMatriz2D(self, nFilas, nColumnas):
        self.Matriz = np.zeros((nFilas, nColumnas))
        self.m_nFilas = nFilas
        self.m_nColumnas = nColumnas

    def CrearMatriz1D(self, nElementos):
        self.Matriz = np.zeros((1, nElementos))
        self.m_nFilas = 1
        self.m_nColumnas = nElementos

    def Introducir(self):
        for i in range(self.m_nFilas):
            for j in range(self.m_nColumnas):
                self.Matriz[i, j] = leer_float(f"Introduce un número para la posición [{i}, {j}]: ")

    def Mostrar(self):
        print(self.Matriz)

    def Existe(self):
        return self.Matriz is not None and self.Matriz.size > 0

    def SumarMatrices(self, Matriz2):
        if self.Matriz.shape == Matriz2.Matriz.shape:
            return self.Matriz + Matriz2.Matriz
        else:
            print("Las matrices deben tener las mismas dimensiones.")

    def RestarMatrices(self, Matriz2):
        if self.Matriz.shape == Matriz2.Matriz.shape:
            return self.Matriz - Matriz2.Matriz
        else:
            print("Las matrices deben tener las mismas dimensiones.")


def leer_int(mensaje="Introduce un número entero: "):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")

def leer_float(mensaje="Introduce un número decimal: "):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Por favor, introduce un número decimal válido.")


def crear_menu(opciones_menu):
    while True:
        print("\nMenú:")
        for i, opcion in enumerate(opciones_menu, 1):
            print(f"{i}. {opcion}")

        opcion = leer_int("Selecciona una opción: ")

        if 1 <= opcion <= len(opciones_menu):
            return opcion
        else:
            print("Error: Selecciona una opción válida.")


def main():
    opciones_menu_principal = [
        "Construir matriz 1D",
        "Construir matriz 2D",
        "Introducir matriz",
        "Mostrar matriz",
        "Operaciones con matrices",
        "Terminar"
    ]

    opciones_menu_operaciones = [
        "Sumar matrices",
        "Restar matrices",
        "Volver al menú principal"
    ]

    matriz = CMatFloat()

    while True:
        opcion_principal = crear_menu(opciones_menu_principal)

        if opcion_principal == 1:
            n_elementos = leer_int("Introduce el número de elementos para el vector: ")
            matriz.CrearMatriz1D(n_elementos)
            print("Matriz 1D creada.")

        elif opcion_principal == 2:
            filas = leer_int("Introduce el número de filas: ")
            columnas = leer_int("Introduce el número de columnas: ")
            matriz.CrearMatriz2D(filas, columnas)
            print("Matriz 2D creada.")

        elif opcion_principal == 3:
            if matriz.Existe():
                matriz.Introducir()
                print("Valores introducidos en la matriz.")
            else:
                print("Error: No se ha creado ninguna matriz. Usa las opciones 1 o 2 para crear una.")

        elif opcion_principal == 4:
            if matriz.Existe():
                matriz.Mostrar()
            else:
                print("Error: No se ha creado ninguna matriz para mostrar.")

        elif opcion_principal == 5:
            if not matriz.Existe():
                print("Error: No se ha creado una matriz principal.")
                continue

            while True:
                opcion_operacion = crear_menu(opciones_menu_operaciones)

                if opcion_operacion == 1:
                    matriz2 = CMatFloat()
                    filas = matriz.m_nFilas
                    columnas = matriz.m_nColumnas
                    matriz2.CrearMatriz2D(filas, columnas)
                    matriz2.Introducir()
                    resultado = matriz.SumarMatrices(matriz2)
                    if resultado is not None:
                        print("Resultado de la suma:")
                        print(resultado)

                elif opcion_operacion == 2:
                    matriz2 = CMatFloat()
                    filas = matriz.m_nFilas
                    columnas = matriz.m_nColumnas
                    matriz2.CrearMatriz2D(filas, columnas)
                    matriz2.Introducir()
                    resultado = matriz.RestarMatrices(matriz2)
                    if resultado is not None:
                        print("Resultado de la resta:")
                        print(resultado)

                elif opcion_operacion == 3:
                    break

        elif opcion_principal == 6:
            print("Programa terminado.")
            break


if __name__ == "__main__":
    main()
