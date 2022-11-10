class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    id = 1

    def __init__(self, name: str, weight: (int, float), price: (int, float)):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = ShopItem.id
        ShopItem.id += 1

    def get_id(self):
        return self.__id
