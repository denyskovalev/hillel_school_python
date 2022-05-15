
# Вывести квадраты чисел от 1 до 10

for i in range(1, 11):
    print(f"Квадрат числа {i}: ", i ** 2)

# Вывести квадраты чисел от 10 до 1

for i in range(1, 11):
    b = (11 - i)
    print(f"Квадрат числа {b}: ", b ** 2)

# Выполнить все задания через While
# 1. Найти максимальное число в списке, но не больше 100

lst_1 = [90, 30, -7, 55, 360, 51, 400, -200, 95]
i = 0
max_elem = lst_1[0]

while i < len(lst_1):
    if max_elem <= lst_1[i] <= 100:
        max_elem = lst_1[i]
    i += 1

print(f"Наибольший елемент из списка: {max_elem}")

# 2. Найти сумму всех чисел из списка что делятся на 3

lst_2 = [3, 6, 9, 15, 22, 24, 37, 17, 14]
all_sum = 0
i = 0

while i < len(lst_2):
    if lst_2[i] % 3 == 0:
        all_sum += lst_2[i]
    i += 1

print("Сумма чисел которые делятся на 3: ", all_sum)

# 3. Вывести квадраты чисел от 10 до 30

lst_3 = list(range(10, 31))
i = lst_3[0]

while i <= lst_3[-1]:
    print(f"Квадрат числа {i}: ", i ** 2)
    i += 1

# 4. Найти наибольшее по длинне слово в списке

lst_maxword = ["Picture", "Cup", "Hair", "Sun", "Currently"]
i = 0
longest_word = []

while i < len(lst_maxword):
    if len(lst_maxword[i]) > len(longest_word):
        longest_word = lst_maxword[i]
    i += 1

print("Longest word: ", longest_word)

# 5. Вывести отдельно сумму парных и непарных чисел списка

lst_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pair_sum = 0
unpair_sum = 0
i = 0

while i < len(lst_numbers):
    if lst_numbers[i] % 2 == 0:
        pair_sum += lst_numbers[i]
    else:
        unpair_sum += lst_numbers[i]
    i += 1

print(f"Sum paired numbers: {pair_sum}\nSum unpaired numbers: {unpair_sum}")

# Седлать функцию которая принимает массив и возвращает его сумму

elements = [10, 20, 20, 50]


def massive_sum_func(x):
    sum_massive = 0
    for i in x:
        sum_massive += i
    return sum_massive


print(f"Sum elements in list: ", massive_sum_func(elements))

# Создать функцию которая принимает два аргумента. Первый - список, второй - "k"
# Найти наибольшее число списка, индекс которого меньше за "k". Если длинна списка меньше "k" - вернуть "0"

examp_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]


def example_sort(ex_lst, k):
    if len(ex_lst) < k:
        return 0

    i = 0
    elem_max = 0

    while i < k:
        if ex_lst[i] > elem_max:
            elem_max = ex_lst[i]
        i += 1

    return elem_max


print(example_sort(examp_list, 5))
print(example_sort(examp_list, 8))
print(example_sort(examp_list, 16))

