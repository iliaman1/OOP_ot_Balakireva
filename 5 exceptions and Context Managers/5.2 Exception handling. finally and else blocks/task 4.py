class Rect:
    def __init__(self, x: (int, float), y: (int, float), width: (int, float), height: (int, float)):
        if type(x) not in (int, float) or type(y) not in (int, float) or type(width) not in (int, float) or type(
                height) not in (int, float) or width <= 0 or height <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def is_collision(self, rect):
        pass