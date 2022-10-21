class StackObj:
    def __init__(self, data,):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, val):
        if isinstance(val, StackObj) or val is None:
            self.__next = val

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, val):
        self.__data = val


class Stack:
    def __init__(self):
        self.top = None
        self.current = None

    def push(self, obj):
        if self.current:
            self.current.next = obj
        self.current = obj
        if self.top is None:
            self.top = obj

    def pop(self):
        h = self.top
        if h is None:
            return
        while h and h.next != self.current:
            h = h.next
        if h:
            h.next = None
        res = self.current
        self.current = h
        if self.current is None:
            self.top = None
        return res

    def get_data(self):
        h = self.top
        res = []
        while h:
            res.append(h.data)
            h = h.next
        return res

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))

print(st.pop().data)
print(st.pop().data)
print(st.pop().data)
print(st.get_data())

