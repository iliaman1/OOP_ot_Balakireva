from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return 'Базовый класс Model'


class ModelForm(Model):
    counter_id = 0

    def __init__(self, login: str, password: str):
        self._login = login
        self._password = password
        self.__class__.counter_id += 1
        self._id = self.__class__.counter_id

    def get_pk(self):
        return self._id
