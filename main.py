
# Написати декоратор для будь якої функції, що буде зберігати історію викликів функцій у файлі.
# Тобто всі функції що будуть задекоровані цим декоратором
# з кожним викликом мають записути у файл наступний рядок:
# {Function name} was called with args {args & kwargs} at {time} and return result {result}

import datetime


def func_calls(some_func):

    def write_calls(*args, **kwargs):

        start_func_time = datetime.datetime.now()
        result = some_func(*args, **kwargs)

        file = open("DZ_less7_result.txt", "a")
        file.write(str(f"{some_func.__name__} was called with args: {args, kwargs}"
                       f" at {start_func_time} and return result: {result}\n"))

        return result
    return write_calls


@func_calls
def adder_func(a, b, c):
    return a + b + c


@func_calls
def adder_func_2(a, b):
    return (a ** 2) + (b ** 2)


print(adder_func(3, 2, 5))
print(adder_func_2(5, 6))
