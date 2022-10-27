class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.tail = None

    def push(self, obj):
        if not (self.top and self.tail):
            self.top = obj
            self.tail = obj
        else:
            self.tail.next