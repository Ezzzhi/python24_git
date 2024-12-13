import threading
from threading import Thread, Event
import time

def first_worker():
    print('Первый рабочий приступил к своей задаче')
    event.wait()
    print(f'Первый рабочий продолжил выполнять задачу')
    time.sleep(5)
    print(f'Первый рабочий закончил выполнять задачу')

def second_worker():
    print('Второй  рабочий приступил к своей задаче')
    time.sleep(10)
    print(f'Второй  рабочий закончил выполнять задачу')
    event.set()

event = Event()
thread1 = threading.Thread(target=first_worker)
thread2 = threading.Thread(target=second_worker)


print(event.is_set())

thread1.start()
thread2.start()

event.set()
print(event.is_set()) # True
event.clear() # сбрасывает установленный флаг
print(event.is_set()) # False