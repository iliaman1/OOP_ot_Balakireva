class CellException(Exception):
    pass


class CellIntegerException(CellException):
    def __str__(self):
        return 'значение выходит за допустимый диапазон'


class CellFloatException(CellException):
    def __str__(self):
        return 'значение выходит за допустимый диапазон'


class CellStringException(CellException):
    def __str__(self):
        return 'длина строки выходит за допустимый диапазон'


class CellInteger:
    def __init__(self, min_value: int, max_value: int):
        self._min_value = min_value
        self._max_value = max_value
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if self._min_value <= val <= self._max_value:
            self.__value = val
        else:
            raise CellIntegerException


class CellFloat:
    def __init__(self, min_value: int, max_value: int):
        self._min_value = min_value
        self._max_value = max_value
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if self._min_value <= val <= self._max_value:
            self.__value = val
        else:
            raise CellFloatException


class CellString:
    def __init__(self, min_length: int, max_length: int):
        self._min_length = min_length
        self._max_length = max_length
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if self._min_length <= len(val) <= self._max_length:
            self.__value = val
        else:
            raise CellStringException


class TupleData:
    def __init__(self, *args):
        for cell in args:
            if not isinstance(cell, (CellInteger, CellFloat, CellString)):
                raise CellException
        self.table = list(args)

    def __getitem__(self, item):
        if 0 > item > len(self.table)-1:
            raise IndexError
        return self.table[item].value

    def __setitem__(self, key, value):
        if 0 > key > len(self.table)-1:
            raise IndexError
        self.table[key].value = value

    def __len__(self):
        return len(self.table)
