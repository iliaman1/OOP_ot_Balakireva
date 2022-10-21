class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    @staticmethod
    def convert(val):
        if type(val) in (float, int):
            return [val, val, val]
        return [val.width, val.height, val.depth]

    def __add__(self, other):
        other = self.convert(other)
        return Box3D(self.width + other[0], self.height + other[1], self.depth + other[2])

    def __mul__(self, other):
        other = self.convert(other)
        return Box3D(self.width * other[0], self.height * other[1], self.depth * other[2])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        other = self.convert(other)
        return Box3D(self.width - other[0], self.height - other[1], self.depth - other[2])

    def __floordiv__(self, other):
        other = self.convert(other)
        return Box3D(self.width // other[0], self.height // other[1], self.depth // other[2])

    def __mod__(self, other):
        other = self.convert(other)
        return Box3D(self.width % other[0], self.height % other[1], self.depth % other[2])


box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
box = 3 * box2    # Box3D: width=6, height=12, depth=18
box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
box = box2 % 3    # Box3D: width=2, height=1, depth=0