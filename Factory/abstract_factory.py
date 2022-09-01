# Abstract Factory is not necessary in python since it uses duck typing
from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def __init__(self,amount) -> None:
        self.amount =amount

    def consume(self):
        print('This tea is delicious')

class Coffee(HotDrink):
    def __init__(self,amount) -> None:
        self.amount =amount

    def consume(self):
        print('This coffee is delicious')


class HotDrinkFactory(ABC):
    def prepare(self,amount):
        pass

class TeaFactory(HotDrinkFactory):

    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea(amount)

class CoffeeFactory(HotDrinkFactory):

    def prepare(self, amount):
        print(f'Ground beans, boil water, pour {amount}ml, enjoy!')
        return Coffee(amount)

class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self) -> None:
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0]+d.name[1:].lower()
                factory_name = name+'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name,factory_instance))
    
    def make_drink(self):
        print('Available drinks:')
        for f in self.factories:
            print(f[0])
        
        s = input(f'Please pick a drink (0-{len(self.factories)-1})')
        idx = int(s)
        s = input(f'Specify amount:')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)

hdm = HotDrinkMachine()
hdm.make_drink().consume()


