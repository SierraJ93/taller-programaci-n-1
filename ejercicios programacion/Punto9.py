class Motor:
    def __init__(self, potencia, tipo):
        self.potencia = potencia
        self.tipo = tipo

    def describir(self):
        return f"Motor {self.tipo} con {self.potencia} HP."


class Coche:
    def __init__(self, marca, modelo, año, motor):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.motor = motor  

    def describir(self):
        return f"Coche: {self.marca} {self.modelo} ({self.año}) con {self.motor.describir()}"


if __name__ == "__main__":
    motor_v6 = Motor(300, "V6")
    coche = Coche("Ford", "Mustang", 2022, motor_v6)
    print(coche.describir())
