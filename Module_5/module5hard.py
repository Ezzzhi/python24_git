# Дополнительное практическое задание по модулю: "Классы и объекты."
# Задание "Свой YouTube"

import time

class User:

    """
    Класс, создающий пользователя с атрибутами никнейм, пароль и возраст
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

class Video:

    """
    Класс, создающий видео с атрибутами: название, длительность,
    текщий момент просмотра, возрастное ограничение
    """

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item: str):
        return item.lower() in self.title.lower()


class UrTube:

    """
    Класс, управляющий регистрацией, входом и выходом пользователей,
    а также добавлением, поиском и просмотром видео.
    """

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        is_user = 0
        password = hash(password)
        if self.users:
            for user in self.users:
                if user.nickname == nickname:
                    is_user = 1
                    if user.password == password:
                        print(f'{nickname}, вход выполнен')
                        self.current_user = user
                        print('Current user', self.current_user)
                        break
                    else:
                        print('Неправильный пароль')
                        break

            if is_user == 0:
                print(f'Пользователь {nickname} не найден, пожалуйста, зарегистрируйтесь')
        else:
            print(f'Пользователь {nickname} не найден, пожалуйста, зарегистрируйтесь')


    def register(self, nickname: str, password: int, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                break
        else:
            new_user = User(nickname, hash(password), age)
            self.users.append(new_user)
            self.current_user = new_user



    def log_out(self, current_user):
        self.current_user = None

    def add(self, *args):
        for movie in args:
            if movie not in self.videos:
                self.videos.append(movie)

    def get_videos(self, other):
        video_list = []
        for video in self.videos:
            if  video.__contains__(other):
                video_list.append(video.title)
        return video_list

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for x in self.videos:
            if x.title == title:
                if x.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return

                for i in range(1, x.duration + 1):
                    print(i, end=' ')
                    time.sleep(1)
                    x.time_now += 1
                x.time_now = 0
                print('Конец видео')





if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')