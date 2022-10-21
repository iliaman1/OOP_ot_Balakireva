class ValidateString:
    def __init__(self, min=3, max=100):
        self.min_length = min
        self.max_length = max

    def validate(self, s):
        if type(s) == str and self.min_length <= len(s) <= self.max_length:
            return True
        return False


class StringValue:
    def __init__(self, validator=ValidateString()):
        self.valid = validator

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.valid.validate(value):
            instance.__dict__[self.name] = value


class RegisterForm:
    login = StringValue()
    password = StringValue()
    email = StringValue()

    def __init__(self, login, psw, email):
        self.login = login
        self.password = psw
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        return f"""<form>
        Логин: <login>
        Пароль: <password>
        Email: <email>
        </form>
        """

