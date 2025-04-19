from model.libro import Item

class Product(Item):
    def __init__(self, name, price):
        self.name = name
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0: 
            self.__price = price
        else:
            raise ValueError("ese precio es invalido deve ser mayor a cero")

    def get_category(self):
        return "Product"

    def description(self):
        print(f"\nlibro: {self.name}, precio: {self.get_price()}")

    def sell(self):
        print(f"\nlibro: {self.name}, precio: {self.get_price()}")

    @classmethod
    def create_product(cls):
        print("\ningresa un nuevo libro")
        name = input("ingresa el nombre del libro: ")

        while True:
            try:
                price = float(input("ingresa el precio del libro: "))
                break
            except ValueError:
                print("precio invalido debe ser mayor a cero.")
        
        product = cls(name, price)

        return product