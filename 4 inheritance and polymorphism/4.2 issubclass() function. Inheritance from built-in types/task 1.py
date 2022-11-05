from typing import Any


class ListInteger(list):
    def __init__(self, iterable):
        super().__init__(self.checker(item) for item in iterable)

    def __setitem__(self, key, value):
        super().__setitem__(key, self.checker(value))

    def append(self, item):
        super().append(self.checker(item))

    @staticmethod
    def checker(value: Any):
        if type(value) != int:
            raise TypeError('можно передавать только целочисленные значения')
        return value

s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError
