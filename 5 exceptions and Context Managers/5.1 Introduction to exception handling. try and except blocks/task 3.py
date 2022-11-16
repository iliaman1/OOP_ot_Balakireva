lst_in = "1 -5.6 True abc 0 23.56 hello".split()


def get_number(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x


lst_out = [get_number(elem) for elem in lst_in]
print(lst_out)
