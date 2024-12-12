import threading

counter = 0
lock = threading.Lock()

def increment(name):
    global counter
    lock.acquire()
    for i in range(1000):
        counter += 1
        print(name, counter, lock.locked())
    lock.release()

def decrement(name):
    global counter
    with lock:     # более лаконичная запись, смысл тот же, что в increment
        for i in range(1000):
            counter -= 1
            print(name, counter, lock.locked())

# конструкция try-except-finaly с замками:
def increment2(name):
    global counter
    try:
        for i in range(1000):
            counter += 1
            print(name, counter, lock.locked())
    except Exception:
        pass
    finally:
        lock.release()


thread1 = threading.Thread(target=increment, args=('thread1', ))
thread2 = threading.Thread(target=decrement, args=('thread2', ))
thread3 = threading.Thread(target=increment, args=('thread3', ))
thread4 = threading.Thread(target=decrement, args=('thread4', ))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
