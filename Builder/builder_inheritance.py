# Buider Inheritance
# Builder Facets violates open-closed principle

class Person:
    def __init__(self) -> None:
        self.name = None
        self.position = None
        self.dob = None
    
    def __str__(self) -> str:
        return f'{self.name} born on {self.dob} works as {self.position}'


    @staticmethod
    def new():
        return PersonBuilder()

class PersonBuilder:
    def __init__(self) -> None:
        self.person = Person()
    
    def build(self):
        return self.person

class PersonInfoBuilder(PersonBuilder):
    def called(self,name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def works_as(self,position):
        self.person.position = position
        return self

class PersonDOBBuilder(PersonJobBuilder):
    def born(self,dob):
        self.person.dob = dob
        return self

pb = PersonDOBBuilder()
person = pb\
        .called('Chirag')\
        .works_as('Data Scientist')\
        .born('8 July')\
        .build()

print(person)


