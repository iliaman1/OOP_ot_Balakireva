class FloatValidator:
    def __init__(self, min_value: float, max_value: float):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, val, *args, **kwargs):
        if type(val) != float or val < self.min_value or val > self.max_value:
            raise ValueError('значение не прошло валидацию')

        return val


class IntegerValidator:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, val, *args, **kwargs):
        if type(val) != int or val < self.min_value or val > self.max_value:
            raise ValueError('значение не прошло валидацию')

        return True


def is_valid(lst: list, validators: list) -> list:
    res_lst = []
    for item in lst:
        for validator in validators:
            try:
                if validator(item):
                    res_lst.append(item)
                    break
            except:
                continue

    return res_lst
