class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new):
        if 2 <= len(new) <= 100:
            self.__model = new

