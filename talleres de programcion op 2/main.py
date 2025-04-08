from modelos.coche import Coche
from modelos.bicicleta import Bicicleta
from animales.animal import Perro, Gato
from interfaces.volador import Pajaro, Avion
from excepciones.excepciones import ExcesoVelocidadException

marca = input("Ingrese la marca del coche: ")
modelo = input("Ingrese el subnombre o modelo del coche: ")
anio = int(input("Ingrese el año del coche: "))

coche1 = Coche(marca, modelo, anio)
coche1.describir()

tipo_bici = input("Ingrese el tipo de bicicleta (ejm:todoterreno): ")
bici1 = Bicicleta(tipo_bici)

vehiculos = [coche1, bici1]
for vehiculo in vehiculos:
    vehiculo.acelerar()

animales = [Perro(), Gato()]
for animal in animales:
    animal.hacerSonido()

voladores = [Pajaro(), Avion()]
for volador in voladores:
    volador.volar()

try:
    incremento = int(input("¿Cuánto desea usted incrementar la velocidad del coche?: "))
    coche1.incrementarVelocidad(incremento)
except ExcesoVelocidadException as e:
    print(f"Error: {e}")
