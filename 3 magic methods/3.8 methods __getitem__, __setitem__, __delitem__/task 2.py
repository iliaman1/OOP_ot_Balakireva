class Track:
    def __init__(self, start_x: (int, float), start_y: (int, float)):
        self.start_x = start_x
        self.start_y = start_y
        self.list_coords = []

    def add_point(self, x: (int, float), y: (int, float), speed: (int, float)):
        self.list_coords.append([(x, y), speed])

    def __getitem__(self, item: int) -> (tuple, int):
        if not isinstance(item, int) and item > len(self.list_coords):
            raise IndexError('некорректный индекс')

        return self.list_coords[item][0], self.list_coords[item][1]

    def __setitem__(self, key: int, value: int):
        if not isinstance(key, int) and key > len(self.list_coords):
            raise IndexError('некорректный индекс')

        self.list_coords[key][1] = value