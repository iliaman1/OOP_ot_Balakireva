class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')

    def __call__(self, data, *args, **kwargs):
        return self._is_valid(data)


class IntegerValidator(Validator):
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data: int) -> bool:
        if type(data) == int and self.max_value >= data >= self.min_value:
            return True
        return False


class FloatValidator(Validator):
    def __init__(self, min_value: (int, float), max_value: (int, float)):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data: float) -> bool:
        if type(data) == float and self.max_value >= data >= self.min_value:
            return True
        return False
