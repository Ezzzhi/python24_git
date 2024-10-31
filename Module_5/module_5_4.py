# Домашняя работа по уроку "Перегрузка операторов"
# Задача "История строительства"

class House:
    roof = True
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if (new_floor > self.number_of_floors) or (new_floor < 1):
            print('"Такого этажа не существует"')
        else:
            for i in range (0, new_floor):
                print(i + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.__len__()}'

    def __eq__(self, other):
        if isinstance(other.__len__(), int):
            return self.__len__() == other.__len__()
        else:
            return 'Error'

    def __lt__(self, other):
        if isinstance(other.__len__(), int):
            return self.__len__() < other.__len__()
        else:
            return 'Error'

    def __le__(self, other):
        if isinstance(other.__len__(), int):
            return self.__len__() <= other.__len__()
        else:
            return 'Error'

    def __gt__(self, other):
        if isinstance(other.__len__(), int):
            return self.__len__() > other.__len__()
        else:
            return 'Error'

    def __ge__(self, other):
        if isinstance(other.__len__(), int):
            return self.__len__() >= other.__len__()
        else:
            return 'Error'

    def __ne__(self, other):
        if isinstance(other.__len__(), int):
            return self.__len__() != other.__len__()
        else:
            return 'Error'

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            return 'Error'

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__(self):
        # мне захотелось немного дополнить метод, чтобы в истории было видно, что ЖК снесен
        for index, value in enumerate(self.houses_history):
            if value == self.name:
                self.houses_history[index] += ' снесен'
                print(self.houses_history[index] + ', но он останется в истории')



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# долго пытался понять, почему выводится последняя строка с удалением ЖК Эльбрус
# потом дошло, что после отработки программы метод del срабатывает автоматически)
