from collections import Counter


class NewList:
    def __init__(self, array: list = None) -> None:
        self.array = array if array else []

    def get_list(self) -> list:
        return self.array

    @staticmethod
    def sub_list(list1: list, list2: list) -> list:
        list1_c = list1[:]
        list2_c = list2[:]
        result_poper = []
        for index_list1, value_list1 in enumerate(list1_c):
            count_del = 0
            for index_list2, value_list2 in enumerate(list2_c):
                if type(value_list1) == type(value_list2) and value_list1 == value_list2 and count_del == 0:
                    result_poper.append(index_list1)
                    list2_c.pop(index_list2)
                    count_del += 1

        for i in sorted(result_poper, reverse=True):
            list1_c.pop(i)

        return list1_c

    def __sub__(self, other: (list, object)) -> object:
        if isinstance(other, NewList):
            other = other.get_list()

        return NewList(self.sub_list(self.array, other))

    def __rsub__(self, other: (list, object)) -> object:
        if isinstance(other, NewList):
            other = other.get_list()

        return NewList(self.sub_list(other, self.array))


lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])

assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"

res1 = lst1 - lst2
res2 = lst1 - [0, True]
res3 = [1, 2, 3, 4.5] - lst2
lst1 -= lst2

assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"
