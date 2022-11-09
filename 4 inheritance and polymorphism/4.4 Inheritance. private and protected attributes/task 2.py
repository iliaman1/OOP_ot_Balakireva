class Furniture:
    def __init__(self, name: str, weight: (int, float)):
        self.__verify_name(name)
        self.__verify_weight(weight)
        self._name = name
        self._weight = weight

    def __setattr__(self, key, value):
        if key == '_name':
            self.__verify_name(value)
        if key == '_weight':
            self.__verify_weight(value)

        object.__setattr__(self, key, value)

    def __verify_name(self, name: str) -> bool:
        if type(name) != str:
            raise TypeError('название должно быть строкой')

        return True

    def __verify_weight(self, weight: (int, float)) -> bool:
        if type(weight) not in (int, float) or weight <= 0:
            raise TypeError('вес должен быть положительным числом')

        return True

    def get_attrs(self) -> tuple:
        return tuple(self.__dict__.values())


class Closet(Furniture):
    def __init__(self, name: str, weight: (int, float), tp: bool, doors: int):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name: str, weight: (int, float), height: (int, float)):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name: str, weight: (int, float), height: (int, float), square: (int, float)):
        super().__init__(name, weight)
        self._height = height
        self._square = square
