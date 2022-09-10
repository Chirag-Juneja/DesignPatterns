# A partially or fully initialized object that you copy (clone) and use.s

import copy

class Address:
    def __init__(self,street,city,country) -> None:
        self.street = street
        self.city = city
        self.country = country
    def __str__(self) -> str:
        return f'{self.street}, {self.city}, {self.country}'

class Person:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address
    
    def __str__(self) -> str:
        return f'{self.name} lives at {self.address}'

ram = Person("Ram",Address('Ram Mandir','Ayodha','India'))
sita = copy.deepcopy(ram)
sita.name = 'Sita'
print(ram)
print(sita)