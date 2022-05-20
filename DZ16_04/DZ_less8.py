# pylint: skip-file

# 1. Поиск первой неисправной версии проэкта. Есть список версий, найти первую неисправную.
# У нас есть функция isBadVersion(version) которая возвращает bool
# Нужно реализовать поиск первой плохой версии используя как можно меньшее колличество вызовов фун.
from random import randint

lst_version = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
bad = randint(2, len(lst_version))
print(f"***Random/unknown bed version: {bad}***")


def is_bad_vers(ver):
    if ver < bad:
        return False
    else:
        return True


# 1 Way
def binary_search_recursive(list_1, start, end):
    if start > end:
        return "All versions is bad"
    else:
        mid = (start + end) // 2
        if is_bad_vers(list_1[mid - 1]) is False and is_bad_vers(list_1[mid]) is True:
            return f"'{list_1[mid]}' - is a first bad version!"
        elif is_bad_vers(list_1[mid]) is True:
            return binary_search_recursive(list_1, start, mid - 1)
        else:
            return binary_search_recursive(list_1, mid + 1, end)


print(binary_search_recursive(lst_version, 0, len(lst_version)))


# 2 Way
def bruteforce_search(lst):
    for i in lst:
        if is_bad_vers(i - 1) is False and is_bad_vers(i) is True:
            return f"'{i}' - is a first bad version! #Way 2"


print(bruteforce_search(lst_version))


# 2. Для списка целых чисел nums, отсортированного по возрастанию вернуть
# массив квадратов каждого из чисел отсортированного по возрастанию

nums = [-4, -1, 0,  3, 10]


# Way 1
def sort_quad(lst):
    lst_quad = []
    for i in lst:
        lst_quad.append(i ** 2)
    return sorted(lst_quad)


print(sort_quad(nums))


# Way 2
def sort_quad_2(i):
    return i ** 2


lst_quad_2 = sorted(map(sort_quad_2, nums))
print(f"{lst_quad_2} #Way 2")


# 3. Для списка целцх чисел nums, переместите все 0 в конец, сохраняя относительнюю последовательность
# ненулевых элементов. Надо сделать это сразу, не делая копию массива

# Way 1
nums_0 = [0, 1, 0, 3, 12, 0, 11, 6, 3]


def zero_sort(mass):
    mass.sort(key=lambda i: i == 0)
    return mass


zero_sort(nums_0)
print(nums_0)


# Way 2
nums_1 = [1, 0, 3, 4, 5, 0, 7, 0, 9]


def zero_sort_2(mass_2):
    for i in mass_2:
        if i == 0:
            mass_2.append(mass_2.pop(mass_2.index(i)))
    return mass_2


zero_sort_2(nums_1)
print(f"{nums_1} #Way 2")


# 4. Дано два отсортированных списка, вернуть один отсортированный список
# с элементами первого второго

lst_1 = [1, 3, 5, 7, 9]
lst_2 = [0, 2, 4, 6, 8]


# Way 1
def concat_lst(lst1, lst2):
    sorted_list_3 = sorted(lst1 + lst2)
    return sorted_list_3


print(concat_lst(lst_1, lst_2))


# Way 2
def merge_lst(ls_1, ls_2):
    result = list.__add__(ls_1, ls_2)
    return sorted(result)


print(f"{list(merge_lst(lst_1, lst_2))} #Way 2")


# 5. Есть массив букв, перевернуть его, не используя revers & [::-1]

some_lst = ["H", "e", "l", "l", "o", "!"]


def no_reverse(lst_func):
    lst_rev = [lst_func.pop() for j in range(len(lst_func))]
    return lst_rev


some_lst = no_reverse(some_lst)
print(some_lst)


# Way 2
some_lst_2 = ["P", "y", "t", "h", "o", "n"]


def no_reverse_2(variable):
    res = []
    for i in range(len(variable)-1, -1, -1):
        res += variable[i]
    return res


some_lst_2 = no_reverse_2(some_lst_2)
print(f"{some_lst_2} #Way 2")


# 6. Написать функцию которя принимает число "n", а возвращает значение числа фибоначи
# с порядковым номером "n"


# Way 1
def fibonacci_recurse(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_recurse(n - 1) + fibonacci_recurse(n - 2)


print(f"{fibonacci_recurse(4)}   <-- Fibonacci")
print(f"{fibonacci_recurse(3)}   <-- Fibonacci")
print(f"{fibonacci_recurse(6)}   <-- Fibonacci")


# Way 2
def fibonacci_cycle(n):
    fib1 = 1
    fib2 = 1
    for i in range(2, n):
        fib1, fib2, = fib2, fib1 + fib2
    return fib2


print(f"{fibonacci_cycle(4)}  <-- Fibonacci Way 2")
print(f"{fibonacci_cycle(3)}  <-- Fibonacci Way 2")
print(f"{fibonacci_cycle(6)}  <-- Fibonacci Way 2")
