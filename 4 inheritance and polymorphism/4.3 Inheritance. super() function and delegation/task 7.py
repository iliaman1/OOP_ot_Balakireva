class StringDigit(str):
    def __init__(self, string: str):
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")

        super().__init__()

    def __add__(self, other: str):
        return StringDigit(super().__add__(other))

    def __radd__(self, other: str):
        return StringDigit(other + super().__add__(''))
