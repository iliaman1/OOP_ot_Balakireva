class Triangle:
    def __init__(self, a: (int, float), b: (int, float), c: (int, float)):
        if type(a) not in (int, float) or type(b) not in (int, float) or type(c) not in (
                int, float) or a <= 0 or b <= 0 or c <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')

        if a > b + c or b > a + c or c > a + b:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')

        self._a = a
        self._b = b
        self._c = c


def create_trangle(args: tuple) -> Triangle:
    try:
        return Triangle(args[0], args[1], args[2])
    except:
        return


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = [create_trangle(elem) for elem in input_data if create_trangle(elem)]
