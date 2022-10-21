class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if type(self.a) not in (float, int) or type(self.b) not in (float, int) or type(self.c) not in (
                float, int) or self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 1

        elif self.a + self.b > self.c and self.c + self.b > self.a and self.a + self.c > self.b:
            return 3

        else:
            return 2
        

a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
