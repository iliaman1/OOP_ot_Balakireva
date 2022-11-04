from typing import Any


class Validator:
    def is_valid(self, data: Any) -> bool:
        return True

    def __call__(self, data: Any, *args, **kwargs) -> bool:
        return self.is_valid(data)


class IntegerValidator(Validator):
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def is_valid(self, data: Any) -> bool:
        if type(data) == int and self.max_value >= data >= self.min_value:
            return True
        raise ValueError('данные не прошли валидацию')


class FloatValidator(Validator):
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def is_valid(self, data: Any) -> bool:
        if type(data) == float and self.max_value >= data >= self.min_value:
            return True
        raise ValueError('данные не прошли валидацию')
