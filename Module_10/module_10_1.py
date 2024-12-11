# Домашнее задание по теме "Введение в потоки"
"""
Задача "Потоковая запись в файлы":
Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов,
file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл
с прерыванием после записи каждого на 0.1 секунду.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию write_words.
После вызовов функций создайте 4 потока для вызова этой функции.
Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков.
"""
import threading
from datetime import datetime
from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(1, word_count+1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

startTime = datetime.now()
write_words(10, 'example1.txt')
write_words(30,'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
endTime = datetime.now()
print (f'Время выполнения функций: {endTime - startTime}')
print()

startTime = datetime.now()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt',))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt',))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt',))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt',))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
endTime = datetime.now()
print (f'Время выполнения потоков: {endTime - startTime}')