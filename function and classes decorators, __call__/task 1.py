from random import randint


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        res = ''
        for i in range(randint(self.min_length, self.max_length)):
            res = res + self.psw_chars[randint(0, len(self.psw_chars)-1)]
        return res


rnd_pass = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
lst_pass = [rnd_pass(), rnd_pass(), rnd_pass()]
print(lst_pass)
