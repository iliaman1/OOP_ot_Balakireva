class Tuple(tuple):
    def __add__(self, other):
        other = tuple(other)

        return Tuple(super().__add__(other))
