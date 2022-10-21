def clock(time):
    h = time // 3600
    m = (time - h * 3600) // 60
    s = time - (h * 3600 + m * 60)
    return f"{h:02d}: {m:02d}: {s:02d}"

print(clock(3600))