from typing import Any

from abc import ABC, abstractmethod


class StackObj:
    def __init__(self, data: Any):
        self._data = data
        self._next = None


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def push_back(self, obj: StackObj):
        if self._top is None:
            self._top = obj

        else:
            temp = self._top
            while temp:
                if temp._next is None:
                    temp._next = obj
                    break

                temp = temp._next

    def pop_back(self) -> StackObj or None:
        if self._top is None:
            return None

        if self._top._next is None:
            res = self._top
            self._top = None
            return res

        temp = self._top
        while temp:
            if temp._next._next is None:
                res = temp._next
                temp._next = None
                return res

            temp = temp._next
