# Домашнее задание по теме "Зачем нужно наследование"
# Задача "Съедобное, несъедобное"


class Animal:

    alive = True
    fed = False

    def __init__(self, name):
        self.name = name
        self.alive = Animal.alive
        self.fed = Animal.fed

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.fed = False

class Mammal(Animal):
    pass

class Predator(Animal):
    pass


class Plant:

    edible = False

    def __init__(self, name):
        self.name = name

class Flower(Plant):
    pass

class Fruit(Plant):

    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(f'{a1.name} is alive: {a1.alive}')
print(f'{a2.name} is fed: {a2.fed}')
a1.eat(p1)
a2.eat(p2)
print(f'{a1.name} is alive: {a1.alive}')
print(f'{a2.name} is fed: {a2.fed}')