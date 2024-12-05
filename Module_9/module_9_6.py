# Домашнее задание по теме "Генераторы"
"""
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.
"""

def all_variants(text):
    for k in range(len(text)):
        for j in range(len(text) - k):
            txt = text[k:j + k + 1]
            yield txt

# test:
a = all_variants("abc")
for i in a:
    print(i)