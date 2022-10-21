class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        if a < len(self.lst_data) and b >= a and b <= len(self.lst_data):
            return self.lst_data[a:b + 1]
        elif b > len(self.lst_data):
            return self.lst_data[a:]
        else:
            return self.lst_data[a]

    def insert(self, lst):
        for i in lst:
            self.lst_data.append(
                {'id': int(i.split()[0]), 'name': i.split()[1], 'old': int(i.split()[2]), 'salary': int(i.split()[3])})

lst = ['1 serg 55 1000', '2 semen 20 10123', '3 pop 123 33333']
test = DataBase()
test.insert(lst)
print(test.select(1,50))