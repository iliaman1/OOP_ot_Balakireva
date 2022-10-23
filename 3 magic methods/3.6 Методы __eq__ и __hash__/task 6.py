from math import sqrt


class TriangleValue:
    def validate(self, value):
        if type(value) in (int, float) and 0 < value:
            return True
        raise ValueError("длины сторон треугольника должны быть положительными числами")

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validate(value):
            instance.__dict__[self.name] = value


class Triangle:
    a = TriangleValue()
    b = TriangleValue()
    c = TriangleValue()

    def __init__(self, a, b, c):
        if a < b + c and b < a + c and c < a + b:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        p = len(self) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
