class Bag:
    def __init__(self, max=0):
        self.max_weight = max
        self.__things = []

    def add_thing(self, thing):
        if self.get_total_weight() + thing.weight <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        self.__things.pop(indx)

    def get_total_weight(self):
        res = 0
        for i in self.things:
            res += i.weight
        return res
    
    @property
    def things(self):
        return self.__things


class Thing:
    def __init__(self, name, weight):
        self.name = name
        if type(weight) in (int, float):
            self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")
