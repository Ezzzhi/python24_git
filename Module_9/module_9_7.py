# Домашнее задание по теме "Декораторы"
"""
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three).
Функция декоратор (is_prime), которая распечатывает "Простое",
если результат 1ой функции будет простым числом и "Составное" в противном случае.
"""

def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        for i in range(2, res//2):
            if not res % i:
                print('Составное')
                return res
        print('Простое')
        return res
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

result2 = sum_three(2, 3, 7)
print(result2)