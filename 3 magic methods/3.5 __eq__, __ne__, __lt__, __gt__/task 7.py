class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume
        self.m = self.ro * self.volume

    def __gt__(self, other):
        if isinstance(other, Body):
            other = other.m

        return self.m > other

    def __lt__(self, other):
        if isinstance(other, Body):
            other = other.m

        return self.m < other

    def __eq__(self, other):
        if isinstance(other, Body):
            other = other.m

        return self.m == other