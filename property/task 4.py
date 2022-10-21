class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.validate(x):
            self.__x = x
        if self.validate(y):
            self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if self.validate(val):
            self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if self.validate(val):
            self.__y = val

    @classmethod
    def validate(cls, val):
        return type(val) in (int, float) and cls.MIN_COORD <= val <= cls.MAX_COORD


    @staticmethod
    def norm2(obj):
        return obj.x * obj.x + obj.y *obj.y


r1 = RadiusVector2D()
r2 = RadiusVector2D(1)
r3 = RadiusVector2D(4, 5)

print(r1.x, r1.y)
print(r2.x, r2.y)
print(r3.x, r3.y)
print(RadiusVector2D.norm2(r1))