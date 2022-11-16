input_str = '8 11 abcd -7.5 2.0 -5'
lst_in = input_str.split()


def is_int(input_str: str) -> bool:
    try:
        int(input_str)
        return True
    except:
        return False


print(sum(map(int, list(filter(is_int, lst_in)))))
