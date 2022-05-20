# pylint: skip-file

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]


def binary_search_recursive(some_lst, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == some_lst[mid]:
        return f"First invalid version: {some_lst[mid]}"

    if element < some_lst[mid]:
        return binary_search_recursive(some_lst, element, start, mid - 1)
    else:
        return binary_search_recursive(some_lst, element, mid + 1, end)


print(binary_search_recursive(lst, 121, 0, len(lst)))
