from typing import Any


class Cell:
    def __init__(self, value: Any) -> None:
        self.value = value


class SparseTable:
    def __init__(self, rows: int = 0, cols: int = 0) -> None:
        self.rows = rows
        self.cols = cols
        self.dict_table = {}

    def add_data(self, row: int, col: int, data: Cell) -> None:
        if not isinstance(row, int) or not isinstance(col, int) or row < 0 or col < 0:
            raise ValueError("Значение строки/столбца должно быть целым неотрицательным числом")

        if row + 1 > self.rows:
            self.rows = row + 1
        if col + 1 > self.cols:
            self.cols = col + 1

        self.dict_table[(row, col)] = data

    def remove_data(self, row: int, col: int) -> None:
        if (row, col) not in self.dict_table:
            raise IndexError('ячейка с указанными индексами не существует')
        del self.dict_table[(row, col)]

        max_row = 0
        max_col = 0
        for key in self.dict_table:
            if key[0] > max_row:
                max_row = key[0]
            if key[1] > max_col:
                max_col = key[1]
        self.rows = max_row + 1
        self.cols = max_col + 1

    def __getitem__(self, item: tuple) -> Cell:
        if item not in self.dict_table:
            raise ValueError('данные по указанным индексам отсутствуют')

        return self.dict_table[item]

    def __setitem__(self, key: tuple, value: Any) -> None:
        if key not in self.dict_table:
            self.add_data(key[0], key[1], value)
        else:
            self.dict_table[key] = value


st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
val = st[2, 5] # ValueError
st.remove_data(12, 3) # IndexError