class IteratorAttrs:
    def __iter__(self):
        for item in self.__dict__.items():
            yield item


class SmartPhone(IteratorAttrs):
    def __init__(self, model: str, size: tuple, memory: int):
        self.model = model
        self.size = size
        self.memory = memory
