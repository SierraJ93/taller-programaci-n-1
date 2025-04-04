
from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, tipo, velocidad=0):
        super().__init__(velocidad)
        self.tipo = tipo

    def acelerar(self):
        self.velocidad += 2
        print(f"La bicicleta acelera a {self.velocidad} km/h")
