class DeltaClock:
    def __init__(self, obj1, obj2):
        self.clock1 = obj1
        self.clock2 = obj2

    def __str__(self):
        res = self.clock1.get_time() - self.clock2.get_time()
        if res < 0:
            return "00: 00: 00"
        else:
            h = res // 3600
            m = (res - h * 3600) // 60
            s = res - (h * 3600 + m * 60)
            return f"{h:02d}: {m:02d}: {s:02d}"

    def __len__(self):

        return self.clock1.get_time() - self.clock2.get_time() if self.clock1.get_time() - self.clock2.get_time() > 0 else 0


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt)


