from typing import Any


class Cell:
    def __init__(self, data: Any = 0):
        self.__data = data

    @property
    def data(self) -> Any:
        return self.__data

    @data.setter
    def data(self, value: Any) -> None:
        self.__data = value


class TableValues:
    def __init__(self, rows: int, cols: int, type_data: Any = int) -> None:
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.lst = [[Cell(0) for _ in range(self.cols)] for _ in range(self.rows)]

    def __getitem__(self, item: tuple) -> Cell:
        if not isinstance(item, tuple) or 0 > item[0] > self.rows or 0 > item[1] > self.cols:
            raise IndexError('неверный индекс')

        return self.lst[item[0]][item[1]]

    def __setitem__(self, key: tuple, value: int) -> None:
        if not isinstance(key, tuple) or 0 > key[0] > self.rows or 0 > key[1] > self.cols:
            raise IndexError('неверный индекс')

        if not isinstance(value, int):
            raise TypeError('неверный тип присваиваемых данных')

        self.lst[key[0]][key[1]].data = value

    def __iter__(self):
        self.current_row = 0
        self.current_coll = 0
        return self

    def __next__(self):
        if self.current_row < len(self.lst) and self.current_coll < len(self.lst[self.current_row]):
            temp_res = self.lst[self.current_row]
            self.current_row += 1
            return temp_res

        # elif self.current_coll >= len(self.lst[self.current_row])-1:
        #     # temp_res = self.lst[self.current_row][self.current_coll]
        #     self.current_coll = 0
        #     self.current_row += 1
        #     return self.lst[self.current_row][self.current_coll].data
        else:
            raise StopIteration


test = TableValues(3, 3)
for row in test:
    for value in row:
        print(value)

