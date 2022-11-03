class Singleton:
    firs_obj = None
    base_obj = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls.base_obj is None:
                cls.base = super().__new__(cls)
                return cls.base_obj

            return cls.base_obj

        if cls.firs_obj is None:
            cls.last = super().__new__(cls)
            return cls.firs_obj

        return cls.firs_obj


class Game(Singleton):
    def __init__(self, name: str):
        if 'name' not in self.__dict__:
            self.name = name