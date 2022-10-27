class Integer:
    def __init__(self, start_value: int = 0) -> None:
        if not isinstance(start_value, int):
            raise ValueError('должно быть целое число')
        self.start_value = start_value
        self.__value = start_value

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, val: int) -> None:
        if not isinstance(val, int):
            raise ValueError('должно быть целое число')

        self.__value = val


class Array:
    def __init__(self, max_length: int, cell: object) -> None:
        self.max_length = max_length
        self.cell = cell
        self.array = [cell() for _ in range(max_length)]

    def __str__(self) -> str:
        return ' '.join(str(v.value) for v in self.array)

    def __getitem__(self, item: int) -> int:
        if item >= self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')

        return self.array[item].value

    def __setitem__(self, key: int, value: int) -> None:
        if key >= self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')

        self.array[key].value = value


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
# ar_int[1] = 10.5 # должно генерироваться исключение ValueError
ar_int[10] = 1  # должно генерироваться исключение IndexError
