"""
1. Написать функцию, которая возвращает другую функцию, повторения двух символов «n» раз.
У нас есть какая-то строчка, и нам нужно написать функцию, которая будет возвращать повторение
первых двух символов. Но это не просто функция, это функция, которая будет генерировать другие функции,
которые будут повторять первые два символа «n» количество раз.
2. Создать массив функций с различными параметрами «n» и применить все эти функции поочерёдно
к аргументу «animal».
3. Применить все функции, которые мы до этого создадим, поочерёдно к массиву аргументов.
"""
# 1.
print(1)
animal = 'мишка'
animals = ['зайка', 'мишка', 'бегемотик']

def gen_repeat(n):

    def repeat(animal):
        return (animal[:2] + '-') * n + animal

    return repeat

test1 = gen_repeat(1)
test2 = gen_repeat(2)

print(test1(animal))
print(test2(animal))
print()

# 2.
print(2)
repetitions = [gen_repeat(n) for n in range(1, 4)]

result = [func(animal) for func in repetitions]

print(result)
print()

# 3

print(3)

res_mas = [func(animal) for animal in animals for func in repetitions]
print(res_mas)
print()

"""
II. Есть функция, которая возводит a в степень b. Нужно ее ускорить.
"""

def memorize_func(f):
    mem = {}
    def wrapper(*args):
        if args not in mem:
            mem[args] = f(*args)
            return f(*args)
        else:
            print('from mem')
            return mem[args]
    return wrapper


@memorize_func
def func(a, b):
    print('from func')
    return a ** b

print(func(3, 5))
print(func(3, 4))
print(func(3, 2))
print(func(3, 5))
print(func(3, 4))
print(func(3, 5))

