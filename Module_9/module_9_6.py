# Домашнее задание по теме "Генераторы"
"""
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.
"""

from itertools import combinations

def all_variants(text):
    for k in range(1, len(text) + 1):
        txt_lst = []
        b = combinations(text, k)
        txt_lst.extend(b)
        for j in txt_lst:
            j = list(j)
            yield (''.join(j))


a = all_variants("abc")
for i in a:
    print(i)