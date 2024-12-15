import multiprocessing as mp
from PIL import Image
from queue import Empty
from datetime import datetime as dt


def resize_image(image_paths, queue_): # открывает картинку из списка, меняет размер, пробрасывает в очередь не сохраняя
    for image_path in image_paths:
        image_ = Image.open(image_path)
        image_ = image_.resize(size=(800, 600))
        queue_.put((image_path, image_))


def change_color(queue_): # достаем картинку из очереди, меняем ей цвет, после этого сохраняем
    while True:
        try:
            image_path, image_ = queue_.get(timeout=5)
        except Empty:
            break
        image_ = image_.convert('L')
        image_.save(image_path)


if __name__ == '__main__':
    data = []
    queue = mp.Queue()

    for image in range(1, 11):
        data.append(f'./images/img_{image}.jpg')

    resize_process = mp.Process(target=resize_image, args=(data, queue,))
    change_color_process = mp.Process(target=change_color, args=(queue,))

    start = dt.now()

    resize_process.start()
    change_color_process.start()

    resize_process.join()
    change_color_process.join()

    end = dt.now()
    print(f'Run time is {end - start}')
