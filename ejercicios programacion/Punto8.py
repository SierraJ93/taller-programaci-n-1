# Interfaces

from abc import ABC, abstractmethod

class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass

class Pajaro(Volador):
    def volar(self):
        print("El pájaro agita sus alas y vuela por el cielo.")

class Avion(Volador):
    def volar(self):
        print("El avión enciende sus motores y se eleva por la pista.")

if __name__ == "__main__":
    pajaro = Pajaro()
    avion = Avion()

    voladores = [pajaro, avion]

    for volador in voladores:
        volador.volar()
