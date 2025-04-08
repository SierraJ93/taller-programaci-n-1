#Ejer 7: Clases Abstractas

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print(" El perro dice: ¡Guau guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print(" El gato dice: ¡Miau!")

def probar_animales():
    animales = [Perro(), Gato()]
    
    for animal in animales:
        animal.hacer_sonido()

if __name__ == "__main__":
    probar_animales()
