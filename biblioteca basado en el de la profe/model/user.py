

class User:
    def __init__(self, name, document_id, address, email, phone):
        self.name= name
        self.document_id = document_id
        self.address = address
        self.set_email(email)
        self.set_phone(phone)

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def set_email(self, email):
        if "@" in email:
            self.__email = email
        else: 
            raise ValueError("email invalido")
    
    def set_phone(self, phone):
        if phone.isdigit() and len(phone) >= 10:
            self.__phone = phone
        else:
            raise ValueError("numero de telefono invcalido deberiatener 10 digitos")

    def get_user_type(self):
        return "User"

    @classmethod
    def create_user(cls):
        print("Crea un usuario")
        user_name = input("ingresa el nombre del usuario: ")
        user_document_id = input("ingresa el numero de cedula del usuario: ")
        user_address = input("ingresa la direccion de residencia del usuario: ")

        user = User(user_name, user_document_id, user_address, "test@gmail.com", "0000000000")

        while True:
            try:
                user_email = input("ingresa el correo electronico del usuario: ")
                user.set_email(user_email)
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                user_phone = input("ingresa el numero de telefono: ")
                user.set_phone(user_phone)
                break
            except ValueError as e:
                print(e)
                
        return user
