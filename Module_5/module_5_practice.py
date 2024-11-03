class Database:
    """
    класс для базы данных пользователей
    """

    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """

    def __init__(self, username, password):
        self.username = username
        # if password == password_confirm:
        self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = input('Hello! Please choose: \n1 - Log in\n2 - Sign in\n')
        if int(choice) == 1:
            login = input("Login: ")
            if login in database.data:
                password = input("Password: ")
                if password == database.data[login]:
                    print("You're in!")
                    continue
                else:
                    print('Wrong password, try again')
            else:
                print('Wrong login, try again')
                continue

        elif int(choice) == 2:
            # user = User(input("Введите логин: "), password := input("Введите пароль: "),
            # password2 := input("Подтвердите пароль: ")) - # ":=" - моржовый оператор, позволяет присвоить
            # значение там, где обычный оператор не работает
            username = input("Login: ")
            password = input("Password: ")
            sum_capital = 0
            sum_digit = 0
            for i in password:
                if i == i.capitalize():
                    sum_capital += 1
                if i.isdigit():
                    sum_digit += 1
            if len(password) < 4 or sum_digit == 0 or sum_capital == 0:
                print('Create more safe password')
                continue

            # user = User('ezhi', password := 'mur', password2 :='mur')
            password2 = input("Введите пароль еще раз: ")
            if password != password2:
                print('Wrong pass, try again')
                continue
            user = User(username, password)
            database.add_user(user.username, user.password)
            print(database.data)
        else:
            print('Wrong choice, try again')




# print(User.__doc__) # - показывает описание класса
# хорошо бы сюда еще навесить интерфейс из tk