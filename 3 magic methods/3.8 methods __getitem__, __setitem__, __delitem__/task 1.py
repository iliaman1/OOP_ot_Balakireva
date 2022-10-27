class Record:
    def __init__(self, **kwargs) -> None:
        self.lst_atributes = []
        for k, v in kwargs.items():
            self.__dict__[k] = v
            self.lst_atributes.append(k)

    def __getitem__(self, item: int) -> getattr:
        if not isinstance(item, int) and item > len(self.lst_atributes):
            raise IndexError('неверный индекс поля')

        return getattr(self, self.lst_atributes[item])

    def __setitem__(self, key: int, value) -> None:
        if not isinstance(key, int) and key > len(self.lst_atributes):
            raise IndexError('неверный индекс поля')

        setattr(self, self.lst_atributes[key], value)
