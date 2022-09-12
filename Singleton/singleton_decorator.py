# Singleton with decorator

import random


def singleton(_class):
    instances = {}

    def get_instance(*args, **kwargs):
        if _class not in instances:
            instances[_class] = _class(*args, **kwargs)
        return instances[_class]

    return get_instance


@singleton
class Database:
    def __init__(self) -> None:
        id = random.randint(1, 100)
        print('id:', id)


d1 = Database()
d2 = Database()
print(d1 == d2)
