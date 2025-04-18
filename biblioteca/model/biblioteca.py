from .libro import Libro
from .prestamo import Prestamo
from exceptions.libro_excepciones import LibroNoDisponibleException, UsuarioNoEncontradoException

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_usuario(self, id_usuario):
        for u in self.usuarios:
            if u.id_usuario == id_usuario:
                return u
        raise UsuarioNoEncontradoException("Usuario no encontrado.")

    def buscar_libro(self, isbn):
        for l in self.libros:
            if l._Libro__isbn == isbn:
                return l
        return None

    def prestar_libro(self, isbn, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if not usuario:
            print(f"❌ Error: Usuario con ID '{id_usuario}' no encontrado.")
            return

        libro = next((l for l in self.libros if l._Libro__isbn == isbn), None)
        if not libro:
            print(f"❌ Error: Libro con ISBN '{isbn}' no encontrado.")
            return

        try:
            libro.prestar()
            self.prestamos.append(Prestamo(libro, usuario))
            print("✅ Libro prestado correctamente.")
        except Exception as e:
            print(f"❌ Error al prestar libro: {e}")
    def devolver_libro(self, isbn, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if not usuario:
            print(f"❌ Error: Usuario con ID '{id_usuario}' no encontrado.")
            return

        libro = next((l for l in self.libros if l._Libro__isbn == isbn), None)
        if not libro:
            print(f"❌ Error: Libro con ISBN '{isbn}' no encontrado.")
            return

        try:
            libro.devolver()
            print("✅ Libro devuelto correctamente.")
        except Exception as e:
            print(f"❌ Error al devolver libro: {e}")
