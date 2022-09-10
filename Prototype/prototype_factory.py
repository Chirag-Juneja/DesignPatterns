# Prototype Factory
import copy

class Address:
    def __init__(self,cubicle,city,country) -> None:
        self.cubicle = cubicle
        self.city = city
        self.country = country
    def __str__(self) -> str:
        return f'{self.cubicle}, {self.city}, {self.country}'

class Employee:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address
    
    def __str__(self) -> str:
        return f'{self.name} works at {self.address}'

class EmployeeFactory:
    __hyd_office_employee = Employee(None,Address(None,'Hyderabard','India'))
    __cn_office_employee = Employee(None,Address(None,'Chennai','India'))

    @staticmethod
    def __new_employee(prototype,name,cubicle):
        employee = copy.deepcopy(prototype)
        employee.name = name
        employee.address.cubicle = cubicle
        return employee

    @staticmethod
    def new_hyd_office_employee(name,cubicle):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.__hyd_office_employee,
            name,
            cubicle
        )

    @staticmethod
    def new_cn_office_employee(name,cubicle):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.__cn_office_employee,
            name,
            cubicle
        )

kumar = EmployeeFactory.new_hyd_office_employee('Kumar',100)
sai = EmployeeFactory.new_cn_office_employee('Sai',125)
print(kumar)
print(sai)
