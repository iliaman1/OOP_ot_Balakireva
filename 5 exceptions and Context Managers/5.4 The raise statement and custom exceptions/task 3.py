class DateError(Exception):
    pass


class DateString:
    def __init__(self, date: str):
        if self.is_date(date):
            self.date = f"{int(date.split('.')[0]):02d}.{int(date.split('.')[1]):02d}.{int(date.split('.')[2]):04d}"

    def __str__(self):
        return self.date

    @staticmethod
    def is_date(value: str) -> bool:
        if len(value := value.split('.')) == 3:
            for index in range(3):
                try:
                    value[index] = int(value[index])
                except:
                    raise DateError
            if 0 < value[0] < 31 and 0 < value[1] < 13 and 0 < value[2] < 3000:
                return True
        return False


date_string = '1.2.1812'
try:
    test = DateString(date_string)
    print(test)
except:
    print('Неверный формат даты')
