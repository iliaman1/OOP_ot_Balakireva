class Point:
    def __init__(self, x: (int, float) = 0, y: (int, float) = 0):
        self._x = x
        self._y = y


try:
    a, b = input().split()
    try:
        pt = Point(int(a), int(b))
    except:
        try:
            pt = Point(float(a), float(b))
        except:
            pt = Point()
finally:
    print(f"Point: x = {pt._x}, y = {pt._y}")
