from collections import Counter


# def get_counter(items: list) -> dict:
#     result = defaultdict(int)
#
#     for value in items:
#         result[value] += 1
#
#     return dict(result)
# repr()

def sub_list(list1: list, list2: list) -> list:
    result = []
    counter = dict(Counter(list2))
    print(counter)
    for value in list1:
        if counter.get(value):
            counter[value] -= 1
        else:
            result.append(value)

    return result


print(sub_list([0, 1, -3.4, 'abc', True], [0, True]))

assert sub_list([-3.4, 'abc'], [0, True]) == [1, -3.4, "abc"]
assert sub_list([1, 2], [1, 2, 3]) == []
assert sub_list([1, 2, 3], [2, 3]) == [1]
assert sub_list([1, 2, 2], [2, 3]) == [1, 2]
assert sub_list([1, 0, True, False, 5.0, True, 1, True, -7.87], [10, True, False, True, 1, 7.87]) == [0, 5.0, 1, True, -7.87]

# lst = NewList()
# lst1 = NewList([0, 1, -3.4, "abc", True])
# lst2 = NewList([1, 0, True])
#
# assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"
#
# res1 = lst1 - lst2
# res2 = lst1 - [0, True]
# res3 = [1, 2, 3, 4.5] - lst2
# lst1 -= lst2
#
# assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
# assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
# assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
# assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
#
# lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
# lst_2 = NewList([10, True, False, True, 1, 7.87])
# res = lst_1 - lst_2
# assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"
#
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
# assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"
