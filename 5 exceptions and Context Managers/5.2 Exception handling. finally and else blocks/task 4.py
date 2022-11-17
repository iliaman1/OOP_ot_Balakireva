class Rect:
    def __init__(self, x: (int, float), y: (int, float), width: (int, float), height: (int, float)):
        if type(x) not in (int, float) or type(y) not in (int, float) or type(width) not in (int, float) or type(
                height) not in (int, float) or width <= 0 or height <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise ValueError('некорректные координаты и параметры прямоугольника')

        if key in ('_width', '_height') and value <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')

        object.__setattr__(self, key, value)

    def is_collision(self, rect):
        if not isinstance(rect, Rect):
            raise TypeError

        if not (self._x + self._width < rect._x or rect._x + rect._width < self._x or self._y + self._height < self._y
                or rect._y + rect._height < self._y):
            raise TypeError('прямоугольники пересекаются')


def is_collision(r1, r2):
    try:
        r1.is_collision(r2)
    except:
        return True
    return False


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_not_collision = [lst_rect[i] for i in range(len(lst_rect)) if
                     not any(is_collision(lst_rect[i], lst_rect[j]) for j in range(len(lst_rect)) if i != j)]
