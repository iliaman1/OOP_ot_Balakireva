from typing import Any


class Matrix:
    def __init__(self, rows_or_list: (int, list), cols: int = 0, fill_value: (int, float) = 0) -> None:
        if not isinstance(rows_or_list, (int, list)) or not isinstance(cols,int) or not isinstance(fill_value, (int, float)):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

        if isinstance(rows_or_list, list):
            self.rows = len(rows_or_list)
            self.cols = len(rows_or_list[0])
            self.lst = rows_or_list
            if not all(len(r) == self.cols for r in rows_or_list) or \
                    not all(self.is_digit(value) for rows in rows_or_list for value in rows):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
        else:
            self.rows = rows_or_list
            self.cols = cols
            self.lst = [[fill_value]*self.cols for _ in range(self.rows)]

    def __getitem__(self, item: tuple) -> (int, float):
        if not isinstance(item, tuple) or 0 > item[0] > self.rows or 0 > item[1] > self.cols:
            raise IndexError('недопустимые значения индексов')

        return self.lst[item[0]][item[1]]

    def __setitem__(self, key: tuple, value: (int, float)) -> None:
        if not isinstance(key, tuple) or 0 > key[0] > self.rows or 0 > key[1] > self.cols:
            raise IndexError('недопустимые значения индексов')

        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')

        self.lst[key[0]][key[1]] = value

    def __add__(self, other: (int, object)) -> object:
        if type(other) == int:

            return Matrix([[elem + other for elem in row] for row in self.lst])

        else:
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError('операции возможны только с матрицами равных размеров')

            return Matrix([[self.lst[row][col] + other.lst[row][col] for col in range(self.cols)] for row in range(self.rows)])

    def __sub__(self, other: (int, object)) -> object:
        if type(other) == int:

            return Matrix([[elem - other for elem in row] for row in self.lst])

        else:
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError('операции возможны только с матрицами равных размеров')

            return Matrix([[self.lst[row][col] - other.lst[row][col] for col in range(self.cols)] for row in range(self.rows)])

    @staticmethod
    def is_digit(value: Any) -> bool:
        return isinstance(value, (int, float))


mt1 = Matrix([[1, 2], [3, 4]])
mt2 = Matrix([[1, 2], [3, 4]])
res = mt1[0, 0]
print(res)