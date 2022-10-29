class Person:
    def __init__(self, fio: str, job: str, old: int, salary: (int, float), year_job: int) -> None:
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.lst = [self.fio, self.job, self.old, self.salary, self.year_job]

    def __getitem__(self, item: int) -> (str, float, int):
        if type(item) != int or 0 > item > 4:
            raise IndexError('неверный индекс')

        return self.lst[item]

    def __setitem__(self, key: int, value: (str, float, int)) -> None:
        if type(key) != int or 0 > key > 4:
            raise IndexError('неверный индекс')

        self.lst[key] = value

    def __iter__(self):
        self.value = -1

        return self

    def __next__(self):
        if self.value < 4:
            self.value += 1
            return self.lst[self.value]
        else:
            raise StopIteration


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError