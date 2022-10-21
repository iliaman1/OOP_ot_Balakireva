class SingletonFive:
    __count = 0
    __last = None

    def __new__(cls, *args, **kwargs):
        if cls.__count < 4:
            cls.__count += 1
            cls.__last = super().__new__(cls)
            return super().__new__(cls)
        return cls.__last

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять

for i in objs:
    print(id(i))
