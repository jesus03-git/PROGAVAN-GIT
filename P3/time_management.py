
# Jesús Gay Canelada y María Mercader Rubio

import re

class Time:
    """
    Clase que representa una hora en formato AM/PM o de 24 horas.

    Atributos de Clase:
        TIME_FORMATS    # ("AM", "PM", "24 HOURS")
        time_count = 0  # Cuenta la cantidad de objetos Time creados

    Atributos:
        hours      # Almacena las horas (1 a 12 para AM/PM, 0 a 23 para 24 horas)
        minutes    # Almacena los minutos (0 a 59)
        seconds    # Almacena los segundos (0 a 59)
        format     # Almacena el formato de la hora: “AM", "PM", "24 HOURS"
    """

    TIME_FORMATS = ("AM", "PM", "24 HOURS")
    time_count = 0

    def __init__(self):
        """
        Inicializa los atributos de la clase Time a valores predeterminados (0 horas, minutos, segundos y formato "24 HOURS").
        """
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.format = "24 HOURS"
        Time.time_count += 1

    def __assign_format(self, formato):
        """
        Asigna el formato proporcionado a la hora y lo valida.

        Args:
            formato (str): Formato de tiempo ("AM", "PM" o "24 HOURS").

        Returns:
            bool: True si el formato es válido, False en caso contrario.
        """
        formato = formato.upper()
        if formato in Time.TIME_FORMATS:
            self.format = formato
            return True
        return False

    def __is_24hour_format(self):
        """
        Verifica si el formato de hora es "24 HOURS".

        Returns:
            bool: True si el formato es "24 HOURS", False en caso contrario.
        """
        return self.format == "24 HOURS"

    def _is_valid_time(self):
        """
        Valida si la hora, minutos y segundos son correctos de acuerdo al formato asignado.

        Returns:
            bool: True si la hora es válida, False en caso contrario.
        """
        if self.__is_24hour_format():
            return 0 <= self.hours <= 23 and 0 <= self.minutes <= 59 and 0 <= self.seconds <= 59
        elif self.format in ["AM", "PM"]:
            return 1 <= self.hours <= 12 and 0 <= self.minutes <= 59 and 0 <= self.seconds <= 59
        return False

    def set_time(self, nHoras, nMinutos, nSegundos, formatoo):
        """
        Asigna la hora, minutos, segundos y el formato proporcionados a la instancia Time.

        Args:
            nHoras (int): Horas (1 a 12 para AM/PM, 0 a 23 para formato de 24 horas).
            nMinutos (int): Minutos (0 a 59).
            nSegundos (int): Segundos (0 a 59).
            formatoo (str): Formato de tiempo ("AM", "PM" o "24 HOURS").

        Returns:
            bool: True si la hora se asignó correctamente, False en caso contrario.
        """
        if self.__assign_format(formatoo):
            self.hours = nHoras
            self.minutes = nMinutos
            self.seconds = nSegundos
            return self._is_valid_time()
        return False

    def get_time(self):
        """
        Devuelve la hora actual de la instancia Time en formato "HH:MM:SS FORMAT".

        Returns:
            str: Cadena que representa la hora actual en formato "HH:MM:SS FORMAT".
        """
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02} {self.format}"

    @classmethod
    def from_string(cls, time_string):
        """
        Crea una instancia Time a partir de una cadena con formato "HH:MM:SS FORMAT".

        Args:
            time_string (str): Cadena que representa la hora en formato "HH:MM:SS FORMAT".

        Returns:
            Time: Objeto Time creado con la hora proporcionada o None si la cadena es inválida.
        """
        time_pattern = r"^(\d{2}):(\d{2}):(\d{2}) (AM|PM|24 HOURS)$"
        match = re.match(time_pattern, time_string)

        if match:
            hours, minutes, seconds, time_format = match.groups()
            new_time = cls()
            if new_time.set_time(int(hours), int(minutes), int(seconds), time_format):
                return new_time
            else:
                print("Valores de tiempo no válidos.")
        else:
            print("Formato de cadena de tiempo no válido.")
        return None

    @staticmethod
    def is_valid_format(time_format):
        """
        Verifica si el formato de tiempo proporcionado es válido (AM, PM o 24 HOURS).

        Args:
            time_format (str): Formato de tiempo a validar.

        Returns:
            bool: True si el formato es válido, False en caso contrario.
        """
        return time_format.upper() in Time.TIME_FORMATS

    @classmethod
    def get_time_count(cls):
        """
        Devuelve el número total de instancias Time creadas.

        Returns:
            int: Número total de objetos Time creados.
        """
        return cls.time_count


def mostrar_hora(time_obj):
    """
    Devuelve la hora de una instancia Time en una cadena formateada.

    Args:
        time_obj (Time): Objeto Time.

    Returns:
        str: Hora formateada en formato "HH:MM:SS FORMAT", o un mensaje si no hay hora establecida.
    """
    if time_obj:
        return time_obj.get_time()
    else:
        return "No hay hora establecida."


def main():
    """
    Función principal que maneja el menú del programa, permitiendo al usuario introducir,
    visualizar y crear horas a partir de una cadena, o salir del programa.
    """
    time_obj = None  # Inicialmente no hay hora asignada
    while True:
        print("\nMenú:")
        print("1. Introducir una nueva hora")
        print("2. Visualizar hora actual")
        print("3. Crear una hora a partir de una cadena")
        print("4. Terminar")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            continue

        if opcion == 1:
            try:
                horas = int(input("Ingrese las horas: "))
                minutos = int(input("Ingrese los minutos: "))
                segundos = int(input("Ingrese los segundos: "))
                formato = input("Ingrese el formato de la hora (AM, PM, 24 HOURS): ").upper()

                if Time.is_valid_format(formato):
                    new_time = Time()
                    if new_time.set_time(horas, minutos, segundos, formato):
                        time_obj = new_time
                        print("Hora establecida correctamente.")
                    else:
                        print("Hora no válida según el formato.")
                else:
                    print("Formato de hora no válido.")
            except ValueError:
                print("Entrada no válida. Asegúrese de ingresar números para horas, minutos y segundos.")

        elif opcion == 2:
            if time_obj:
                print(f"La hora actual es: {mostrar_hora(time_obj)}")
            else:
                print("No se ha establecido ninguna hora.")

        elif opcion == 3:
            time_string = input("Ingrese la hora en formato HH:MM:SS FORMAT: ")
            new_time = Time.from_string(time_string)
            if new_time:
                time_obj = new_time
                print("Hora creada correctamente a partir de la cadena.")
            else:
                print("Error al crear la hora desde la cadena.")

        elif opcion == 4:
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione entre 1 y 4.")


if __name__ == "__main__":
    main()
