class Ellipse:
    def __init__(self, *args) -> None:
        if args:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]

    def __bool__(self) -> bool:
        return hasattr(self, 'x1') and hasattr(self, 'y1') and hasattr(self, 'x2') and hasattr(self, 'y2')

    def get_coords(self) -> tuple:
        if bool(self):
            return self.x1, self.y1, self.x2, self.y2
        raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(4, 3, 2, 1)]
for obj in lst_geom:
    if bool(obj):
        obj.get_coords()
