"""Домашнее задание по теме "Позиционирование в файле".
Цель: Закрепить знания о позиционировании в файле, использовав метод tell() файлового объекта.
Написать усовершенствованную функцию записи.

Задача "Записать и запомнить":
Создайте функцию custom_write(file_name, strings), которая принимает аргументы
file_name - название файла для записи, strings - список строк для записи.
Функция должна:
Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>,
<байт начала строки>), а значением - записываемая строка. Для получения номера байта
начала строки используйте метод tell() перед записью."""

def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'a', encoding='utf-8')
    a = 0
    for string in strings:
        a += 1
        b = file.tell()
        file.write(string + '\n')
        strings_positions[(a, b)] = string
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)