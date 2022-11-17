from typing import Any


def input_int_numbers():
    res = ['0']
    try:
        res = list(map(int, input().split()))
    except:
        raise TypeError('все числа должны быть целыми')
    finally:
        return res


def is_int(value: Any) -> bool:
    if type(value) == int:
        return True
    return False


while True:
    result = input_int_numbers()
    if all(is_int(item) for item in result):
        print(*result)
        break
