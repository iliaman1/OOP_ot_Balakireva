from math import sqrt


class PathLines:
    def __init__(self, *args):
        self.path = [LineTo()] + list(args)

    def get_path(self):
        if len(self.path) < 2:
            return []
        return self.path

    def get_length(self):
        res = 0
        for i in range(len(self.path) - 1):
            res += sqrt((self.path[i + 1].x - self.path[i].x) ** 2 + (self.path[i + 1].y - self.path[i].y) ** 2)
        return res

    def add_line(self, line):
        self.path.append(line)


class LineTo:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
print(dist)