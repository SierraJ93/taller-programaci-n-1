class Vehiculo:
    def __init__(self, velocidad=0):
        self.velocidad = velocidad
    
    def acelerar(self):
        self.velocidad += 5
        print(f"Velocidad actual: {self.velocidad} km/h")
