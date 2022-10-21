import re
from string import ascii_lowercase, digits


class CardCheck:
    @staticmethod
    def check_card_number(number):
        if re.fullmatch(r'\d{4}-\d{4}-\d{4}-\d{4}', number):
            return True
        return False

    @staticmethod
    def check_name(name):
        if re.fullmatch(r'[A-Z]+\s[A-Z]+', name):
            return True
        return False


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_name)