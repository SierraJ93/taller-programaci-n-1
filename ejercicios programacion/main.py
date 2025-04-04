
from coche import Coche
from bicicleta import Bicicleta

marca = input("Ingrese la marca del coche: ")
modelo = input("Ingrese el modelo del coche: ")
anio = int(input("Ingrese el año del coche: "))

coche1 = Coche(marca, modelo, anio)
coche1.describir()

tipo_bici = input("Ingrese el tipo de bicicleta: ")
bici1 = Bicicleta(tipo_bici)

vehiculos = [coche1, bici1]
for vehiculo in vehiculos:
    vehiculo.acelerar()
