from .usuario import Usuario

class Profesor(Usuario):
    def puede_pedir_prestamo(self):
        return len(self.historial_prestamos) < 5
    def __str__(self):
        return f"👨‍🏫 Profesor - ID: {self.id_usuario}, Nombre: {self.nombre}"
