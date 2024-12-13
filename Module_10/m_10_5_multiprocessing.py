import multiprocessing
import time
import threading

counter = 0

def first_worker(n):
    global counter
    for i in range(n):
        counter += 1
        time.sleep(0.011)
    print(f'Первый рабочий изменил значение счётчика, и теперь он равен {counter}')

def second_worker(n):
    global counter
    for i in range(n):
        counter += 1
        time.sleep(0.02)
    print(f'Второй рабочий изменил значение счётчика, и теперь он равен {counter}')

# потоки:
# thread1 = threading.Thread(target=first_worker, args=(10, ))
# thread2 = threading.Thread(target=second_worker, args=(5, ))
#
# thread1.start()
# thread2.start()

# процессы
if __name__ == '__main__': # без этой конструкции выдаст ошибку
    process1 = multiprocessing.Process(target=first_worker, args=(10, ))
    process2 = multiprocessing.Process(target=second_worker, args=(5, ))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
print(counter)