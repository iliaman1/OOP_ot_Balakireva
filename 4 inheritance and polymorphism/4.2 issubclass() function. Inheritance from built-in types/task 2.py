from typing import Any


class Thing:
    def __init__(self, name: str, price: float, weight: float):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash(self.name)


class DictShop(dict):
    def __init__(self, things: dict = None):
        if things:
            if type(things) != dict:
                raise TypeError('аргумент должен быть словарем')

            for key in things.keys():
                if type(key) != Thing:
                    raise TypeError('ключами могут быть только объекты класса Thing')

            super().__init__(things)

        else:
            super().__init__()

    def __setitem__(self, key: Thing, value: Any):
        if type(key) != Thing:
            raise TypeError('ключами могут быть только объекты класса Thing')

        super().__setitem__(key, value)
