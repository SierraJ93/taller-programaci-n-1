from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.historial_prestamos = []

    @abstractmethod
    def puede_pedir_prestamo(self):
        pass

    def ver_historial(self):
        return self.historial_prestamos
