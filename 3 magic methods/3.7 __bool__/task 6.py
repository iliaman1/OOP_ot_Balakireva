class Vector:
    def __init__(self, *args: (int, float)) -> None:
        self.lst_coords = list(args)

    def __len__(self):
        return len(self.lst_coords)

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                other = other.lst_coords
                return Vector(*[self.lst_coords[i] + other[i] for i in range(len(self))])

            else:
                raise ArithmeticError('размерности векторов не совпадают')

        return Vector(*[self.lst_coords[i] + other for i in range(len(self))])

    def __sub__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                other = other.lst_coords
                return Vector(*[self.lst_coords[i] - other[i] for i in range(len(self))])

            else:
                raise ArithmeticError('размерности векторов не совпадают')

        return Vector(*[self.lst_coords[i] - other for i in range(len(self))])

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                other = other.lst_coords
                return Vector(*[self.lst_coords[i] * other[i] for i in range(len(self))])

            else:
                raise ArithmeticError('размерности векторов не совпадают')

        return Vector(*[self.lst_coords[i] * other for i in range(len(self))])

    def __iadd__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                other = other.lst_coords
                for i in range(len(self)):
                    self.lst_coords[i] += other[i]

                return self

            else:
                raise ArithmeticError('размерности векторов не совпадают')

        for i in range(len(self)):
            self.lst_coords[i] += other

        return self

    def __isub__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                other = other.lst_coords
                for i in range(len(self)):
                    self.lst_coords[i] -= other[i]

                return self

            else:
                raise ArithmeticError('размерности векторов не совпадают')

        for i in range(len(self)):
            self.lst_coords[i] -= other

        return self

    def __imul__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                other = other.lst_coords
                for i in range(len(self)):
                    self.lst_coords[i] *= other[i]

                return self

            else:
                raise ArithmeticError('размерности векторов не совпадают')

        for i in range(len(self)):
            self.lst_coords[i] *= other

        return self

    def __eq__(self, other):
        return self.lst_coords == other.lst_coords