class StackObj:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, val):
        self.__next = val


class Stack:
    def __init__(self, top=None):
        self.top = top
        self.tail = None

    def push_back(self, obj):
        if self.top == None:
            self.top = obj

        if self.tail == None:
            self.tail = obj

        if self.top and self.tail:
            self.tail.next = obj
            self.tail = obj

    def pop_back(self):
        current = self.top
        if current == None:
            return

        if current == self.tail:
            self.top = self.tail = None

        while current:
            if current.next == self.tail:
                current.next = None
                self.tail = current
            current = current.next

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for i in other:
            self.push_back(StackObj(i))
        return self


assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"
