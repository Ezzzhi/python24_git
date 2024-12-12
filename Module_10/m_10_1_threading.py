import threading
import time

def func1():
    for i in range(10):
        time.sleep(1)
        print('\n', i, threading.current_thread())

def func2(x):
    for i in range(10, 20):
        time.sleep(x)
        print(i, threading.current_thread())
        print(threading.current_thread().is_alive())

thread = threading.Thread(target=func2, args=(1, ))
thread.start()
thread.join()
print(thread.is_alive())
func1()

print(threading.enumerate()) # выводит список потоков
print(threading.current_thread()) # выводит текущий поток