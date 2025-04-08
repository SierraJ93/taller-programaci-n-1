#Ejer 10: Manejo de Excepciones y Clases Personalizadas

class ExcesoVelocidadException(Exception):
   
    def __init__(self, velocidad, mensaje="Velocidad maxima: no se puede superar los 200 km/h."):
        self.velocidad = velocidad
        self.mensaje = mensaje
        super().__init__(f"{mensaje} Velocidad actual: {velocidad} km/h")

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0  # Velocidad inicial en km/h
    
    def incrementar_velocidad(self, velocidad):
        nueva_velocidad = self.velocidad + velocidad
        if nueva_velocidad > 200:
            raise ExcesoVelocidadException(nueva_velocidad)
        self.velocidad = nueva_velocidad
        print(f"Velocidad actual del {self.marca} {self.modelo}: {self.velocidad} km/h")

def probar_coche():
    coche = Coche("Mazda", "Cx 30")
    
    try:
        coche.incrementar_velocidad(100)
        coche.incrementar_velocidad(80)
        coche.incrementar_velocidad(30) 
    except ExcesoVelocidadException as e:
        print( "Error", e)

if __name__ == "__main__":
    probar_coche()
