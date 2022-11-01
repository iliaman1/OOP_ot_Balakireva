from typing import Any


class Cell:
    def __init__(self, data: Any):
        self.__data = data

    @property
    def data(self) -> Any:
        return self.data

    @data.setter
    def data(self, value: Any) -> None:
        self.data = value


class TableValues:
    def __init__(self, rows: int, cols: int, type_data: Any = int) -> None:
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.lst = [[Cell(0) for _ in range(self.cols)] for _ in range(self.rows)]

    def __getitem__(self, item: tuple):
        if not isinstance(item, tuple) or 0 > item[0] > self.rows or 0 > item[1] > self.cols:
            raise IndexError('неверный индекс')

        return self.lst[item[0]][item[1]]

    def __setitem__(self, key: tuple, value: int) -> None:
        if not isinstance(key, tuple) or 0 > key[0] > self.rows or 0 > key[1] > self.cols:
            raise IndexError('неверный индекс')

        if not isinstance(value, int):
            raise TypeError('неверный тип присваиваемых данных')

        self.lst[key[0]][key[1]] = value

    def __iter__(self):
        self.start_row = 0
        self.start_coll = 0
        return self

    def __next__(self):
        if

