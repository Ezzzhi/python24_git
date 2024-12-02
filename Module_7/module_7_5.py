"""
Домашнее задание по теме "Файлы в операционной системе".
Цель задания:

Освоить работу с файловой системой в Python, используя модуль os.
Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize
и использование модуля time для корректного отображения времени.

Задание:

Создайте новый проект или продолжите работу в текущем проекте.
Используйте os.walk для обхода каталога, путь к которому указывает переменная directory.
Примените os.path.join для формирования полного пути к файлам.
Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
Используйте os.path.getsize для получения размера файла.
Используйте os.path.dirname для получения родительской директории файла.
"""
import os
import time

def time_mod(file_name):
    time_sec = os.path.getmtime(file_name) # получаем время модификации файла в секундах
    time_local = time.localtime(time_sec)# получаем время в формате struct_time
    return time.strftime('%d.%m.%Y %H:%M:%S', time_local) # получаем время в указанном формате

for dir_path, dir_names, file_names in os.walk('.'):
    # перебрать каталоги
    for dir_name in dir_names:
        print('Папка:', os.path.join(dir_path, dir_name))
    # перебрать файлы
    for filename in file_names:
        file_path = os.path.join(dir_path, filename)
        file_size = os.path.getsize(file_path)
        print(
            f'Обнаружен файл: {filename}, Путь: {file_path}, '
            f'Размер: {file_size} байт, '
            f'Время изменения: {time_mod(file_path)}, Родительская директория: {os.path.dirname(file_path)}')