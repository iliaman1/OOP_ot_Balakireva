import re

stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]

for i in range(len(stich)):
    stich[i] = re.sub("[–|?|!|,|.|;]", "", stich[i])

for i in range(len(stich)):
    while '  ' in stich[i]:
        stich[i] = stich[i].replace('  ', ' ')

for i in range(len(stich)):
    stich[i] = stich[i].split()


class StringText:
    def __init__(self, list_words):
        self.list_words = list_words

    def __len__(self):
        return len(self.list_words)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)


st1 = StringText(stich[0])
st2 = StringText(stich[1])
st3 = StringText(stich[2])
st4 = StringText(stich[3])
st5 = StringText(stich[4])
st6 = StringText(stich[5])
st7 = StringText(stich[6])
lst_text = [st1, st2, st3, st4, st5, st6, st7]
lst_text_sorted = sorted(lst_text, key=lambda x: len(x), reverse=True)
lst_text_sorted = [' '.join(i.list_words) for i in lst_text_sorted]
