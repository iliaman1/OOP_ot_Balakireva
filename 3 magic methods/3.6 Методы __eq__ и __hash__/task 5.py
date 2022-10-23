class Dimensions:
    def __init__(self, a: (int, float), b: (int, float), c: (int, float)) -> None:
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self) -> hash:
        return hash((self.a, self.b, self.c))


s_inp = '1 2 3; 4 5 6.78; 1 2 3; 1 1 2.5'
lst_inp = s_inp.split('; ')
lst_dims = [Dimensions(float(i.split()[0]), float(i.split()[1]), float(i.split()[2])) for i in lst_inp]
lst_dims.sort(key=lambda x: hash(x))
