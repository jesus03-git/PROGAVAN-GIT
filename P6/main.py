# Importamos módulos
from time_management import Time
from utils import leer_int, leer_cadena, crear_menu

class Ficha:
    def __init__(self, nombre="", edad=0, nacio=None):
        self._nombre = nombre
        self._edad = edad
        self._nacio = nacio if nacio else Time()

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def nacio(self):
        return self._nacio

    def visualizar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Nacimiento: {self.nacio.get_time()}"

class Empleado(Ficha):
    def __init__(self, nombre, edad, nacio, categoria, antiguedad):
        super().__init__(nombre, edad, nacio)
        self._categoria = categoria
        self._antiguedad = antiguedad

    @property
    def categoria(self):
        return self._categoria

    @property
    def antiguedad(self):
        return self._antiguedad

    def visualizar(self):
        base_info = super().visualizar()
        return f"{base_info}, Categoría: {self.categoria}, Antigüedad: {self.antiguedad} años"

class Cliente(Ficha):
    def __init__(self, nombre, edad, nacio, dni):
        super().__init__(nombre, edad, nacio)
        self._dni = dni

    @property
    def dni(self):
        return self._dni

    def visualizar(self):
        base_info = super().visualizar()
        return f"{base_info}, DNI: {self.dni}"

    def __eq__(self, other):
        return isinstance(other, Cliente) and self.nombre == other.nombre and self.edad == other.edad

class RegistroDiario:
    def __init__(self):
        self._personas = []

    def agregar_persona(self, persona):
        if isinstance(persona, (Empleado, Cliente)):
            self._personas.append(persona)
        else:
            raise TypeError("Solo se pueden agregar instancias de Empleado o Cliente.")

    def visualizar_registro(self):
        for persona in self._personas:
            print(persona.visualizar())

    def visualizar_empleados(self):
        for persona in self._personas:
            if isinstance(persona, Empleado):
                print(persona.visualizar())

    def es_empleado(self, persona):
        return isinstance(persona, Empleado)

    def __getitem__(self, index):
        return self._personas[index]

    def __add__(self, otro_registro):
        nuevo_registro = RegistroDiario()
        nuevo_registro._personas = self._personas + otro_registro._personas
        return nuevo_registro

def main():
    registro = RegistroDiario()

    while True:
        opciones = [
            "Introducir empleado",
            "Introducir cliente",
            "Buscar por nombre y edad",
            "Mostrar registro diario",
            "Mostrar empleados",
            "Visualizar persona por índice",
            "Combinar registros diarios",
            "Salir"
        ]
        opcion = crear_menu(opciones)

        if opcion == 1:
            nombre = leer_cadena("Nombre del empleado: ")
            edad = leer_int("Edad del empleado: ")
            categoria = leer_cadena("Categoría del empleado: ")
            antiguedad = leer_int("Antigüedad en años: ")
            hora_nacimiento = Time.from_string(leer_cadena("Hora de nacimiento (HH:MM:SS FORMAT): "))
            empleado = Empleado(nombre, edad, hora_nacimiento, categoria, antiguedad)
            registro.agregar_persona(empleado)

        elif opcion == 2:
            nombre = leer_cadena("Nombre del cliente: ")
            edad = leer_int("Edad del cliente: ")
            dni = leer_cadena("DNI del cliente: ")
            hora_nacimiento = Time.from_string(leer_cadena("Hora de nacimiento (HH:MM:SS FORMAT): "))
            cliente = Cliente(nombre, edad, hora_nacimiento, dni)
            registro.agregar_persona(cliente)

        elif opcion == 3:
            nombre = leer_cadena("Nombre: ")
            edad = leer_int("Edad: ")
            encontrado = False
            for persona in registro._personas:
                if persona.nombre == nombre and persona.edad == edad:
                    print(f"Encontrado: {persona.visualizar()} ({'Empleado' if isinstance(persona, Empleado) else 'Cliente'})")
                    encontrado = True
            if not encontrado:
                print("No se encontró a la persona.")

        elif opcion == 4:
            registro.visualizar_registro()

        elif opcion == 5:
            registro.visualizar_empleados()

        elif opcion == 6:
            indice = leer_int("Índice: ")
            try:
                print(registro[indice].visualizar())
            except IndexError:
                print("Índice fuera de rango.")

        elif opcion == 7:
            nuevo_registro = RegistroDiario()
            print("Agrega dos personas al nuevo registro para combinar:")
            for _ in range(2):
                nombre = leer_cadena("Nombre: ")
                edad = leer_int("Edad: ")
                hora_nacimiento = Time.from_string(leer_cadena("Hora de nacimiento (HH:MM:SS FORMAT): "))
                if leer_cadena("Es empleado? (s/n): ").lower() == 's':
                    categoria = leer_cadena("Categoría del empleado: ")
                    antiguedad = leer_int("Antigüedad en años: ")
                    nuevo_registro.agregar_persona(Empleado(nombre, edad, hora_nacimiento, categoria, antiguedad))
                else:
                    dni = leer_cadena("DNI del cliente: ")
                    nuevo_registro.agregar_persona(Cliente(nombre, edad, hora_nacimiento, dni))
            registro += nuevo_registro
            print("Registros combinados exitosamente.")

        elif opcion == 8:
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()
