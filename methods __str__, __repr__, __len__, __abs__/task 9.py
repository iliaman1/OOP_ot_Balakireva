class PolyLine:
    def __init__(self, *args):
        self.start_coord = args[0]
        self.list = list(args[:])

    def add_coord(self, x, y):
        self.list.append((x, y))

    def remove_coord(self, indx):
        self.list.pop(indx)

    def get_coords(self):
        return self.list