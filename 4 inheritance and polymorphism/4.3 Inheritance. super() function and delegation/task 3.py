class SellItem:
    def __init__(self, name: str, price: (int, float)):
        self.name = name
        self.price = price


class House(SellItem):
    def __init__(self, name: str, price: (int, float), material: str, square: (int, float)):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name: str, price: (int, float), size: float, rooms: int):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    def __init__(self, name: str, price: (int, float), square: (int, float)):
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_object(self, product: SellItem):
        self.products.append(product)

    def remove_object(self, product: SellItem):
        self.products.remove(product)

    def get_objects(self) -> list:
        return self.products
