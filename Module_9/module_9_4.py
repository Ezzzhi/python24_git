# Домашнее задание по теме "Создание функций на лету"
# Задача "Функциональное разнообразие":

# Lambda-функция:
# Даны 2 строки
# Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
# Здесь ? - место написания lambda-функции.
# Результатом должен быть список совпадения букв в той же позиции

first = 'Мама мыла раму'
second = 'Рамена мало было'

res = list(map(lambda x, y: x == y, first, second))
print(res)
print()



# Замыкание:
# Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
# Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр принимающий неограниченное количество данных любого типа.
# Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
# Функция get_advanced_writer возвращает функцию write_everything.

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        file = open(file_name, 'w', encoding='utf-8')
        for data in data_set:
            file.write(str(data) + '\n')
        file.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:
# Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
# В этом классе также определите метод __call__ который будет случайным образом выбирать слово из words
# и возвращать его. Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции
# можете использовать функцию choice из модуля random.

from random import choice

class MysticBall:

    def __init__(self, *words):
        self.words = list(words)

    def __call__(self):
        return self.words[choice(range(0, len(self.words)))]


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
