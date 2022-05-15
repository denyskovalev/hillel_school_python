
import time


def some_de(some_func):

    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = some_func(*args, **kwargs)

        end_time = time.time()
        print(f"Time running - ", (end_time - start_time) * 100)
        return result
    return wrapper


@some_de
def adder_func(a, b, c):
    return a + b + c


# adder_func(3 ** 10, 4 ** 400000000, 8 * 1000000)

"""practice"""

# Before running function print all arg & kwargs
# Print end function after completing running
# Return result * 10


def decoration_func(any_func):

    def decor_any(*args, **kwargs):
        print(f"Function start with: {args}, {kwargs}")

        result = any_func(*args, **kwargs)

        print("Func complete. End.")
        return result * 10
    return decor_any


@decoration_func
def adder_numbers(a, b, c):
    return a + b + c


# print(adder_numbers(3, 2, 4))


"""Files"""

# n - reed from input file
# find all simple number from 1 to n
# write result from result file


def if_simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


file = open("less7_input.txt")
n = int(file.read())

file.close()

lst = [i for i in range(1, n+1)]

lst = list(filter(if_simple, lst))

print(lst)

file_result = open("less7_result.txt", "a")

file_result.write(str(f"{lst}\n"))

