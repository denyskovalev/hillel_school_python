
# Создать словарь характеристик автотранспорта (Марка, Модель, Год, Пробег, Цвет)

avto_dict = {
    "name_dir": "Renault",
    "model": "Kiger",
    "year": "2021",
    "other": {"mileage": "0", "color": "red"}
}

# Удалить из словаря и вывести на экран год автомобиля

y = avto_dict.pop("year")
print(y)

# Создать две произвольные множества чисел найти в них общие элементы

s1 = {3, 4, 5, 6, 20, 40}
s2 = {1, 2, 3, 4, 5, 6, 100}

print(s1.intersection(s2))

# СОздать две переменные password, repead_password.
# Напечатать - True если они одинаковы, False - если разные

password = input("Введите пароль: ")
repead_password = input("Повторите пароль: ")

print(password == repead_password)

# СОздать произвольный список. Перевести его в tuple и вывести первые 3 элемента

samp_list = ["word", 2022, (10, 20), "word2", "word3", 2020]

samp_list = tuple(samp_list)
print(samp_list[:3])

# Найти mod от деления 121 на 7

a = 121
b = 7

print(a % b)

# Найти div 121 на 7

print(a // b)

# Вычислить 2 в степени 10 (2^10)

c = 2 ** 10
print(c)