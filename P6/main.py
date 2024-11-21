from time_management import Time
import utils

class Ficha:
    def __init__(self):
        self._nombre = ""
        self._edad = 0
        self._nacio = "12:00:00 AM"
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    @property
    def nacio(self):
        return self._nacio
    
    @nacio.setter
    def nacio(self, nueva_fecha):
        self._nacio = nueva_fecha

    # def Visualizar():