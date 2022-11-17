try:
    a, b = input().split()
    try:
        c = int(a) + int(b)
    except:
        try:
            c = float(a) + float(b)
        except:
            c = str(a) + str(b)
finally:
    print(c)
