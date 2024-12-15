from datetime import datetime as dt
import multiprocessing as mp
from PIL import Image


def resize_image(image_paths, pipe_: mp.Pipe, stop_event): # открывает картинку из списка, меняет размер, пробрасывает в очередь не сохраняя
    for image_path in image_paths:
        image_ = Image.open(image_path)
        image_ = image_.resize(size=(800, 600))
        image_.save(image_path)
        pipe_.send(image_path)
    stop_event.set()


def change_color(pipe_: mp.Pipe, stop_event): # достаем картинку из очереди, меняем ей цвет, после этого сохраняем
    while not stop_event.is_set():
        image_path = pipe_.recv()
        image_ = Image.open(image_path)
        image_ = image_.convert('L')
        image_.save(image_path)


if __name__ == '__main__':
    data = []
    queue = mp.Queue()
    conn1, conn2 = mp.Pipe()
    stop_event = mp.Event()

    for image in range(1, 11):
        data.append(f'./images/img_{image}.jpg')

    resize_process = mp.Process(target=resize_image, args=(data, conn1, stop_event, ))
    change_color_process = mp.Process(target=change_color, args=(conn2, stop_event, ))

    start = dt.now()
    resize_process.start()
    change_color_process.start()

    resize_process.join()
    change_color_process.join()
    end = dt.now()
    print(f'Run time is {end - start}')
