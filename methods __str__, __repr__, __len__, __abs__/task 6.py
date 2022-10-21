from math import sqrt


class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.coords = [0] * args[0]
        else:
            self.coords = list(args)

    def set_coords(self, *args):
        ran = len(self.coords) if len(self.coords) < len(args) else len(args)
        for i in range(ran):
            self.coords[i] = args[i]

    def get_coords(self):
        return tuple(self.coords[:])

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        sum = 0
        for i in self.coords:
            sum += i * i
        return sqrt(sum)


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D)  # res_len = 3
res_abs = abs(vector3D)
print(res_len, res_abs)
