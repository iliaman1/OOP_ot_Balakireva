class Descript:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    # def __set__(self, instance, value):
    #     return setattr(instance, self.name, value)


class Test:
    x = Descript()

    def __init__(self, x):
        self.x = x

    def setter(self, value):
        self.__x = value


res = Test()
print(res.__dict__)
res.setter(15)
print(res.__dict__)
