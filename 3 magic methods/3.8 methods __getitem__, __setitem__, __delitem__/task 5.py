class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.index = None


class Stack:
    def __init__(self):
        self.top = None
        self.tail = None
        self.len = 0

    def push(self, obj):
        if not (self.top and self.tail):
            self.top = obj
            self.tail = obj
            self.tail.index = self.len
            self.len += 1
        else:
            obj.prev = self.tail
            self.tail.next = obj
            self.tail = obj
            self.tail.index = self.len
            self.len += 1

    def pop(self):
        if self.tail == self.top:
            res = self.tail
            self.tail = self.top = None
            self.len = 0

            return res

        elif self.tail == None and self.top == None:

            return None

        else:
            res = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.len -= 1

            return res

    def __getitem__(self, item):
        if not isinstance(item, int) or item >= self.len or item < 0:
            raise IndexError('неверный индекс')

        if self.top.index == item:
            return self.top
        else:
            obj = self.top
            while obj:
                if obj.index == item:
                    return obj

                obj = obj.next

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key >= self.len or key < 0:
            raise IndexError('неверный индекс')

        new = value
        if self.top.index == key:
            new.next = self.top.next
            new.index = self.top.index
            new.prev = self.top.prev
            if self.top.next:
                self.top.next.prev = new
            self.top = new
            return
        elif self.tail.index == key:
            new.next = self.tail.next
            new.index = self.tail.index
            new.prev = self.tail.prev
            self.tail.prev.next = new
            self.tail = new
            return
        else:
            obj = self.top
            while obj:
                if obj.index == key:
                    new.next = obj.next
                    new.index = obj.index
                    new.prev = obj.prev
                    obj.prev.next = new
                    obj.next.prev = new
                    return

                obj = obj.next


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
res = st[3] # исключение IndexError
