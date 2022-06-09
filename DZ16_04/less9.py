# pylint: skip-file

# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
#
#
# def binary_search_recursive(some_lst, element, start, end):
#     if start > end:
#         return -1
#
#     mid = (start + end) // 2
#     if element == some_lst[mid]:
#         return f"First invalid version: {some_lst[mid]}"
#
#     if element < some_lst[mid]:
#         return binary_search_recursive(some_lst, element, start, mid - 1)
#     else:
#         return binary_search_recursive(some_lst, element, mid + 1, end)
#
#
# print(binary_search_recursive(lst, 121, 0, len(lst)))
#
#
# import datetime
#
#
# def decor_func(some_function):
#
#     def wrapper(a, b):
#
#         start_time = datetime.datetime.now()
#         result1 = some_function(a, b)
#
#         file = open("result.txt", "a")
#         file.write(f"{some_function.__name__} was called with {a, b} at {start_time} and return result {result1}\n")
#         return result1
#     return wrapper
#
#
# @decor_func
# def kate_function(a, b):
#     return a*b
#
#
# print(kate_function(2, 54))

class Hero:
    def __init__(self):
        self.money = 1222

    def get_money(self):
        return self.__money

    def set_money(self, value):
        if value > 100:
            self.__money = 100
            print(111)
        elif value < 0:
            self.__money = 1
            print(222)
        else:
            self.__money = value
            print(333)

    money = property(get_money, set_money)


me = Hero()

print(me.money)



