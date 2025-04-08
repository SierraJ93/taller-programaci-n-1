from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacerSonido(self):
        pass



class Perro(Animal):
    def hacerSonido(self):
        print("El perro suena: ¡Guauuuuuuuuuuuuu!")



class Gato(Animal):
    def hacerSonido(self):
        print("El gato suena: ¡Miauuuuuuuuuuuuuuuu!")
