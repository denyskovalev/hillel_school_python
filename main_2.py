import math

"""           НАПИСАТЬ ФУНКЦИИ КОТОРЫЕ:           """
# 1. Принимает радиус круга, возвращает его длинну. Обработать случаи когда функция принимает не число


def radius_to_len(rad_circle):

    p_num = math.pi
    try:
        len_circle = 2 * p_num * rad_circle
        return len_circle
    except TypeError:
        return "Error: Wrong data type. Enter numbers."


print(radius_to_len(5))
print(radius_to_len('a'))


# 2. Принимает радиус круга, возвращает его площадь. Обработать случаи когда функция принимает не число


def radius_to_area(radius_circle):

    p_num = math.pi
    try:
        area_circle = p_num * radius_circle ** 2
        return area_circle
    except:
        return "Error: Wrong data type. Enter numbers."


print(radius_to_area(5))
print(radius_to_area('a'))


# 3. Принимает число, возвращает является ли число полиндромом


def if_palindrome(pal):

    palinfrome = str(pal)
    reversed_pal = palinfrome[::-1]
    if palinfrome == reversed_pal:
        return f"{palinfrome} - is a palindrome"
    else:
        return f"{palinfrome} - not palindrome"


print(if_palindrome(123456789))
print(if_palindrome(123454321))


# 4. Функция принимает "n", оно должно быть больше нуля. С помощью рекурсии вывести все
# числа меньше "n" и болье 0

def recursion_1(n):

    if n > 0:
        if n == 1:
            return 1
        print(n)
        return recursion_1(n - 1)

    else:
        return f"{n} <- sub 0. Or wrong data type\n"


print(recursion_1(5))
# print(recursion_1(0))
# print(recursion_1(1))
# print(recursion_1(-5))


# 5. Написать lambda функцию которая принимает x,y. И возвращает x^2+y^2

lambd_numb = lambda x, y: (x ** 2) + (y ** 2)

print(lambd_numb(5, 5))


# 6. Написать lambda функцию которая принимает слово и возвращает его длинну

lambd_word = lambda x: len(x)

print(f"Len this word -> {lambd_word('pako')}")
print(f"Len this word -> {lambd_word('abraham')}")


# 7. написать map который превращает все числа в списке на строку

lst_numbers = [1, 2, 3, 4, 5, 10, 20, 50, 100, 1000]


def num_to_str(ls):
    return str(ls)


lst_str = list(map(num_to_str, lst_numbers))
print(f"Number to string -> {lst_str}")


# 8. Написать fillter который оставляет в списке только числа > 10

lst_for_filter = [1, 2, 3, 4, 5, 6, 9, 12, 13, 14, 15, 16, 17, 20]


def num_func(lst_10):
    return lst_10 < 10


lst_after_filter = list(filter(num_func, lst_for_filter))
print(f"After filter -> {lst_after_filter}")

# 9. Есть список слов, с помощью map удалить с каждого лова все буквы "а" 2 способа

lst_words = ["abraham", "asus", "acer", "cat", "cup", "Harry"]

# 9.1


def repl_a(rs):

    some_word = ""
    for i in rs:
        if i != "a":
            some_word = some_word + i
    return some_word


list_result = list(map(repl_a, lst_words))
print(f"1 way -> {list_result}")

# 9.2

list_result_2 = list(map(lambda x: x.replace("a", ""), lst_words))
print(f"2 way  (with lambda) -> {list_result_2}")


# 10. Есть список слов, с помощью filter оставить только те слова, в которых кол-во букв больше 4 (2 способа)

lst_words_10 = ["sun", "hair", "function", "tuple", "python"]

# 10.1


def lst_len_words(t):
    return len(t) > 4


list_result_3 = list(filter(lst_len_words, lst_words_10))

print(f"1 way (len words < 10) -> {list_result_3}")

# 10.2

list_result_4 = list(filter(lambda x: len(x) > 4, lst_words_10))

print(f"2 way (len words < 10)(with lambda) -> {list_result_3}")
