# A component which is instantiated only once.
# Singleton by allocator gives reference to same object but still calls the init

import random

class Database:
    __instance = None

    def __init__(self) -> None:
        id = random.randint(1,100)
        print('id:',id)

    def __new__(cls,*args,**kwargs):
        if not cls.__instance:
            cls.__instance = super(Database,cls).__new__(cls,*args,**kwargs)
        return cls.__instance

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1==d2)