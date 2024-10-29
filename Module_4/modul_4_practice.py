# from math import pi
import math

# print(globals())

# globals_dict = {'__name__': '__main__', '__doc__': None, '__package__': None,\
#                 '__loader__': '<_frozen_importlib_external.SourceFileLoader object at 0x000001B7112F4380>',\
#                 '__spec__': None, '__annotations__': {}, '__builtins__': "<module 'builtins' (built-in)>",\
#                 '__file__': 'D:\\_Python24\\Module_4\\modul_4_practice.py', '__cached__': None,\
#                 'math': "<module 'math' (built-in)>"}
#
# for key, value in globals_dict.items():
#     print(key, value)

def insertion_sort(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
        return ls


# for path in sys.path:
#     print(path)

# def divide(divident, divisor):
#     if divisor == 0:
#         return 'Ошибка'
#     else:
#         return divident / divisor
#
# print(divide(5, 6))


# def square(x):
#     d = x**2
#     def even(x):
#         d = x*2
#     even(x)
#     return d
#
# print(square(4))


print(math.pi)


print(object)