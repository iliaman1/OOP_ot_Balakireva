class SuperShop:
    def __init__(self, name, goods=[]):
        self.name = name
        self.goods = goods

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, prod):
        self.goods.remove(prod)


class StringValue:
    def __init__(self, max=50, min=2):
        self.min_length = min
        self.max_length = max

    def validate(self, s):
        if type(s) == str and self.min_length <= len(s) <= self.max_length:
            return True
        return False

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validate(value):
            instance.__dict__[self.name] = value


class PriceValue:
    def __init__(self, max=10000):
        self.max_value = max

    def validate(self, price):
        if type(price) in (int, float) and 0 <= price <= self.max_value:
            return True
        return False

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validate(value):
            instance.__dict__[self.name] = value


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")