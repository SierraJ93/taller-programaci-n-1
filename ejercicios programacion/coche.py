
from vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, velocidad=0):
        super().__init__(velocidad)
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
    
    def describir(self):
        print(f"Coche: {self.__marca} {self.__modelo} ({self.__anio})")

    def acelerar(self):
        self.velocidad += 10
        print(f"El coche acelera a {self.velocidad} km/h")
