lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
    'Pythone; Балакиревa С.М.; 2021'
]


class BookStudy:
    def __init__(self, name: str, author: str, year: int) -> None:
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self) -> hash:
        return hash((self.name.lower(), self.author.lower()))


lst_bs = [BookStudy(row.split('; ')[0], row.split('; ')[1], int(row.split('; ')[2])) for row in lst_in]
unique_books = len({hash(k): 1 for k in lst_bs})
