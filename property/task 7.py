class PhoneBook:
    def __init__(self):
        self.phone_l = []

    def add_phone(self, phone):
        self.phone_l.append(phone)

    def remove_phone(self, indx):
        self.phone_l.pop(indx)

    def get_phone_list(self):
        return self.phone_l


class PhoneNumber:
    def __init__(self, number, name):
        self.number = number
        self.fio = name


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)
