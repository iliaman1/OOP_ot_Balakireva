class RadiusVector:
    def __init__(self, *args: (int, float)) -> None:
        self.coord = list(args)

    def __getitem__(self, item: (int, slice)) -> (int, float, slice):
        if not isinstance(item, (int, slice)):
            raise IndexError('неверный индекс')

        if isinstance(item, int) and item < len(self.coord):
            return self.coord[item]

        if isinstance(item, slice):
            return tuple(self.coord[item])

    def __setitem__(self, key: (int, slice), value: (int, float, list)) -> None:
        if not isinstance(key, (int, slice)):
            raise IndexError('неверный индекс')

        if isinstance(key, int) and key < len(self.coord):
            self.coord[key] = value

        if isinstance(key, slice):
            self.coord[key] = value


v = RadiusVector(1, 1, 1, 1)
print(v[1])  # 1
v[:] = 1, 2, 3, 4
print(v[2])  # 3
print(v[1:])  # (2, 3, 4)
