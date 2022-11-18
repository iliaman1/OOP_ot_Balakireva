class ValidatorString:
    def __init__(self, min_length: int, max_length: int, chars: str):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, text: str):
        if len(text) < self.min_length or len(text) > self.max_length:
            raise ValueError('недопустимая строка')

        if self.chars:
            flag = 0
            for char in self.chars:
                if char in text:
                    flag += 1
            if flag == 0:
                raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, login_validator: ValidatorString, password_validator: ValidatorString):
        self.login_validator = login_validator
        self.password_validator = password_validator

    def form(self, request: dict):
        if 'login' not in request or 'password' not in request:
            raise TypeError('в запросе отсутствует логин или пароль')

        self.login_validator.is_valid(request['login'])
        self.password_validator.is_valid(request['password'])
        self._login = request['login']
        self._password = request['password']


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
