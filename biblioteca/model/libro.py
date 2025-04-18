class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__disponible = True

    def prestar(self):
        if not self.__disponible:
            raise Exception("El libro no está disponible.")
        self.__disponible = False

    def devolver(self):
        self.__disponible = True

    def esta_disponible(self):
        return self.__disponible

    def __str__(self):
        return f"{self.__titulo} - {self.__autor} (ISBN: {self.__isbn})"
