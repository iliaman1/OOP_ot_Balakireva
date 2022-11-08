class ItemAttrs:
    def __init__(self):
        self.lst_attr = [value for value in self.__dict__.keys()]

    def __getitem__(self, item):
        return getattr(self, self.lst_attr[item])

    def __setitem__(self, key, value):
        setattr(self, self.lst_attr[key], value)


class Point(ItemAttrs):
    def __init__(self, x: (int, float), y: (int, float)):
        self.x = x
        self.y = y
        super().__init__()
