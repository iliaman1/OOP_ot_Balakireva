class IterColumn:
    def __init__(self, lst: list, column: int) -> None:
        self.lst = lst
        self.column = column

    def __iter__(self):
        self.row = 0
        return self

    def __next__(self):
        if self.row < len(self.lst):
            temp = self.row
            self.row += 1
            return self.lst[temp][self.column]
        else:
            raise StopIteration


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]

it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)
