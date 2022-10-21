class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        if isinstance(other, Item):
            other = other.money

        return self.money + other

    def __radd__(self, other):
        return self.__add__(other)


class Budget:
    def __init__(self):
        self.items_list = []

    def add_item(self, it: Item) -> None:
        self.items_list.append(it)

    def remove_item(self, indx: int) -> None:
        self.items_list.pop(indx)

    def get_items(self) -> list:
        return self.items_list