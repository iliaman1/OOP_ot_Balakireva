class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        for i, j in zip(fields, lst_values):
            try:
                setattr(self, i, j)
            except:
                return False
        return True


test = StreamData()
test.create(['name', 'age'], ['ilia', 10])
print(test.__dict__)
