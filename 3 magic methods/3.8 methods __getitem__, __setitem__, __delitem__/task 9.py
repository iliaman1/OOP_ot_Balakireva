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
        if not isinstance(row, int) or not isinstance(col, int) or row < 0 or :
            pass


    def remove_data(self, row: int, col: int) -> None:
        pass
