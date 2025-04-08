from abc import ABC, abstractmethod

class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass

class Pajaro(Volador):
    def volar(self):
        print("El pajaro vuela moviendo sus alas.")

class Avion(Volador):
    def volar(self):
        print("El avión despega y vuela a una gran altura.")
