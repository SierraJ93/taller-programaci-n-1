from modelos.vehiculo import Vehiculo
from excepciones.excepciones import ExcesoVelocidadException

class Motor:
    def __init__(self, potencia, tipo):
        self.potencia = potencia
        self.tipo = tipo

    def describir(self):
        return f"Motor {self.potencia} hp, tipo {self.tipo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, velocidad=0):
        super().__init__(velocidad)

        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.motor = Motor(150, "Gasolina")
    
    def describir(self):
        print(f"Coche: {self.__marca} {self.__modelo} ({self.__anio}) - {self.motor.describir()}")

    def acelerar(self):
        self.velocidad += 10
        print(f"El coche acelera a {self.velocidad} km/h")

    def incrementarVelocidad(self, incremento):
        if self.velocidad + incremento > 200:
            raise ExcesoVelocidadException()
        self.velocidad += incremento
        print(f"Velocidad aunmentada en {self.velocidad} km/h")
