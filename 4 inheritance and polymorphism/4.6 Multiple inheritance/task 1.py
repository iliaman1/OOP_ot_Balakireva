class Digit:
    def __init__(self, val: (int, float)):
        if type(val) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')

        self.value = val


class Integer(Digit):
    def __init__(self, val: int):
        if type(val) != int:
            raise TypeError('значение не соответствует типу объекта')

        super().__init__(val)


class Float(Digit):
    def __init__(self, val: float):
        if type(val) != float:
            raise TypeError('значение не соответствует типу объекта')

        super().__init__(val)


class Positive(Digit):
    def __init__(self, val: (int, float)):
        if val < 0:
            raise TypeError('значение не соответствует типу объекта')

        super().__init__(val)


class Negative(Digit):
    def __init__(self, val: (int, float)):
        if val > 0:
            raise TypeError('значение не соответствует типу объекта')

        super().__init__(val)


class PrimeNumber(Integer, Positive):
    def __init__(self, val: int):
        super().__init__(val)


class FloatPositive(Float, Positive):
    def __init__(self, val: float):
        super().__init__(val)


digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]
lst_positive = [elem for elem in digits if isinstance(elem, Positive)]
lst_float = [elem for elem in digits if isinstance(elem, Float)]
