# Builder Facets

class Person:
    def __init__(self) -> None:
        #address
        self.street = None
        self.postcode = None
        self.city = None
        #employment
        self.company = None
        self.position = None
        self.income = None
    
    @staticmethod
    def create():
        return PersonBuilder()

    def __str__(self) -> str:
        return f'Address:{self.street},{self.postcode},{self.city}\n'+\
            f'Employed at {self.company} as a {self.position} earning {self.income}'
        
class PersonBuilder:
    def __init__(self,person=Person()) -> None:
        self.person = person
    
    @property
    def works(self):
        return PersonJobBuilder(self.person)
    
    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person

class PersonJobBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)
    
    def at(self,company):
        self.person.company = company
        return self
    
    def as_a(self,position):
        self.person.position = position
        return self

    def earns(self,income):
        self.person.income = income
        return self

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)
    
    def at(self,street):
        self.person.street = street
        return self
    
    def with_postcode(self,postcode):
        self.person.postcode = postcode
        return self

    def in_city(self,city):
        self.person.city = city
        return self
    
pb = Person.create()
person = pb\
    .lives\
        .at('121 Baker Street')\
        .with_postcode('50000')\
        .in_city('London')\
    .works\
        .at('Scotland Yard')\
        .as_a('Detective')\
        .earns('Nothing')\
    .build()

print(person)
