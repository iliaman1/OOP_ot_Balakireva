def sub_list(list1: list, list2: list) -> list:
    result = []
    for index_list1, value_list1 in enumerate(list1):
        count_del = 0
        for index_list2, value_list2 in enumerate(list2):
            if type(value_list1) == type(value_list2) and value_list1 == value_list2 and count_del == 0:
                result.append(index_list1)
                list2.pop(index_list2)
                count_del += 1
    for i in sorted(result, reverse=True):
        list1.pop(i)
    return list1

print(sub_list([1, 0, True, False, 5.0, True, 1, True, -7.87], [10, True, False, True, 1, 7.87]))
assert sub_list([0, 1, -3.4, "abc", True], [0, True]) == [1, -3.4, "abc"]
assert sub_list([1, 2], [1, 2, 3]) == []
assert sub_list([1, 2, 3], [2, 3]) == [1]
assert sub_list([1, 2, 2], [2, 3]) == [1, 2]
assert sub_list([1, 0, True, False, 5.0, True, 1, True, -7.87], [10, True, False, True, 1, 7.87]) == [0, 5.0, 1, True, -7.87]
