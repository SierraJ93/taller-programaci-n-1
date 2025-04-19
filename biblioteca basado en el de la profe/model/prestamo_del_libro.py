from model.libro import Item

class Service(Item):
    def __init__(self, name, hourly_rate, estimated_hours):
        self.name = name
        self.hourly_rate = hourly_rate
        self.estimated_hours = estimated_hours

    def sell(self):
        print(f"Prestamo de un libro {self.name}, Rate: {self.hourly_rate}, Horas: {self.estimated_hours}, Total: {self.hourly_rate * self.estimated_hours}")

    @classmethod
    def create_service(cls):
        print("\ncrea la plantoilla del prestamo")
        name = input("ingresa el nombre del libro prestado: ")
        rate = float(input("precio por hora del prestamo dl libro: "))
        hours = float(input("ingresa el numero de horas estimados: "))
               
        service = cls(name, rate, hours)
        return service