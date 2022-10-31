from typing import Any


class StackObj:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None
        self.prev = None
        self.index = None


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.tail = None
        self.len = 0

    def push_back(self, obj: StackObj) -> None:
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

    def push_front(self, obj: StackObj) -> None:
        if not (self.top and self.tail):
            self.top = obj
            self.tail = obj
            self.tail.index = self.len
            self.len += 1
        else:
            obj.next = self.top
            self.top = obj
            self.top.index = 0
            self.len += 1
            current = self.top.next
            while current:
                current.index += 1
                current = current.next

    def pop(self) -> (StackObj, None):
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

    def __getitem__(self, item: int) -> Any:
        if not isinstance(item, int) or item >= self.len or item < 0:
            raise IndexError('неверный индекс')

        if self.top.index == item:
            return self.top.data
        else:
            obj = self.top
            while obj:
                if obj.index == item:
                    return obj.data

                obj = obj.next

    def __setitem__(self, key: int, value: Any) -> None:
        if not isinstance(key, int) or key >= self.len or key < 0:
            raise IndexError('неверный индекс')

        new = StackObj(value)
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

    def __len__(self) -> int:
        return self.len

    def __iter__(self):
        self.current = self.top
        return self

    def __next__(self) -> StackObj:
        if self.current:
            temp = self.current
            self.current = self.current.next
            return temp
        else:
            raise StopIteration


st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))
print(st[0].data)
