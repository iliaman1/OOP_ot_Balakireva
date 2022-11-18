class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        cls.lst = lst
        cls.max_length = max_length
        return super().__new__(cls, tuple(lst))

    def __repr__(self):
        return ' '.join(str(i) for i in self.lst)


digits = list(map(float, input().split()))  # эту строчку не менять (коллекцию digits также не менять)

# здесь создавайте объект класса
try:
    test = TupleLimit(digits, 5)
except Exception as e:
    print(e)
else:
    print(test)