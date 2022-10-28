class Thing:
    def __init__(self, name: str, weight: (int, float)) -> None:
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight: (int, float)) -> None:
        self.max_weight = max_weight
        self.list_of_items = []
        self.current_weight = 0

    def add_thing(self, thing: Thing) -> None:
        if not isinstance(thing, Thing):
            raise TypeError('В сумку можно добавлять только тип Thing')

        if thing.weight + self.current_weight <= self.max_weight:
            self.list_of_items.append(thing)
            self.current_weight += thing.weight
        else:
            raise ValueError('превышен суммарный вес предметов')

    def __getitem__(self, item: int) -> Thing:
        if not isinstance(item, int) or item > len(self.list_of_items):
            raise IndexError('неверный индекс')

        return self.list_of_items[item]

    def __setitem__(self, key: int, value: Thing) -> None:
        if not isinstance(key, int) or key > len(self.list_of_items):
            raise IndexError('неверный индекс')

        if self.current_weight - self.list_of_items[key].weight + value.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        else:
            self.current_weight = self.current_weight - self.list_of_items[key].weight + value.weight
            self.list_of_items[key] = value

    def __delitem__(self, key: int) -> None:
        if not isinstance(key, int) or key > len(self.list_of_items):
            raise IndexError('неверный индекс')

        self.current_weight -= self.list_of_items[key].weight
        del self.list_of_items[key]


bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
bag.add_thing(Thing('ножницы', 300))  # генерируется исключение ValueError
print(bag[2].name)  # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name)  # платок
del bag[0]
print(bag[0].name)  # платок
t = bag[4]  # генерируется исключение IndexError
