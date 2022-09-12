# Singleton using metaclass
import random

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self) -> None:
        id = random.randint(1, 100)
        print('id:', id)


d1 = Database()
d2 = Database()
print(d1 == d2)