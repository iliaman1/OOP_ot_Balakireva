class Translator:
    d = {}

    def add(self, eng, rus):
        if eng not in self.d:
            self.d[eng] = [rus]
        elif eng in self.d and rus not in self.d[eng]:
            self.d[eng].append(rus)
        else:
            pass

    def remove(self, eng):
        del self.d[eng]

    def translate(self, eng):
        return self.d[eng]


tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')
print(*tr.translate('go'))
print(tr.translate('car'))
tr.remove('car')
