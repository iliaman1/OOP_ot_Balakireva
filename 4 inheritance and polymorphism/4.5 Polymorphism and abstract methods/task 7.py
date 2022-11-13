class Track:
    def __init__(self, *args):
        if type(args[0]) in (int, float):
            self.start = PointTrack(args[0], args[1])
            self.__points = [self.start]
        else:
            self.__points = [point for point in args]

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)


class PointTrack:
    def __init__(self, x: (int, float), y: (int, float)):
        if type(x) not in (int, float) or type(y) not in (int, float):
            raise TypeError('координаты должны быть числами')

        self.x = x
        self.y = y

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"
