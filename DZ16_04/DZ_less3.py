import math
# Найти максимальное число в списке, но не больше 100

lst_1 = [1, 10, -40, 250, 30, 40, 90, 70, 96, 75, 400, -10]
def_count = 0

for i in lst_1:
    if i <= 100 and i > def_count:
        def_count = i

print("Макс число(не больше 100): " + str(def_count))

# Найти сумму чисел в списке которые делятся на 3

lst_2 = [2, 5, 6, 12, 36, 4, 9, 7]
lstsum = 0

for i in lst_2:
    if i % 3 == 0:
        lstsum += i

print("Сумма чисел которые делятся на 3: " + str(lstsum))

# Вывести квадраты чисел от 10 до 30

lst_3 = list(range(10, 31))

for i in lst_3:
    print(i ** 2)

# Вывести из списка слов то слово в котором больше всего букв

lst_4 = ["Окунь", "Синхрофазотрон", "Тюлень", "Галустян", "Парацетамол", "Кошка"]
long_word = []

for i in lst_4:
    if len(i) >= len(long_word):
        long_word = i

print("Самое длинное слово: " + long_word)

# Посчитать и вывести на экран отдельно сумму парнх и непарных чисел

lst_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
paired_sum = 0
unpired_sum = 0

for i in lst_5:
    if i % 2 == 0:
        paired_sum += i
    else:
        unpired_sum += i

print("Сумма парных чисел: " + str(paired_sum))
print("Сумма непарных чисел: " + str(unpired_sum))

# Вычислить квадратное уравнение: ax^2+bx+c=0

print("Введите коефф.уравнения 'ax^2+bx+c=0': ")
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

discr = (b ** 2) - (4 * a) * c
print("Дискриминант: " + str(discr))

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(f"x1 = {x1} x2 = {x2}")
elif discr == 0:
    x = -b / (2 * a)
    print(f"Одинаковые корни: x = {x}")
else:
    print("Корней нет")

# Найти самое маленькое из трех чисел

rand_numb = [26, -23, 17]
low_numb = 0

for i in rand_numb:
    if i < low_numb:
        low_numb = i

print("Наименьшее число из трёх: " + str(low_numb))

# Пользователь вводит год. Если он высокосный написать "Yes" если нет "No"

vis_year = int(input("Высокосный? Введите год: "))

if vis_year % 4 ==0:
    print("Yes")
else:
    print("No")

# Пользователь вводит бал (0 - 100) в цыфровом формате.
# Нужно преобразовать бал в Болонскую систему (A - F)

score = int(input("Ведите бал (0-100): "))

if score >=101 or score <= -1:
    print("Неверный диапазон значения. (от 0 до 100)")
elif score >= 80:
    print("Ваша оценка: A")
elif score >= 60 and score <= 80:
    print("Ваша оценка: B")
elif score >= 50 and score <= 60:
    print("Ваша оценка: C")
elif score >= 45 and score <= 50:
    print("Ваша оценка: D")
elif score >= 25 and score <= 45:
    print("Ваша оценка: E")
else:
    print("Ваша оценка: F")