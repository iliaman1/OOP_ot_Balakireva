class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls


class Money:
    type_money = None

    def __init__(self, volume: (int, float) = 0, cb: CentralBank = None):
        self.__volume = volume
        self.__cb = cb

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, val):
        self.__cb = val

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, val):
        self.__volume = val

    def validate_volumes(self, other):
        if self.cb is None:
            raise ValueError('Неизвестен курс валют.')

        if self.type_money is None:
            raise ValueError('Неизвестен тип кошелька.')

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = other.volume / other.cb.rates[other.type_money]
        return v1, v2

    def __eq__(self, other):
        v1, v2 = self.validate_volumes(other)
        return abs(v1 - v2) < 0.1

    def __lt__(self, other):
        v1, v2 = self.validate_volumes(other)
        return v1 < v2

    def __le__(self, other):
        v1, v2 = self.validate_volumes(other)
        return v1 <= v2


class MoneyR(Money):
    type_money = 'rub'


class MoneyD(Money):
    type_money = 'dollar'


class MoneyE(Money):
    type_money = 'euro'
