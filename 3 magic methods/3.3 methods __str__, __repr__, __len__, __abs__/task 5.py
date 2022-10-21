from math import sqrt


class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, val):
        self.__real = val

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, val):
        self.__img = val

    def __setattr__(self, key, value):
        if key == f'_{self.__class__.__name__}__real' and type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
        elif key == f'_{self.__class__.__name__}__img' and type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
        else:
            object.__setattr__(self, key, value)

    def __abs__(self):
        return sqrt(self.__real * self.__real + self.img * self.__img)


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(abs(cmp))
