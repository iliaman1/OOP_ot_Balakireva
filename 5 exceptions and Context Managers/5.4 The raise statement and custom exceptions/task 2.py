class PrimaryKeyError(Exception):
    def __init__(self, message=None, pk=None, id=None):
        if not all([message, pk, id]):
            self.message = 'Первичный ключ должен быть целым неотрицательным числом'

        if id:
            self.message = f"Значение первичного ключа id = {id} недопустимо"

        if pk:
            self.message = f"Значение первичного ключа pk = {pk} недопустимо"

    def __str__(self):
        return self.message


print(PrimaryKeyError(id=-10.5))
