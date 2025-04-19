from model.product import Product
from model.prestamo_del_libro import Service
from model.store import Store
from model.user import User
from model.empleado import Employee
from model.client import Client
items = []
def add_item():
    print("\ntu quieres ingresar un libro o un servicio?")
    choice = input("Escriba 'p' para Producto o 's' para Servicio: ").lower()

    if choice == 'p':
        product = Product.create_product()
        items.append(product)
        print("libro agregado exitosamente.")
    elif choice == 's':
        service = Service.create_service()
        items.append(service)
        print("servicio agregado exitosamente")
    else:
        print("esa no es una opcion valida. ")

def show_items():
    print("elemento")
    for i in items:
        i.sell()
def sell_item():
    if not items:
        print("\nno hay libros para vender o prestar.")
        return

    print("\nselecciona el libro a vender:")
    for idx, s in enumerate(items):
        print(f"{idx + 1}. {s.name}")

    while True:
        try:
            selection = int(input("ingresa el numero: ")) - 1
            if 0 <= selection < len(items):
                item = items[selection]
                print(f"\n venta '{item.name}'...")
                item.sell()
                break
            else:
                print("opcion invalida.")
        except ValueError:
            print("ingresa un numeroi valido.")

users = []

def add_user():
    print("\n¿Quieres crear un usuario regular, un empleado o un cliente?")
    choice = input("Escriba 'u' para Usuario, 'e' para Empleado o 'c' para cliente: ").lower()

    if choice == 'u':
        user = User.create_user()
        users.append(user)
        print("usuario ingresado exitosamente.")
    elif choice == 'e':
        employee = Employee.create_user()
        users.append(employee)
        print("empleado ingresado exitosamente")
    elif choice == 'c':
        client = Client.create_user()
        users.append(client)
        print("cliente ingresado exitosamente")
    else:
        print("opcion invalida. ")

def show_users():
    print("\nregistro de usuario")
    for u in users:
        print(f"\nNombre de usuario: {u.name}")
        print(f"Numero de cedula: {u.document_id}")
        print(f"Direccion de recidencia: {u.address}")
        print(f"Correo electronico: {u.get_email()}")
        print(f"Numero de telefono: {u.get_phone()}")
        print(f"TIPO DE USUARIO: {u.get_user_type()}")

while True:
    print("\nMenu principal")
    print("1. libros y servicios")
    print("2. Menu de usuario")
    print("3. vender libro")
    print("4. salir")
    main_option = input("Elige una opción:")

    if main_option == "1":
        while True:
            print("\nMenu de libros y servicios")
            print("1. agreagr libro")
            print("2. lsita de libros")
            print("3. Salir")
            option = input("Elige una opción: ")

            if option == "1":
                add_item()
            elif option == "2":
                show_items()
            elif option == "3":
                break
            else:
                print("opcion invalida.")
    elif main_option == "2":
        while True:
            print("\nmenude usuario")
            print("1. agreagar usuario")
            print("2. LIsta de usuarios")
            print("3. Salir")
            option = input("Elige una opción: ")

            if option == "1":
                add_user()
            elif option == "2":
                show_users()
            elif option == "3":
                break
            else:
                print("opcion invalida.")
    elif main_option == "3":
        sell_item()
    elif main_option == "4":
        break
    else:
        print("opcion invalida")













