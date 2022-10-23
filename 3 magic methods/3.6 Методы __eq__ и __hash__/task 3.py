class Record:
    pk = 1

    def __init__(self, fio: str, descr: str, old: int) -> None:
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = self.pk
        Record.pk += 1

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other: object):
        return hash(self) == hash(other)


class DataBase:
    def __init__(self, path: str) -> None:
        self.path = path
        self.dict_db = {}

    def write(self, record: Record) -> None:
        if record in self.dict_db:
            self.dict_db[record] += [record]
        else:
            self.dict_db[record] = [record]

    def read(self, pk: int) -> Record:
        for object_list in self.dict_db.values():
            for item in object_list:
                if item.pk == pk:
                    return item


lst_in = ['Балакирев С.М.; программист; 33',
          'Кузнецов Н.И.; разведчик-нелегал; 35',
          'Суворов А.В.; полководец; 42',
          'Иванов И.И.; фигурант всех подобных списков; 26',
          'Балакирев С.М.; преподаватель; 33'
          ]
db = DataBase('c?/')

for i in lst_in:
    temp_list = i.split('; ')
    temp_object = Record(temp_list[0], temp_list[1], int(temp_list[2]))
    db.write(temp_object)
