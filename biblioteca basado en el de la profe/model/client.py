from model.user import User

class Client(User):
    def __init__(self, name, document_id, address, email, phone, client_type):
        super().__init__(name, document_id, address, email, phone)
        self.client_type = client_type

    def get_user_type(self):
        return "Client"

    @classmethod
    def create_user(cls):
        print("Crea un cliente")

        base_user = super().create_user()

        client_type= input("ingresa el tipo de cliente: ")

        return cls(
            name = base_user.name,
            document_id = base_user.document_id,
            address = base_user.address,
            email = base_user.get_email(),
            phone = base_user.get_phone(),
            client_type = client_type
        )