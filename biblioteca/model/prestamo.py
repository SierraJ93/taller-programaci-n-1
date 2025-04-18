from datetime import datetime

class Prestamo:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = None

    def devolver(self):
        self.fecha_devolucion = datetime.now()
        self.libro.devolver()
