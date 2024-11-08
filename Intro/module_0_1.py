# print ('Hello world')
# print ('Hello' * 5)

class Animal:

    _DEGREE_OF_DANGER = 0
    live = 5

    def attack(self):
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, I'm attacking you O_O")
        else:
            print("Sorry, I'm peaceful :)")

class PoisonousAnimal(Animal):

    _DEGREE_OF_DANGER = 8
    live = 6

    def attack(self):
        super().attack()


class Duckbill (PoisonousAnimal):

    sound = "Click-click-click"

db = Duckbill()
db.attack()
print(db.live)