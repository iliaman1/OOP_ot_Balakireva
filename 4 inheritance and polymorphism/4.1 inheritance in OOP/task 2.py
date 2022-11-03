class Thing:
    id = 1

    def __init__(self, name: str, price: float, weight: float = None,
                 dims: tuple = None, memory: int = None, frm: str = None):
        self.id = self.id
        Thing.id += 1
        self.name = name
        self.price = price
        self.weight = weight
        self.dims = dims
        self.memory = memory
        self.frm = frm

    def get_data(self) -> tuple:
        return (self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm)


class Table(Thing):
    def __init__(self, name: str, price: float, weight: float, dims: tuple):
        super().__init__(name, price, weight, dims)


class ElBook(Thing):
    def __init__(self, name: str, price: float, memory: int, frm: str):
        super().__init__(name, price, memory=memory, frm=frm)


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(table.__dict__)
print(book.__dict__)
