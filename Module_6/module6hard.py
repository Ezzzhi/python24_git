# Дополнительное практическое задание по модулю 6
# Задание "Они все так похожи"

from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if Figure.__is_valid_color(color[0], color[1], color[2]):
            self.__color = list(color)
            self.filled = True
        else:
            self.__color = [0, 0, 0]
            self.filled = False

        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count


    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        for i in (r, g, b):
            if not isinstance(i, int) or (0 >= i) or (i >= 255):
                return False
        return True

    def set_color(self, r, g, b):
        if Figure.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if len(sides) != len(self.__sides):
            return False
        else:
            for side in list(sides):
                if not isinstance(side, int) or side <= 0:
                    return False
            return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __str__(self):
        return f'{self.__class__.__name__}: color {self.get_color()}, sides {self.get_sides()}'


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__len__() / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2

class Triangle(Figure):

    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        p = len(self)/2
        s = p
        for side in self.get_sides():
            s *= (p - side)
        return s ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *side):
        if len(side) == 1:
            side = [side[0]] * self.sides_count
        super().__init__(color, *side)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            new_sides = new_sides * self.sides_count
        super().set_sides(*new_sides)

    def get_volume(self):
        list_ = self.get_sides()
        return list_[0] ** 3



if __name__ == '__main__':

    print('Добавление валидных фигур')
    circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
    print(circle1)
    triangle1 = Triangle((236, 26, 65), 6, 8, 12)
    print(triangle1)
    cube1 = Cube((222, 35, 130), 6)
    print(cube1)
    print()

    print('Добавление невалидных фигур')
    circle2 = Circle((500, 200, 100), 10, 5)  # (Цвет, стороны)
    print(circle2)
    triangle2 = Triangle((236, 456, 65), 6, 8)
    print(triangle2)
    cube2 = Cube((222, 'pink', 130), 6, 5, 3, 4)
    print(cube2)
    print()

    print('Проверка на изменение цветов')
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())
    print()

    print('Проверка на изменение сторон')
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    cube2.set_sides(5)  # Изменится
    print(cube2.get_sides())
    triangle1.set_sides(5, 3)  # Не изменится
    print(triangle1.get_sides())
    triangle2.set_sides(15, 7, 18)  # Изменится
    print(triangle2.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())
    print()

    print('Проверка периметра круга')
    print(len(circle1))
    print()

    print('Проверка площади треугольника')
    print(triangle1.get_square())
    print()

    print('Проверка объёма (куба)')
    print(cube1.get_volume())