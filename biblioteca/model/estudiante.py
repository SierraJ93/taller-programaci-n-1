from .usuario import Usuario

class Estudiante(Usuario):
    def puede_pedir_prestamo(self):
        return len(self.historial_prestamos) < 3
    def __str__(self):
        return f"👨‍🎓 Estudiante - ID: {self.id_usuario}, Nombre: {self.nombre}"
