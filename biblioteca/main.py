from model.libro import Libro
from model.estudiante import Estudiante
from model.profesor import Profesor
from model.biblioteca import Biblioteca

def mostrar_menu():
    print("\n--- Menú Biblioteca ---")
    print("1. Agregar libro")
    print("2. Registrar estudiante")
    print("3. Registrar profesor")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Ver todos los libros")
    print("7. Ver usuarios registrados")
    print("0. Salir")

if __name__ == "__main__":
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            nombre = input("Nombre del estudiante: ")
            id_estudiante = input("ID del estudiante: ")
            estudiante = Estudiante(nombre, id_estudiante)
            biblioteca.registrar_usuario(estudiante)

        elif opcion == "3":
            nombre = input("Nombre del profesor: ")
            id_profesor = input("ID del profesor: ")
            profesor = Profesor(nombre, id_profesor)
            biblioteca.registrar_usuario(profesor)

        elif opcion == "4":
            isbn = input("ISBN del libro: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == "5":
            isbn = input("ISBN del libro: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == "6":
            for libro in biblioteca.libros:
                print(libro)

        elif opcion == "7":
            for usuario in biblioteca.usuarios:
                print(usuario)

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")
            