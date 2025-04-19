from model.user import User

class Employee(User):
    def __init__(self, name, document_id, address, email, phone, position, salary):
        super().__init__(name, document_id, address, email, phone)
        self.position = position
        self.set_salary(salary)
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else: 
            raise ValueError("salario no valido")

    def get_user_type(self):
        return "Employee" 

    @classmethod
    def create_user(cls):
        print("Crea un empleado")

        base_user = super().create_user()

        employee_position= input("ingresa la posiscion del empleado(organizador,vendedor,gerente): ")

        while True:
            try:
                employee_salary = float(input("ingresa el salario que tendra el empleado: "))
                break
            except ValueError as e:
                print(e)
        
        return cls(
            name = base_user.name,
            document_id = base_user.document_id,
            address = base_user.address,
            email = base_user.get_email(),
            phone = base_user.get_phone(),
            position = employee_position,
            salary = employee_salary
        )


