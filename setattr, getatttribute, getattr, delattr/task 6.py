class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, val):
        self.__radius = val

    def __setattr__(self, key, value):
        if key == '_Circle__x' and type(value) in (int, float):
            object.__setattr__(self, key, value)
        elif key == '_Circle__y' and type(value) in (int, float):
            object.__setattr__(self, key, value)
        elif key == '_Circle__radius' and type(value) in (int, float) and value > 0:
            object.__setattr__(self, key, value)
        elif type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            return

    def __getattr__(self, item):
        return False


circle = Circle(10.5, 7, 22)
print(circle.__dict__)
print(circle.radius)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует
print(circle.radius)
print(res)


