
# Сгенерировать список от 1 до 100 всех чисел что делтся на 2 --- 2 способа

lst_1 = [i for i in range(1, 101) if i % 5 == 0]

print(lst_1) # 1

######

lst_2 = list(range(1, 101))
lst_3 = []

for i in lst_2:
    if i % 5 == 0:
        lst_3.append(i)

print(lst_3) # 2

########

lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

input_str = "pythonist"

# Выводим в консоль исходную строку
print("Исходная строка: " + input_str)

result_str = ""

for i in input_str:
    if i != "h":
        result_str = result_str + i

    # Выводим в консоль строку после удаления i-го элемента
print("Строка после удаления i-го элемента: " + result_str)