from abc import abstractmethod


class Test:
    def __init__(self, descr: str):
        if len(descr) < 10 or len(descr) > 10000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr

    @abstractmethod
    def run(self):
        raise NotImplementedError('объяви меня, балда')


class TestAnsDigit(Test):
    def __init__(self, descr: str, ans_digit: (int, float), max_error_digit: (int, float) = 0.01):
        super().__init__(descr)
        if type(ans_digit) not in (int, float) or type(max_error_digit) not in (int, float) or max_error_digit < 0:
            raise ValueError('недопустимые значения аргументов теста')

        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def run(self) -> bool:
        ans = float(input())
        if self.ans_digit - self.max_error_digit < ans < self.ans_digit + self.max_error_digit:
            return True

        return False


descr, ans = map(str.strip, input().split('|'))  # for example: What value will be obtained when calculating 2+2? | 4
ans = float(ans)  # here, for simplicity, we assume that ans is exactly a number and there can be no errors in the conversion
try:
    test = TestAnsDigit(descr, ans)
    print(test.run())
except Exception as e:
    print(e)
