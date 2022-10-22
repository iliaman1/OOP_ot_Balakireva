class Box:
    def __init__(self):
        self.box_list = []

    def add_thing(self, obj):
        self.box_list.append(obj)

    def get_things(self):
        return self.box_list

    def __eq__(self, other):
        dict_self = {i.name.lower(): i.mass for i in self.box_list}
        dict_other = {i.name.lower(): i.mass for i in other.box_list}
        return dict_self == dict_other


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass
