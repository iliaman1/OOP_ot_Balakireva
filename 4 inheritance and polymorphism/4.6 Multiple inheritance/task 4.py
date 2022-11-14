class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    # здесь объявляйте еще один метод
    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)


# здесь объявляйте класс Money
class Money:
    def __init__(self, count: (int, float)):
        if type(count) not in (int, float):
            raise TypeError('сумма должна быть числом')

        self._money = count

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        if type(value) not in (int, float):
            raise TypeError('сумма должна быть числом')

        self._money = value


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"
