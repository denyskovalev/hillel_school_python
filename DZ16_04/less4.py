

# Найти сумму элементов списка ##########################################

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# s = 0
# i = 0
#
# while i < len(lst):
#     s += lst[i]
#     i += 1
#
# print(s)
# print("End")

# Найти Макс число в помощью while #########################################

# lst_2 = [10, 20, 100, -5, 400, 700]
#
# i = 0
# max_el = lst_2[0]
#
# while i < len(lst_2):
#     if lst_2[i] > max_el:
#         max_el = lst_2[i]
#         i += 1
#     else:
#         i += 1
#
# print(max_el)

# Найти числа на которые делится число ###########################

# n = 50 # 1, 2, 5, 10, 25, 50
# k = 70 # 1, 2, 5, 7, 10, 14, 35, 70
# lst = []
# lst_2 = []
# s = n + 1
# m = k + 1
# max_deliel = 0
#
# for i in range(1, s):
#     if n % i == 0:
#         lst.append(i)
# for i in range(1, m):
#     if k % i == 0:
#         lst_2.append(i)
#
# print(f"Делители {n}: {lst}")
# print(f"Делители {k}: {lst_2}")
#
# result = list(set(lst) & set(lst_2))
#
# for i in result:
#     if i >= max_deliel:
#         max_deliel = i
#
# print(f"Наибольший общий делитель: {max_deliel}")

# Сделатьфункцию котораявычисляет делители передаваемого числа
#
# def res_number(num):
#     res_lst = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             res_lst.append(i)
#     return res_lst
#
# print(res_number(50))
# print(res_number(70))