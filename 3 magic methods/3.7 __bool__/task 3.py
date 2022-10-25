from math import sqrt


class Line:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self) -> int:
        return int(sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2))

    def __bool__(self) -> bool:
        return len(self) >= 1
