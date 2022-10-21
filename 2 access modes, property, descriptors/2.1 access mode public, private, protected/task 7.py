from random import randint


class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.'
        return ''.join([chars[randint(0, len(chars)-1)] for _ in range(10)]) + '@gmail.com'

    @classmethod
    def check_email(cls, email):
        chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@._")
        if cls.__is_email_str(email):
            if set(email) <= chars:
                if len(email[:email.index('@')]) <= 100:
                    if len(email[email.index('@'):]) <= 50:
                        if '.' in email[email.index('@'):]:
                            if '..' not in email:
                                return True
        return False

    @staticmethod
    def __is_email_str(email):
        if type(email) == str:
            return True
        return False


print(EmailValidator.check_email("sc_lib@list.ru"))  # True
print(EmailValidator.check_email("sc_lib@list_ru"))  # False
