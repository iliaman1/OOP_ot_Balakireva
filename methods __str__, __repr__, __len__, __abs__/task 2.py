class Model:
    def __init__(self):
        self.flag = 0

    def query(self, **args):
        self.q = args
        self.res = [f"{i[0]} = {i[1]}" for i in self.q.items()]
        self.flag = 1

    def __str__(self):
        if self.flag == 1:
            return f"Model: {', '.join(self.res)}"
        return 'Model'


model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)
